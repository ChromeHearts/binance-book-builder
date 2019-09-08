from enum import Enum


class Side(Enum):
    BID = 0
    ASK = 1


class Level:
    def __init__(self, side: Side):
        self._side = side

        self._price_level = dict()  # price => qty

        if self._side == Side.BID:
            self._best_op = max
        elif self._side == Side.ASK:
            self._best_op = min
        else:
            raise Exception("Unknown side: {}".format(side))

    def update_level(self, price: str, qty: str):

        if abs(float(qty)) <= 0.0000001:
            if price in self._price_level:
                self._price_level.pop(price)
        else:
            self._price_level[price] = qty

    def best(self):
        bprc = self._best_op(self._price_level.keys())
        return bprc, self._price_level[bprc]


class Book:
    def __init__(self, ticker):
        self._ticker = ticker
        self._levels = (Level(Side.BID), Level(Side.ASK))

    def bbo(self):
        return self._levels[0].best(), self._levels[1].best()

    def update_level(self, side: Side, price: str, qty: str):
        self._levels[side.value].update_level(price, qty)
