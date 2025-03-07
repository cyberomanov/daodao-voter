from datatypes.web3.balance import Balance
from sdk.cosmpy.aerial.client import LedgerClient
from sdk.cosmpy.crypto.address import Address


def get_balance(client: LedgerClient, address: str, denom: str, denomination: int = 10 ** 6):
    balance = client.query_bank_balance(address=Address(address), denom=denom)
    return Balance(
        int=balance,
        float=round(balance / denomination, 4)
    )
