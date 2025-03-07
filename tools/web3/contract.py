from sdk.cosmpy.aerial.client import LedgerClient
from sdk.cosmpy.aerial.contract import LedgerContract
from sdk.cosmpy.crypto.address import Address


def get_contract_by_address(address: str, client: LedgerClient) -> LedgerContract:
    return LedgerContract(path=None, address=Address(address), client=client)
