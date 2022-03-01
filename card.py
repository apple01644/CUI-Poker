class Card:
    def __init__(self, suit: str, rank: int):
        self.suit = suit
        self.rank = rank

    def number_to_letter(self):
        if self.rank == 1:
            return 'A'
        elif self.rank == 10:
            return 'T'
        elif self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        else:
            return str(self.rank)

    def __repr__(self):
        return self.suit + self.number_to_letter()
