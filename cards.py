import copy
import random
import warnings

ranks = [0,'A','2','3','4','5','6','7','8','9','10','J','Q','K']
rank_names = {'0':'Joker','A':'Ace','2':'Two','3':'Three',
	'4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight',
	'9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

suits = ['C','D','H','S']
suit_names = {'C':'Clubs','D':'Diamonds',
	'H':'Hearts','S':'Spades'}

class Card(object):
	rank = '0'
	suit = '0'
	value = 0
	def __init__(self, v, s):
		if s not in suits:
			raise TypeError("Invalid Suit")
		if v not in ranks:
			if type(v) == type(1) and v <=13:
				v = ranks[v]
			else:
				raise TypeError("Invalid Rank")
		
		self.rank = v
		self.suit = s
	def __repr__(self):
		if self.rank == '0' and self.suit == '0':
			return '<Joker>'
		else:
			return '<'+rank_names[self.rank] + ' of ' + suit_names[self.suit] + '>'
			#return '<'+self.rank + self.suit+'>'
	def value(self):
		return ranks.index(self.rank)
	def __cmp__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return cmp(t1,t2)

class Deck(object):
	def __init__(self, numDecks=1, jflag=0):
		self.cards = [Card(v,s) for v in ranks[1:] for s in suits for deck in range(numDecks)]
		self.numDecks = numDecks
		self.jflag = jflag
		if jflag:
			 self.cards += [Card('0','0') for j in jflag]
		self.orig_cards=copy.deepcopy(self.cards)
		random.shuffle(self.cards)
	def draw(self, n = 1):
		card = []
		for _ in range(n):
			if self.deckSize():
				card.append(self.cards.pop())
			else:
				raise IndexError("Deck Empty!")
		if n==1:
			return card[0]
		else:
			return card
	def deckSize(self):
		return len(self.cards)
	def reshuffle(self):
		self.cards = copy.deepcopy(self.orig_cards)
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
		if cards > self.deckSize():
			raise IndexError("Not Enough Cards!")
		if cards % n != 0:
			warnings.warn("Warning: The cards will not be distributed evenly.")
		dealt=[]
		for _ in range(n):
			dealt.append([])
		
		ctr=0
		while(self.deckSize()):
			dealt[ctr%n].append(self.draw())
			ctr+=1
		return dealt
	def __len__(self):
		return self.deckSize()
	def __getitem__(self,key):
		return self.cards[key]
	def __iter__(self):
		while self.deckSize():
			yield self.cards.pop()
		raise StopIteration
	def __repr__(self):
		return "<{} {} with {} {} remaining>".format(self.numDecks, \
			"deck" if self.numDecks == 1 else "decks", \
			self.deckSize(), \
			"card" if self.deckSize() == 1 else "cards")
