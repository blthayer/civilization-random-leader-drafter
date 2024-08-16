#!/usr/bin/python3

"""Randomly choose n_leaders for each player (n_players).
Duplicate leaders are not allowed, and duplicate civilizations
are not allowed.

A vectorized approach (e.g. numpy) is probably more efficient,
but I wanted to do this with only built-ins for portability
and simplicity.
"""

import argparse
import csv
from dataclasses import dataclass
import random


@dataclass
class Leader:
    name: str
    civ: str

    def __repr__(self) -> str:
        return f"{{{self.name}: {self.civ}}}"


def read_leaders() -> list[Leader]:
    with open("leaders.csv", newline='') as csvfile:
        header = csvfile.readline()
        # I normally don't do inline assertions, but...
        # This is a quick script. This is fragile
        # and sorta dumb, oh well.
        assert header.strip() == "Leader, Civilization"
        reader = csv.reader(csvfile, delimiter=',')
        leaders = [Leader(name=x[0].strip(), civ=x[1].strip()) for x in reader]

    return leaders


def main(n_players: int, n_leaders: int):
    # Get leaders, then shuffle in-place.
    leaders = read_leaders()
    random.shuffle(leaders)

    # Prime the loop.
    final_list = []
    leader_set = set()
    civ_set = set()
    idx = 0

    # In theory the "and (idx...)" is not necessary,
    # but who wants to accidentally be stuck in an
    # infinite loop?
    while (len(final_list) < (n_players * n_leaders)) and (idx < len(leaders)):
        _leader = leaders[idx]
        idx += 1

        # Ensure no duplicate leaders or civs.
        if (_leader.name not in leader_set) and (_leader.civ not in civ_set):
            final_list.append(_leader)
            leader_set.add(_leader.name)
            civ_set.add(_leader.civ)

    # Print out the result.
    for n in range(n_players):
        print(f"Player {n+1}: {final_list[n * n_leaders:(n * n_leaders + n_leaders)]}".replace("[", "").replace("]", ""))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n_players", help="Number of players", type=int)
    parser.add_argument("n_leaders", help="Number of leaders each player can choose from", type=int)
    args = parser.parse_args()
    main(n_players=args.n_players, n_leaders=args.n_leaders)
