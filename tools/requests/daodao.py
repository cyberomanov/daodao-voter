import json
from typing import List

import requests

from datatypes.response.proposal_info import ProposalInfoResponse
from datatypes.response.proposal_modules import ProposalModulesResponse
from datatypes.response.reverse_proposals import ReverseProposalsResponse
from datatypes.response.vote import VoteResponse
from datatypes.response.voting_power import VotingPowerResponse


def get_proposal_info(
        session: requests.Session,
        dao_contract: str,
        proposal_id: int,
        proposal_type: str
) -> ProposalInfoResponse:
    url = f"https://indexer.daodao.zone/stargaze-1/contract/{dao_contract}/{proposal_type}/proposal?id={proposal_id}"
    response = session.get(url=url)

    if response.status_code != 200:
        raise Exception(f"get_proposal_info: {response.status_code}")

    return ProposalInfoResponse.parse_obj(response.json())


def get_vote(
        session: requests.Session,
        dao_contract: str,
        proposal_id: int,
        proposal_type: str,
        voter_address: str
) -> VoteResponse:
    url = f"https://indexer.daodao.zone/stargaze-1/contract/" \
          f"{dao_contract}/{proposal_type}/vote?proposalId={proposal_id}&voter={voter_address}"
    response = session.get(url=url)

    if response.status_code == 204:
        return VoteResponse()
    elif response.status_code != 200:
        raise Exception(f"get_vote: {response.status_code}")

    return VoteResponse.parse_obj(response.json())


def get_voting_power(
        session: requests.Session,
        dao_contract: str,
        voter_address: str,
        height: int
) -> VotingPowerResponse:
    url = f"https://indexer.daodao.zone/stargaze-1/contract/" \
          f"{dao_contract}/daoCore/votingPowerAtHeight?address={voter_address}&height={height}"
    response = session.get(url=url)

    if response.status_code != 200:
        raise Exception(f"get_voting_power: {response.status_code}")

    return VotingPowerResponse.parse_obj(response.json())


def get_proposal_modules(session: requests.Session, dao_contract: str) -> [ProposalModulesResponse]:
    url = f"https://indexer.daodao.zone/stargaze-1/contract/{dao_contract}/daoCore/activeProposalModules?"
    response = session.get(url=url)

    if response.status_code != 200:
        raise Exception(f"get_proposal_modules: {response.status_code}")

    return [ProposalModulesResponse.parse_obj(item) for item in json.loads(response.content)]


def get_reverse_proposals(
        session: requests.Session,
        proposal_contract: str,
        proposal_type: str
) -> List[ReverseProposalsResponse]:
    url = f"https://indexer.daodao.zone/stargaze-1/contract/" \
          f"{proposal_contract}/{proposal_type}/reverseProposals?limit=100"
    response = session.get(url=url)

    if response.status_code != 200:
        raise Exception(f"get_reverse_proposals: {response.status_code}")

    return [ReverseProposalsResponse.parse_obj(item) for item in json.loads(response.content)]
