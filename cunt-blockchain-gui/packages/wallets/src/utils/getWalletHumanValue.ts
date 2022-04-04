import type { Wallet } from '@cunt/api';
import { WalletType } from '@cunt/api';
import { mojoToCATLocaleString, mojoToCuntLocaleString } from '@cunt/core';

export default function getWalletHumanValue(wallet: Wallet, value: number): string {
  return wallet.type === WalletType.CAT
    ? mojoToCATLocaleString(value)
    : mojoToCuntLocaleString(value);
}
