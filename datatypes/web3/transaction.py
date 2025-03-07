from typing import Optional

from pydantic import BaseModel

from sdk.cosmpy.aerial.tx import Transaction


class SimulateTxResponse(BaseModel):
    estimated_gas: int
    generated_tx: Optional[Transaction]
    exception: str | None

    class Config:
        arbitrary_types_allowed = True


class SimulateListTxResponse(SimulateTxResponse, BaseModel):
    list_type: Optional[str]
    contract_version: Optional[int]
