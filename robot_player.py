from random import randint
from time import sleep

from player import Player, DealBetsSignal
from valuation import valuing


class RobotPlayer(Player):
    ai = True

    def on_bet(self, current_bet: int, betting_rounds: int) -> DealBetsSignal:

        if self.chip_count <= current_bet - self.suggested_bet and \
                self.suggested_bet > 0 or self.suggested_bet <= 0 \
                and self.chip_count <= current_bet:
            if randint(0, 2 + current_bet - self.chip_count) != 0:
                return DealBetsSignal.AllIn
        else:
            v = int(valuing(self.hand))

            if v + randint(0, 4) + randint(0, 4) >= 10 + betting_rounds * 1.5 and (
                    self.chip_count >= current_bet - self.suggested_bet + betting_rounds and
                    self.suggested_bet > 0 or self.chip_count >= current_bet + betting_rounds
                    and self.suggested_bet <= 0
            ):
                return DealBetsSignal.Raise
            elif v + randint(0, 3) + randint(0, 4) >= 3 + betting_rounds * 1.5:
                return DealBetsSignal.Call
        return DealBetsSignal.Die
