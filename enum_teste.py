from enum import Enum

class Corretoras(Enum):
    Binance =   1
    XBINGX  =   2
    BayBit  =   3


print(Corretoras.XBINGX.name)