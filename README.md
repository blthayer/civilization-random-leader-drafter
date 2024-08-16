# civilization-random-leader-drafter
Python tool to select a unique random leader pool for multiple players in the Sid Meier’s Civilization® VI video game. Easily adaptable to other games and use cases.

## Quick Start

```console
$ cd ~
$ wget "https://github.com/blthayer/civilization-random-leader-drafter/archive/refs/heads/main.zip"
...
$ unzip main.zip 
...
$ cd civilization-random-leader-drafter-main/
$ python3 civ_drafter.py 2 3
Player 1: {Eleanor of Aquitaine: English}, {Gorgo: Greek}, {Lady Six Sky: Mayan}
Player 2: {Amanitore: Nubian}, {Frederick Barbarossa: German}, {Alexander: Macedonian}
```

## Dependencies

Python 3. "Tested" with 3.10 and 3.11.

## Installation

Simply download `civ_drafter.py` and `leaders.csv` from this repository, and save both
files into the same directory. For the sake of example, we'll assume
the files are saved in `~/civilization-random-leader-drafter`.

## Use

```console
$ cd ~/civilization-random-leader-drafter
$ python3 civ_drafter.py --help
usage: civ_drafter.py [-h] n_players n_leaders

positional arguments:
  n_players   Number of players
  n_leaders   Number of leaders each player can choose from

options:
  -h, --help  show this help message and exit
$ python3 civ_drafter.py 3 4
Player 1: {Kristina: Swedish}, {Tokugawa: Japanese}, {Basil II: Byzantine}, {Gilgamesh: Sumerian}
Player 2: {Victoria (Age of Steam): English}, {Mvemba a Nzinga: Kongolese}, {Eleanor of Aquitaine: French}, {Suleiman (Kanuni): Ottoman}
Player 3: {Peter: Russian}, {Cleopatra (Egyptian): Egpytian}, {Alexander: Macedonian}, {Jadwiga: Polish}
```

## Customization

Simply modify `leaders.csv` to adapt this program to another game (say... Civ VII?)
and run `civ_drafter.py`.
