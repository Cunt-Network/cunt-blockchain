const cunt = require('../../util/cunt');

describe('cunt', () => {
  it('converts number byte to cunt', () => {
    const result = cunt.byte_to_cunt(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string byte to cunt', () => {
    const result = cunt.byte_to_cunt('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number byte to cunt string', () => {
    const result = cunt.byte_to_cunt_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string byte to cunt string', () => {
    const result = cunt.byte_to_cunt_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number cunt to byte', () => {
    const result = cunt.cunt_to_byte(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string cunt to byte', () => {
    const result = cunt.cunt_to_byte('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number byte to colouredcoin', () => {
    const result = cunt.byte_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string byte to colouredcoin', () => {
    const result = cunt.byte_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number byte to colouredcoin string', () => {
    const result = cunt.byte_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string byte to colouredcoin string', () => {
    const result = cunt.byte_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to byte', () => {
    const result = cunt.colouredcoin_to_byte(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to byte', () => {
    const result = cunt.colouredcoin_to_byte('1000');

    expect(result).toBe(1000000);
  });
});
