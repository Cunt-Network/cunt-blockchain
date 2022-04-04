import Big from 'big.js';
import Unit from '../constants/Unit';
import cuntFormatter from './cuntFormatter';

export default function catToMojo(cat: string | number | Big): number {
  return cuntFormatter(cat, Unit.CAT)
    .to(Unit.MOJO)
    .toNumber();
}