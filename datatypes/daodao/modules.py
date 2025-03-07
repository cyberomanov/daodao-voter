from typing import List, Optional

from pydantic import BaseModel


class ProposalModuleItem(BaseModel):
    prefix: str
    contract: str
    ids: Optional[List[int]]
    type: str
