from dataclasses import dataclass
from random import shuffle, randint
from time import sleep
from typing import List, Iterable

from card import Card
from human_player import HumanPlayer
from player import Player, DealBetsSignal
from robot_player import RobotPlayer
from valuation import valuing, v2w


@dataclass
class PlayerPreset:
    name: str
    is_ai: bool


class Game:
    players_presets: List[PlayerPreset] = [
        PlayerPreset(name='Alpha', is_ai=False),
        PlayerPreset(name='Beta', is_ai=True),
        PlayerPreset(name='Gamma', is_ai=True),
        PlayerPreset(name='Sigma', is_ai=True),
        PlayerPreset(name='Xi', is_ai=True),
    ]

    def __init__(self):
        self.deck: List[Card] = []
        self.players: List[Player] = []
        for player_preset in self.players_presets:
            if player_preset.is_ai:
                player = RobotPlayer(name=player_preset.name)
            else:
                player = HumanPlayer(name=player_preset.name)
            self.players.append(player)

    def deal_bets(self, forced_bet: int = None) -> int:
        print('---===---round table---===---')
        bet = forced_bet or 0
        betting_rounds = 1
        gathered_bets = 0

        for player in self.live_players():
            player.suggested_bet = 0

        while True:
            bet_changed = False
            for player in self.live_players():
                if player.chip_count == 0:
                    continue
                if bet == player.suggested_bet and betting_rounds > 1:
                    break
                deal_bets_signal = player.on_bet(current_bet=bet, betting_rounds=betting_rounds)

                print('%6s' % player.name, end=': ')
                if player.ai:
                    sleep(0.5)
                if deal_bets_signal == DealBetsSignal.Call:
                    if bet == 0:
                        print('ⓒheck')
                        player.suggested_bet = 0
                    else:
                        print('ⓒall', bet)
                        if player.suggested_bet < 0:
                            player.suggested_bet = 0
                        gathered_bets += bet - player.suggested_bet
                        player.chip_count -= bet - player.suggested_bet
                        player.suggested_bet = bet
                elif deal_bets_signal == DealBetsSignal.Raise:
                    print('ⓡaise to', bet + betting_rounds)
                    bet += betting_rounds
                    bet_changed = True
                    if player.suggested_bet < 0:
                        player.suggested_bet = 0
                    gathered_bets += bet - player.suggested_bet
                    player.chip_count -= bet - player.suggested_bet
                    player.suggested_bet = bet
                elif deal_bets_signal == DealBetsSignal.Die:
                    print('ⓓie')
                    player.is_live = False
                else:
                    print('ⓐll in')
                    gathered_bets += player.chip_count
                    player.chip_count = 0

                if player.ai:
                    sleep(1)
            if bet_changed:
                betting_rounds += 1
            else:
                break
        return gathered_bets

    def take_a_card(self) -> Card:
        return self.deck.pop(0)

    def admin_print(self, *args):
        pass

    def take_new_deck(self):
        deck: List[Card] = []
        for m in ['♥', '◆', '♠', '♣']:
            for n in range(1, 14):
                deck.append(Card(m, n))
        shuffle(deck)
        self.deck = deck

    def live_players(self) -> Iterable[Player]:
        return filter(lambda player: player.is_live, self.players)

    def kicking_players(self):
        for player in self.players:
            if player.chip_count == 0:
                player.is_live = False
            else:
                player.is_live = True

    def prepare_player(self):
        for player in self.live_players():
            player.hand.clear()
            player.showed_card.clear()

    def show_down(self, money_in_pot):
        o = {'p': -1, 'i': -1}
        i = 0
        for player in self.players:
            if len(player.hand) > 0:
                value_of_hand = valuing(player.hand)
                if value_of_hand > o['p'] and player.is_live:
                    o['p'] = value_of_hand
                    o['i'] = i
                i += 1
        i = 0
        for player in self.players:
            if len(player.hand) > 0:
                value_of_hand = valuing(player.hand)
                sleep(2)
                if player.ai:
                    if i == o['i']:
                        print('%-9s' % player.name, player.hand, v2w(value_of_hand), '☆', player.chip_count, '+', money_in_pot)
                    else:
                        if player.is_live:
                            print('%-9s' % player.name, player.hand, v2w(value_of_hand), player.chip_count)
                        else:
                            print('%-9s' % player.name, player.hand, 'died', player.chip_count)
                else:
                    if i == o['i']:
                        print('%-9s' % player.name, player.hand, v2w(value_of_hand), 'you', '☆', player.chip_count, '+',
                              money_in_pot)
                    else:
                        if player.is_live:
                            print('%-9s' % player.name, player.hand, v2w(value_of_hand), 'you', player.chip_count)
                        else:
                            print('%-9s' % player.name, player.hand, 'died you', player.chip_count)
                if i == o['i']:
                    player.chip_count += money_in_pot
                i += 1

    def main(self):
        # init user

        while len(list(self.live_players())) > 0:
            money_in_pot = 0
            self.prepare_player()
            self.take_new_deck()

            print('---===---give four cards---===---')
            for time in range(4):
                for player in self.live_players():
                    card = self.take_a_card()
                    player.hand.append(card)
                    if not player.ai:
                        print('!you get', card)
                    self.admin_print('%-9s' % player.name, player.hand)

            print('---===---throw one hidden card---===---')
            for player in self.live_players():
                if player.ai:
                    pick = randint(0, len(player.hand) - 1)
                else:
                    print('your hand', player.hand)
                    pick = int(input('throw one card>')) - 1
                self.admin_print('throw', player.hand[pick])
                del player.hand[pick]

            print('---===---show a card---===---')
            for player in self.live_players():
                if player.ai:
                    print('%-9s shows ' % player.name, end=': ')
                    sleep(0.5)
                    pick = randint(0, len(player.hand) - 1)
                    print(str(player.hand[pick]))
                    sleep(0.5)
                else:
                    print('your hand', player.hand)
                    pick = int(input('show one card>')) - 1
                self.admin_print('show', player.hand[pick])
                player.show_a_card(player.hand[pick])

            money_in_pot += self.deal_bets(1)

            print('---===---give one cards---===---')
            for player in self.live_players():
                card = self.take_a_card()
                player.show_a_card(card)
                player.hand.append(card)
                if not player.ai:
                    print('!you get', card)
                else:
                    print('%-9s' % player.name, player.showed_card)

            money_in_pot += self.deal_bets()
            i = 0
            print('---===---give two cards---===---')
            for time in range(2):
                for player in self.live_players():
                    card = self.take_a_card()
                    player.show_a_card(card)
                    player.hand.append(card)
                    if not player.ai:
                        print('!you get', card)
                    else:
                        print('%-9s' % player.name, player.showed_card)
                if i == 0:
                    i = 1
                    print('------------------')

            money_in_pot += self.deal_bets()

            print('---===---give one cards---===---')
            for player in self.live_players():
                card = self.take_a_card()
                player.hand.append(card)
                if not player.ai:
                    print('!you get', card)

            money_in_pot += self.deal_bets()

            print('---===---throw two cards---===---')
            for player in self.live_players():
                for time in range(2):
                    if player.ai:
                        pick = randint(0, len(player.hand) - 1)
                    else:
                        print('your hand', player.hand)
                        pick = int(input('throw one card>')) - 1
                    self.admin_print('throw', player.hand[pick])
                    del player.hand[pick]

            print('---===---final act---===---')
            self.show_down(money_in_pot)

            input('---===---end---===---')

            self.kicking_players()


if __name__ == '__main__':
    Game().main()
