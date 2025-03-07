from pydantic import BaseModel


class VotingPowerResponse(BaseModel):
    power: int
