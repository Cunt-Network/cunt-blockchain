import Big from 'big.js';
import Unit from '../constants/Unit';
import cuntFormatter from './cuntFormatter';

export default function mojoToCunt(mojo: string | number | Big): number {
  return cuntFormatter(mojo, Unit.MOJO)
    .to(Unit.CUNT)
    .toNumber();
}