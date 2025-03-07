from datatypes.web3.transaction import SimulateTxResponse
from sdk.cosmpy.aerial.client import LedgerClient, prepare_and_broadcast_basic_transaction
from sdk.cosmpy.aerial.contract import LedgerContract, create_cosmwasm_execute_msg
from sdk.cosmpy.aerial.tx import Transaction, SigningCfg
from sdk.cosmpy.aerial.tx_helpers import SubmittedTx
from sdk.cosmpy.aerial.wallet import LocalWallet


def submit_tx(
        client: LedgerClient,
        wallet: LocalWallet,
        tx: Transaction,
        gas_limit: int
) -> SubmittedTx:
    submitted_tx = prepare_and_broadcast_basic_transaction(
        client=client,
        tx=tx,
        sender=wallet,
        gas_limit=gas_limit
    )

    return submitted_tx


def seal_tx(
        tx: Transaction,
        wallet: LocalWallet,
        client: LedgerClient,
        fee: str = "",
        gas_limit: int = 0
) -> Transaction:
    account = client.query_account(wallet.address())
    tx.seal(
        SigningCfg.direct(wallet.public_key(), account.sequence),
        fee=fee,
        gas_limit=gas_limit,
    )
    tx.sign(wallet.signer(), client.network_config.chain_id, account.number)
    tx.complete()
    return tx


def sign_and_complete_tx(tx: Transaction, wallet: LocalWallet, client: LedgerClient) -> Transaction:
    free_tx = seal_tx(tx, wallet, client)
    gas_limit, fee = client.estimate_gas_and_fee_for_tx(free_tx)
    return seal_tx(tx, wallet, client, fee=fee, gas_limit=gas_limit)


def generate_vote_tx(
        client: LedgerClient,
        wallet: LocalWallet,
        proposal_contract: LedgerContract,
        proposal_id: int,
        vote: str | int
) -> Transaction:
    if isinstance(vote, str):
        args = {
            "vote": {
                "proposal_id": proposal_id,
                "vote": vote
            }
        }
    else:
        args = {
            "vote": {
                "proposal_id": proposal_id,
                "vote": {
                    "option_id": vote
                }
            }
        }
    tx = Transaction()
    tx.add_message(
        create_cosmwasm_execute_msg(
            sender_address=wallet.address(),
            contract_address=proposal_contract.address,
            args=args,
            funds=None
        )
    )
    return sign_and_complete_tx(tx, wallet, client)


def simulate_tx(client: LedgerClient, tx_generation_func, *args, **kwargs) -> SimulateTxResponse:
    try:
        tx = tx_generation_func(client=client, *args, **kwargs)
        estimated_gas = client.simulate_tx(tx=tx)
        return SimulateTxResponse(
            estimated_gas=estimated_gas,
            generated_tx=tx,
            exception=None
        )
    except Exception as e:
        if 'no voting power' in str(e):
            exception_detail = 'no voting power'
        else:
            exception_detail = (
                e.args[0].details if e.args and hasattr(e.args[0], "details") else
                (e.args[0] if e.args else str(e))
            )
        return SimulateTxResponse(
            estimated_gas=0,
            generated_tx=Transaction(),
            exception=exception_detail
        )


def simulate_vote_tx(
        client: LedgerClient,
        wallet: LocalWallet,
        proposal_contract: LedgerContract,
        proposal_id: int,
        vote: str
) -> SimulateTxResponse:
    return simulate_tx(
        client,
        generate_vote_tx,
        wallet=wallet,
        proposal_contract=proposal_contract,
        proposal_id=proposal_id,
        vote=vote
    )
