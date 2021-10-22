from typing import Dict

import blspy

from cunt.full_node.bundle_tools import simple_solution_generator
from cunt.types.blockchain_format.coin import Coin
from cunt.types.blockchain_format.program import Program
from cunt.types.coin_spend import CoinSpend
from cunt.types.condition_opcodes import ConditionOpcode
from cunt.types.generator_types import BlockGenerator
from cunt.types.spend_bundle import SpendBundle
from cunt.util.ints import uint64
from cunt.wallet.puzzles.p2_delegated_puzzle_or_hidden_puzzle import puzzle_for_pk, solution_for_conditions

GROUP_ORDER = 0x73EDA753299D7D483339D80809A1D80553BDA402FFFE5BFEFFFFFFFF00000001


def int_to_public_key(index: int) -> blspy.G1Element:
    index = index % GROUP_ORDER
    private_key_from_int = blspy.PrivateKey.from_bytes(index.to_bytes(32, "big"))
    return private_key_from_int.get_g1()


def puzzle_hash_for_index(index: int, puzzle_hash_db: dict) -> bytes:
    public_key = bytes(int_to_public_key(index))
    puzzle = puzzle_for_pk(public_key)
    puzzle_hash = puzzle.get_tree_hash()
    puzzle_hash_db[puzzle_hash] = puzzle
    return puzzle_hash


def make_fake_coin(index: int, puzzle_hash_db: dict) -> Coin:
    """
    Make a fake coin with parent id equal to the index (ie. a genesis block coin)

    """
    parent = index.to_bytes(32, "big")
    puzzle_hash = puzzle_hash_for_index(index, puzzle_hash_db)
    amount = 100000
    return Coin(parent, puzzle_hash, uint64(amount))


def conditions_for_payment(coin) -> Program:
    d: Dict = {}  # a throwaway db since we don't care
    new_puzzle_hash = puzzle_hash_for_index(int.from_bytes(coin.puzzle_hash, "big"), d)
    return Program.to([[ConditionOpcode.CREATE_COIN, new_puzzle_hash, coin.amount]])


def make_spend_bundle(count: int) -> SpendBundle:
    puzzle_hash_db: Dict = dict()
    coins = [make_fake_coin(_, puzzle_hash_db) for _ in range(count)]

    coin_spends = []
    for coin in coins:
        puzzle_reveal = puzzle_hash_db[coin.puzzle_hash]
        conditions = conditions_for_payment(coin)
        solution = solution_for_conditions(conditions)
        coin_spend = CoinSpend(coin, puzzle_reveal, solution)
        coin_spends.append(coin_spend)

    spend_bundle = SpendBundle(coin_spends, blspy.G2Element())
    return spend_bundle


def make_block_generator(count: int) -> BlockGenerator:
    spend_bundle = make_spend_bundle(count)
    return simple_solution_generator(spend_bundle)
