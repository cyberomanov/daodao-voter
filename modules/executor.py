import random

import requests
from loguru import logger

from data.constants import (
    STARS_CHAIN_ID,
    STARS_FEE_DENOM,
    STARS_GRPC,
    STARS_STAKING_DENOM,
    STARS_PREFIX,
    STARS_DEFAULT_DENOM,
    STARGAZE_EXPLORER
)
from datatypes.daodao.modules import ProposalModuleItem
from sdk.cosmpy.aerial.client import LedgerClient
from sdk.cosmpy.aerial.contract import LedgerContract
from sdk.cosmpy.aerial.exceptions import QueryTimeoutError
from sdk.cosmpy.aerial.wallet import LocalWallet
from tools.daodao.choose_vote import choose_vote
from tools.daodao.total_votes import get_total_votes
from tools.other.read_file import read_file
from tools.other.sleep import sleep_in_range
from tools.requests.daodao import (
    get_proposal_info,
    get_vote,
    get_voting_power,
    get_proposal_modules,
    get_reverse_proposals
)
from tools.requests.session import get_proxied_session
from tools.web3.balance import get_balance
from tools.web3.client import get_client
from tools.web3.contract import get_contract_by_address
from tools.web3.transaction import simulate_vote_tx, submit_tx
from tools.web3.wallet import get_wallet_from_mnemonic
from user_data import config


def process_wallet_vote(
        proposal_id: int,
        proposal_type: str,
        proposal_prefix: str,
        wallet: LocalWallet,
        session: requests.Session,
        client: LedgerClient,
        proposal_contract: LedgerContract,
        proposal_votes,
        proposal_choices,
        wallet_index: int
):
    vote = get_vote(
        session=session,
        dao_contract=str(proposal_contract.address),
        proposal_id=proposal_id,
        voter_address=str(wallet.address()),
        proposal_type=proposal_type
    )

    if vote.votedAt:
        if isinstance(vote.vote, str):
            logger.success(
                f"#{wallet_index} | {wallet.address()}: "
                f"already voted with [{vote.vote}] on [{proposal_prefix}/{proposal_id}]."
            )
        else:
            logger.success(
                f"#{wallet_index} | {wallet.address()}:"
                f" already voted with [{vote.vote.option_id}] on [{proposal_prefix}/{proposal_id}]."
            )
        return

    stars_balance = get_balance(client=client, address=str(wallet.address()), denom=STARS_FEE_DENOM)
    if stars_balance.float <= 2:
        logger.warning(
            f"#{wallet_index} | {wallet.address()}: balance {stars_balance.float} {STARS_DEFAULT_DENOM} is too low.")
        return

    # logger.info(f"#{wallet_index} | {wallet.address()}: balance {stars_balance.float} {STARS_DEFAULT_DENOM}.")

    random_vote = choose_vote(votes=proposal_votes, choices=proposal_choices)
    vote_tx = simulate_vote_tx(
        client=client,
        wallet=wallet,
        proposal_contract=proposal_contract,
        proposal_id=proposal_id,
        vote=random_vote
    )
    if vote_tx.estimated_gas and vote_tx.generated_tx:
        try:
            submitted_tx = submit_tx(
                client=client,
                wallet=wallet,
                tx=vote_tx.generated_tx,
                gas_limit=int(vote_tx.estimated_gas * config.gas_multiplier)
            )

            submitted_tx.wait_to_complete(timeout=30)
            logger.success(
                f"#{wallet_index} | {wallet.address()} | "
                f"voted with [{random_vote}] on [{proposal_prefix}/{proposal_id}] | "
                f"{STARGAZE_EXPLORER}/{submitted_tx.tx_hash}"
            )
            if config.sleep_between_txs[1]:
                sleep_in_range(sec_from=config.sleep_between_txs[0], sec_to=config.sleep_between_txs[1])
        except QueryTimeoutError:
            logger.error(f"#{wallet_index} | {wallet.address()} | timeout error.")
        except Exception as e:
            if "insufficient funds" in str(e):
                logger.warning(f"#{wallet_index} | {wallet.address()} | {stars_balance.float} is too low for voting.")
            else:
                logger.exception(f"#{wallet_index} | {wallet.address()} | {e.args}.")
    else:
        logger.error(f"#{wallet_index} | {wallet.address()}: invalid transaction simulation: {vote_tx.exception}.")


def process_proposal(
        proposal_contract: str,
        proposal_id: int,
        proposal_type: str,
        proposal_prefix: str,
        session: requests.Session,
        client: LedgerClient,
        mnemonics: list
):
    proposal = get_proposal_info(
        session=session,
        dao_contract=proposal_contract,
        proposal_id=proposal_id,
        proposal_type=proposal_type
    )
    proposal_contract = get_contract_by_address(address=proposal_contract, client=client)
    try:
        quorum_value = int(float(proposal.proposal.threshold['threshold_quorum']['quorum']['percent']) * 100)
    except:
        quorum_value = int(float(proposal.proposal.voting_strategy['single_choice']['quorum']['percent']) * 100)
    total_votes = get_total_votes(votes=proposal.proposal.votes, choices=proposal.proposal.choices)
    total_power = int(proposal.proposal.total_power)
    turnout = round(100 / total_power * total_votes, 2)
    if turnout < config.min_required_turnout_threshold:
        logger.warning(
            f'{proposal_prefix}/{proposal_id}: {proposal.proposal.votes} - '
            f'{turnout}/{quorum_value}% turnout, waiting for more votes.'
        )
    else:
        logger.info(f"{proposal_prefix}/{proposal_id}: {proposal.proposal.votes} - {turnout}/{quorum_value}% turnout.")
        random.shuffle(mnemonics)
        for index, mnemonic in enumerate(mnemonics, start=1):
            process_wallet_vote(
                proposal_contract=proposal_contract,
                proposal_id=proposal_id,
                proposal_prefix=proposal_prefix,
                wallet=get_wallet_from_mnemonic(mnemonic=mnemonic, prefix=STARS_PREFIX),
                session=session,
                client=client,
                proposal_votes=proposal.proposal.votes,
                proposal_choices=proposal.proposal.choices,
                wallet_index=index,
                proposal_type=proposal_type
            )


def main_executor():
    mnemonics = read_file('user_data/mnemonic.txt')
    client = get_client(
        chain_id=STARS_CHAIN_ID,
        grpc=STARS_GRPC,
        fee_denom=STARS_FEE_DENOM,
        staking_denom=STARS_STAKING_DENOM,
        multiplier=config.gas_multiplier,
        fee_gas_price=config.fee_gas_price
    )

    with get_proxied_session(proxy=config.proxy) as session:
        voter_mnemonics = []
        for wallet_index, mnemonic in enumerate(mnemonics, start=1):
            wallet = get_wallet_from_mnemonic(mnemonic=mnemonic, prefix=STARS_PREFIX)
            voting_power = get_voting_power(
                session=session,
                dao_contract=str(config.dao_contract),
                voter_address=str(wallet.address()),
                height=client.query_latest_block().height
            )
            if voting_power.power > 0:
                voter_mnemonics.append(mnemonic)
                logger.info(f"#{wallet_index} | {wallet.address()}: voting power = {voting_power.power}.")
            else:
                logger.warning(f"#{wallet_index} | {wallet.address()}: voting power = {voting_power.power}.")

        active_proposal_modules = get_proposal_modules(session=session, dao_contract=config.dao_contract)
        proposal_modules_items = []
        for item in active_proposal_modules:
            if item.status == 'enabled':
                proposal_modules_items.append(
                    ProposalModuleItem(
                        prefix=item.prefix,
                        contract=item.address,
                        type="daoProposalSingle" if "single" in item.info.contract.lower() else "daoProposalMultiple"
                    )
                )
            else:
                logger.warning(f'{item}')

        random.shuffle(proposal_modules_items)
        for module in proposal_modules_items:
            total_proposals = get_reverse_proposals(
                session=session,
                proposal_contract=module.contract,
                proposal_type=module.type
            )

            open_proposals = [proposal for proposal in total_proposals if proposal.proposal.status == "open"]
            random.shuffle(open_proposals)
            for proposal in open_proposals:
                process_proposal(
                    proposal_contract=module.contract,
                    proposal_id=proposal.id,
                    proposal_type=module.type,
                    proposal_prefix=module.prefix,
                    session=session,
                    client=client,
                    mnemonics=voter_mnemonics
                )
