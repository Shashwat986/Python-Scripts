import random
values = [0,'A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['C','D','H','S']
joker = ['0','0']

class Card:
	rank = '0'
	suit = '0'
	value = 0
	def __init__(self, v, s):
		self.rank = v
		self.suit = s
	def __repr__(self):
		return self.rank + self.suit
	def value(self):
		
		return values.index(self.rank)

class Deck:
	def __init__(self, numDecks=1, jflag=0):
		self.cards = [(v,s) for v in values[1:] for s in suits]*numDecks
		if jflag:
			 self.cards += joker*jflag
		self.orig_cards=self.cards
		random.shuffle(self.cards)
	def draw(self):
		crd = self.cards.pop()
		card = Card(crd[0],crd[1])
		return card
	def deckSize(self):
		return len(self.cards)
	def reshuffle(self):
		self.cards = self.orig_cards
		random.shuffle(self.cards)
	def shuffle(self):
		random.shuffle(self.cards)
	def cut(self,n=None):
		if n is None:
			n=random.randint(1,len(self.cards))
		self.cards = self.cards[n:]+self.cards[:n]
	def deal(self, n, cards=None):
		if cards is None:
			cards=self.deckSize();
		dealt=[]
		for _ in range(n):
			dealt.append([])
		
		ctr=0
		while(self.deckSize()):
			dealt[ctr%n].append(self.draw())
			ctr+=1
		return deck