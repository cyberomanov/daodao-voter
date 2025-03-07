from pydantic import BaseModel


class ProposalModuleInfo(BaseModel):
    version: str
    contract: str


class ProposalModulesResponse(BaseModel):
    prefix: str
    status: str
    address: str
    info: ProposalModuleInfo
