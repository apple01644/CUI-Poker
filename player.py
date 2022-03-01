import enum
from random import randint
from typing import List, NoReturn, Optional

from card import Card


class DealBetsSignal(enum.Enum):
    Call = 0
    Raise = 1
    Die = 2
    AllIn = 3


class Player:
    @property
    def ai(self) -> bool:
        raise NotImplementedError()

    def __init__(self, name: str):
        self.name: str = name
        self.chip_count: int = 10 + randint(0, 20)
        self.suggested_bet: int = 0
        self.hand: List[Card] = []
        self.showed_card: List[Card] = []
        self.is_live: bool = True

    def __repr__(self):
        if self.is_live:
            s = 'Live-'
        else:
            s = 'Died-'
        s += str(self.chip_count)

    def show_a_card(self, card: Card) -> NoReturn:
        self.showed_card.append(card)

    def on_bet(self, current_bet: int, betting_rounds: int) -> DealBetsSignal:
        raise NotImplementedError()
