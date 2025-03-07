from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class VoteChoice(BaseModel):
    option_id: int


class VoteResponse(BaseModel):
    voter: Optional[str]
    vote: Optional[Union[str, VoteChoice]]
    power: Optional[str]
    rationale: Optional[str]
    votedAt: Optional[datetime]
