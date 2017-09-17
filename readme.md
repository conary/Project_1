## Write in plain english, what will you do to test everything mentioned in the description

1)) ** The class Deck's constructor does not accept input, and you can assume this will always be handled correctly by a programmer using this code.

---How to test? - Does Deck(1) raise and expection (aka error)

2)) * The Deck constructor builds a list of cards -- all the cards that would be included in a 52-card deck: rank 1-13 of each of the four suits.
* The Deck constructor creates one instance variable: self.cards, **which should hold a list of Card objects when a Deck instance is created.**

--How to test? -
1) if self.cards is a list
2) if self.cards has instances/objects of Card class, for ex: self.cards[0] should be an object of class Card. To test this, self.assertIsInstance(self.card[0], Card)
#selfassertIstance(object, Class)
Run a for loop to test for all elements of list for class Card (use for loop)
#self.cards = [card1, card2, card3, etc..]
    for card_object in self.cards:
        self.assertIsInstance(card_object, Card)
3) Check length of self.cards

3)) * The Deck string method should return a **multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.**

--How to test? -
1) Does it print 52 lines?
    str(deck) #will give list
    'Ace of Diamonds'\n
    2 of Diamonds
    ..'
    - d_string = str(deck)
      d_list = d_string.split('\n')
      len(d_list) == 52

4)) * Deck has a method pop_card which accepts an integer as input and has a default value such that the Deck will pop off the last (top) card of the deck, as if you're taking off the top card in a card game. When pop_card is invoked on a Deck instance, the last card in the deck is removed from the deck. You should be able to "pop" all of the cards off of the deck until the deck is empty (its self.cards list is the empty list).
- if keep removing items from list and no more to remove should raise Index error
- deck.pop_card() #after 52 times will raise error, how to test for this?
- self.assertRaises(IndexError, deck.pop_card)
#self.assertRaises(exceptionname)