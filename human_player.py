from player import Player, DealBetsSignal


class HumanPlayer(Player):
    ai = False

    def on_bet(self, current_bet: int, betting_rounds: int) -> DealBetsSignal:
        sec = ['Call', 'Die']

        if self.chip_count <= current_bet - self.suggested_bet and \
                self.suggested_bet > 0 or \
                self.suggested_bet <= 0 and \
                self.chip_count <= current_bet:
            sec[0] = 'All in'
        else:
            if current_bet == 0:
                sec[0] = 'Check'
            if (
                    self.chip_count >= current_bet - self.suggested_bet + betting_rounds and
                    self.suggested_bet > 0 or
                    self.chip_count >= current_bet + betting_rounds
                    and self.suggested_bet <= 0):
                sec.append('Raise')
        print(sec, 'Your chips %d,' % self.chip_count, 'Now deal:', current_bet)
        print(self.hand)
        user_selected_answer = sec[int(input('select>')) - 1]
        if user_selected_answer == 'All in':
            return DealBetsSignal.AllIn
        elif user_selected_answer == 'Call' or user_selected_answer == 'Check':
            return DealBetsSignal.Call
        elif user_selected_answer == 'Raise':
            return DealBetsSignal.Raise
        else:
            return DealBetsSignal.Die
