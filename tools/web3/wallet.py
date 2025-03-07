from sdk.cosmpy.aerial.wallet import LocalWallet


def get_wallet_from_mnemonic(mnemonic: str, prefix: str) -> LocalWallet:
    return LocalWallet.from_mnemonic(mnemonic=mnemonic, prefix=prefix)
