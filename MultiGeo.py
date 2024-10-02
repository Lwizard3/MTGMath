from math import comb

class Deck:
    def __init__(self, population, count, sample, sucesses, starting_hand):
        self.population = population
        self.count = count
        self.sample = sample
        self.sucesses = sucesses
        self.starting_hand = starting_hand

    def copy(self):
        return Deck(self.population, self.count, self.sample, self.sucesses, self.starting_hand)


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
    Temp.sample = Deck.starting_hand
    mull1 = atleast(Temp)
    mull2 = atleast(Deck)

    return mull1 + mull2 - (mull1 * mull2)

def expected_with_mull(Deck):
    mull1_expected = 0
    mull1_prob = 0
    Temp = Deck.copy()
    Temp.sample = Deck.starting_hand
    for i in range(Deck.sucesses, Temp.sample + 1):
        Temp.sucesses = i
        prob = hypergeo(Temp)
        mull1_prob += prob
        mull1_expected += prob * i

    Temp.sample = Deck.sample
    mull2_expected = 0
    for i in range(Deck.sample + 1):
        Temp.sucesses = i
        mull2_expected += hypergeo(Temp) * i

    return mull1_expected + mull2_expected * (1 - mull1_prob)

    

deck = Deck(99, 36, 12, 5, 7)

print(atleast(deck))
print(below(deck))
print(hypergeo(deck))
print(expected(deck))
print(prob_with_mull(deck))
print(expected_with_mull(deck))
