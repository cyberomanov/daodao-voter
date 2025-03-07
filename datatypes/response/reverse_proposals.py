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


class Quorum(BaseModel):
    percent: str


class ThresholdDetail(BaseModel):
    majority: Dict[str, Any]


class ThresholdQuorum(BaseModel):
    quorum: Quorum
    threshold: ThresholdDetail


class Threshold(BaseModel):
    threshold_quorum: ThresholdQuorum


class Expiration(BaseModel):
    at_time: str


class Proposal(BaseModel):
    msgs: Optional[List[Msg]] = []
    veto: Optional[Veto] = None
    title: str
    votes: Dict[str, Any]
    status: str
    proposer: str
    threshold: Optional[Threshold] = None
    expiration: Expiration
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


class ReverseProposalsResponse(BaseModel):
    id: int
    proposal: Proposal
    createdAt: datetime
    completedAt: Optional[datetime] = None
    executedAt: Optional[datetime] = None
