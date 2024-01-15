from math import comb

class Deck:
    def __init__(self, population, count, sample, sucesses):
        self.population = population
        self.count = count
        self.sample = sample
        self.sucesses = sucesses

    def copy(self):
        return Deck(self.population, self.count, self.sample, self.sucesses)


def hypergeo(Deck):
    return comb(Deck.count, Deck.sucesses) * comb(Deck.population - Deck.count, Deck.sample - Deck.sucesses) / comb(Deck.population, Deck.sample)



def atleast(Deck):
    Temp = Deck.copy()
    prop = 0
    for i in range(Deck.sucesses, Deck.sample + 1):
        Temp.sucesses = i
        prop += hypergeo(Temp)
    return prop

def below(Deck):
    Temp = Deck.copy()
    prop = 0
    for i in range(0, Deck.sucesses):
        Temp.sucesses = i
        prop += hypergeo(Temp)
    return prop

def expected(Deck):
    Temp = Deck.copy()
    expected = 0
    for i in range(0, Deck.sample + 1):
        Temp.sucesses = i
        expected += hypergeo(Temp) * i
    return expected

def prob_with_mull(Deck):
    Temp = Deck.copy()
    Temp.sample = 7
    mull1 = atleast(Temp)
    mull2 = atleast(Deck)

    return mull1 + mull2 - (mull1 * mull2)

deck = Deck(99, 99, 9, 3)

print(atleast(deck))
print(below(deck))
print(hypergeo(deck))
print(expected(deck))
print(prob_with_mull(deck))
