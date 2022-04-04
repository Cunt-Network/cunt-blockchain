import Big from 'big.js';
import Unit from '../constants/Unit';
import cuntFormatter from './cuntFormatter';

export default function cuntToMojo(cunt: string | number | Big): number {
  return cuntFormatter(cunt, Unit.CUNT)
    .to(Unit.MOJO)
    .toNumber();
}