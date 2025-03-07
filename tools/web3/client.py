from sdk.cosmpy.aerial.client import LedgerClient
from sdk.cosmpy.aerial.config import NetworkConfig
from sdk.cosmpy.aerial.gas import SimulationGasStrategy


def get_client(
        chain_id: str,
        grpc: str,
        fee_gas_price: float,
        fee_denom: str,
        staking_denom: str,
        multiplier: float
) -> LedgerClient:
    client = LedgerClient(
        cfg=NetworkConfig(
            chain_id=chain_id,
            url=f"grpc+{grpc}",
            fee_minimum_gas_price=fee_gas_price,
            fee_denomination=fee_denom,
            staking_denomination=staking_denom,
        )
    )
    client.gas_strategy = SimulationGasStrategy(client=client, multiplier=multiplier)
    return client
