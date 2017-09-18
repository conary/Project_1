## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
# 0. The class Deck's constructor does not accept input,
#check what happens if deck(3) raises an error
class TestDeck(unittest.TestCase):
    def test_init(self):
        d = Deck()

#1. Check to see if the class Card has 3 class variables suit_names,
#rank_levels, and faces
    def test_card_class_variables(self):
        f = Card(0, 12)
        s = f.suit_names
        r = f.rank_levels
        f = f.faces
        self.assertTrue(type(s)) == type([
            'Diamonds', 'Clubs', 'Hearts', 'Spades'
            ])
        self.assertTrue(type(r)) == type([
            1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12, 13
            ])
        self.assertTrue(type(f)) == type({
            1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'
            })

#2. Test to see if the card constructor assigns the correct instance variables
    def test_card_constructor(self):    
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for rank in ranks:
            f = Card(0, rank)
            self.assertTrue(type(f.rank_num) == int)
            if rank == 1:
                self.assertTrue(f.rank == 'Ace')
            if rank > 1:
                if rank < 11:
                    self.assertTrue(type(f.rank) == int)
                else:
                    if rank == 11:
                        self.assertTrue(f.rank =='Jack')
                if rank == 12:
                    self.assertTrue(f.rank =='Queen')
                if rank == 13:
                    self.assertTrue(f.rank =='King')

#3. Test to see if the Card class has a string method,
#and test if string is correct with input 5 (5 of Diamonds)
    def test_card_string_method(self):
        f = Card(0, 5)
        #print(f.__str__())
        self.assertTrue(f.__str__() == '5 of Diamonds')

#4. Test to see if self.cards is of type list     
    def test_cards_list(self):
        g = Deck()
        s = g.cards
        self.assertTrue(type(s) == list)

#5. Test to see if the deck's string method returns a 52-line string 
    def test_deck_amount_cards(self):
        f = Card(0, 12)
        g = Deck()
        t = g.__str__()
        self.assertEqual(len(t.split('\n')), 52)

#6. Test to see if pop_card() method is able to pop all 52 cards off of a fresh deck
    def test_pop_card(self):
        g = Deck()
        c = 0
        for i in g.cards:
            g.pop_card()
            c = c + 1
        self.assertTrue(c == 52)

#7. Test to see if shuffle and sort functions work
    def test_deck_shuffle_and_sort_functions(self):
        g = Deck()
        b = g.__str__() 
        g.shuffle()
        a = g.__str__()
        self.assertTrue(b != a)
        g.sort_cards()
        s = g.__str__()
        self.assertTrue(s == b)

#8. Test to see if replace_card function works
    def test_deck_replace_function(self):
        g = Deck()
        original = g.__str__()
        s = g.pop_card()
        removed = g.__str__()
        self.assertTrue(original != removed)
        g.replace_card(s)
        replaced = g.__str__()
        self.assertTrue(original == replaced) 
        g.replace_card(s)
        replaced_again = g.__str__()
        self.assertTrue(replaced_again == original)

#9. Test to see if deal function works with edge case big hand
    def test_deck_deal_function(self):
        g = Deck()
        c = g.deal_hand(52)
        self.assertTrue(len(c) == 52)

#10. Test to see if self.cards has instances/objects of Card class
    def test_self_cards(self):
        g = Deck()
        for card_obj in g.cards:
            self.assertIsInstance(card_obj, Card)

#11. Test to see if War Game returns tuple of the correct types
    def test_play_war_game(self):
        w = play_war_game(testing=True)
        self.assertIsInstance(w, tuple)
        self.assertTrue(type(w[0]) == type('Tie'))
        self.assertTrue(type(w[1]) == type(24))
        self.assertTrue(type(w[2]) == type(24))

#12. Test to see if show_song returns the same value for the same search paramter
    def test_show_song(self):
        iteration_one = show_song('all you need is love')
        iteration_two = show_song('all you need is love')
        self.assertTrue(iteration_one == iteration_two)

if __name__=='__main__':
    unittest.main(verbosity=2)
