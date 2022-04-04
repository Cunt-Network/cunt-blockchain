import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useCurrencyCode, mojoToCuntLocaleString, CardSimple } from '@cunt/core';
import { useGetFarmedAmountQuery } from '@cunt/api-react';

export default function FarmCardTotalCuntFarmed() {
  const currencyCode = useCurrencyCode();
  const { data, isLoading, error } = useGetFarmedAmountQuery();

  const farmedAmount = data?.farmedAmount;

  const totalCuntFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      return (
        <>
          {mojoToCuntLocaleString(farmedAmount)}
          &nbsp;
          {currencyCode}
        </>
      );
    }
  }, [farmedAmount]);

  return (
    <CardSimple
      title={<Trans>Total Cunt Farmed</Trans>}
      value={totalCuntFarmed}
      loading={isLoading}
      error={error}
    />
  );
}
