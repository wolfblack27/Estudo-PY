from enum import Enum

class Corretoras(Enum):
    Binance =   1
    XBINGX  =   2
    BayBit  =   3


print(f'Valor do enumerador:{Corretoras.XBINGX.value} --- Nome do enumerador: {Corretoras.XBINGX.name}')