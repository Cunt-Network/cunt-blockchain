import Big from 'big.js';
import Unit from '../constants/Unit';
import cuntFormatter from './cuntFormatter';

export default function mojoToCATLocaleString(mojo: string | number | Big) {
  return cuntFormatter(Number(mojo), Unit.MOJO)
    .to(Unit.CAT)
    .toLocaleString();
}