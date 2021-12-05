const cunt = require('../../util/cunt');

describe('cunt', () => {
  it('converts number mojo to cunt', () => {
    const result = cunt.mojo_to_cunt(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to cunt', () => {
    const result = cunt.mojo_to_cunt('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to cunt string', () => {
    const result = cunt.mojo_to_cunt_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to cunt string', () => {
    const result = cunt.mojo_to_cunt_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number cunt to mojo', () => {
    const result = cunt.cunt_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string cunt to mojo', () => {
    const result = cunt.cunt_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = cunt.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = cunt.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = cunt.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = cunt.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = cunt.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = cunt.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
