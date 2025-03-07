from datetime import datetime
from typing import List, Optional, Any, Dict

from pydantic import BaseModel


class Execute(BaseModel):
    msg: str
    funds: List[Any]
    contract_addr: str


class Wasm(BaseModel):
    execute: Execute


class Msg(BaseModel):
    wasm: Wasm


class TimelockDuration(BaseModel):
    time: int


class Veto(BaseModel):
    vetoer: str
    early_execute: bool
    timelock_duration: TimelockDuration
    veto_before_passed: bool


class Choice(BaseModel):
    msgs: List[Msg] = []  # может быть пустым
    index: int
    title: str
    vote_count: str
    description: str
    option_type: str


class Proposal(BaseModel):
    msgs: Optional[List[Msg]] = []
    choices: Optional[List[Choice]] = None
    veto: Optional[Veto] = None
    title: str
    votes: dict
    status: str
    proposer: str
    threshold: Optional[Any] = None
    expiration: Dict[str, str]
    description: str
    total_power: str
    start_height: int
    allow_revoting: bool
    min_voting_period: Optional[Any]
    voting_strategy: Optional[Dict[str, Any]] = None


class ProposalModuleInfo(BaseModel):
    version: str
    contract: str


class ProposalModule(BaseModel):
    prefix: str
    status: str
    address: str
    info: ProposalModuleInfo


class ProposalInfoResponse(BaseModel):
    id: int
    proposal: Proposal
    createdAt: datetime
    proposalModule: ProposalModule
    daoProposalId: str
    dao: str
    hideFromSearch: bool
