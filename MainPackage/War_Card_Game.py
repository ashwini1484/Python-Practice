'''
This is a WAR card game simulated between two computer players
'''

## Section for all import of libraries

from random import shuffle #used to shuffle cards randomly


suites = ['Hearts','Diamonds','Spades','Clubs']

ranks  = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Ace','Jack','King','Queen']

##For every card chosen from the deck, a value needs to be assigned for comparison. It is done by the following dictionary
card_values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


class Card:

    '''
    This is a class that simulates cards in a deck.
    The class should be able to identify suite, rank and value of the card
    '''

    def __init__(self,suite,rank):

        self.suite = suite
        self.rank  = rank.title()
        self.value = card_values[rank]

    def __str__(self):

        return self.rank + ' of ' + self.suite


class Deck:

    '''
    This class creates a deck of cards - a deck that actually holds the 52 card combinations resembling the real-world card deck
    '''
    
    def __init__(self):

        self.all_cards = []

        for suite in suites:
            for rank in ranks:

                created_card = Card(suite,rank)

                self.all_cards.append(created_card)


    def RandShuffle(self):

        shuffle(self.all_cards)

    def DealCard(self):

        return self.all_cards.pop()


class Player:

    def __init__(self,name):

        self.name      = name
        self.my_cards  = []

    def __str__(self):
        return f'Player {self.name} has {len(self.my_cards)} cards.'

    def RemoveCard(self):

        return self.my_cards.pop(0)

    def AddCards(self,new_cards):

        if type(new_cards) == type([]):
            self.my_cards.extend(new_cards)
        else:
            self.my_cards.append(new_cards)

if __name__ == '__main__':
    
    ## Create players
    player_one = Player('One')
    player_two = Player('Two')

    #Create a deck of cards and shuffle it
    new_deck = Deck()
    new_deck.RandShuffle()

    #Deal the cards to both players
    for num in range(26):
        player_one.AddCards(new_deck.DealCard())
        player_two.AddCards(new_deck.DealCard())
    
    print(len(player_one.my_cards))
    print(len(player_two.my_cards))

    
    #Check if the game is still on and iterate
    game_on = True
    round_num = 0

    while game_on:

        round_num += 1
        print(f'Round {round_num}')

        #Check if anyone won the game
        if len(player_one.my_cards) == 0:
            print('Player One lost the game. Player Two wins!!')
            game_on = False
            break
        elif len(player_two.my_cards) == 0:
            print('Player Two lost the game. Player One wins!!')
            game_on = False
            break
        else:
            game_on = True

        player_one_cards = []
        player_one_cards.append(player_one.RemoveCard())
        #print(player_one.RemoveCard())

        player_two_cards = []
        player_two_cards.append(player_two.RemoveCard())
        #print(player_two.RemoveCard())

        at_war = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.AddCards(player_one_cards)    
                player_one.AddCards(player_two_cards) 
                at_war = False
                break
            elif player_one_cards[-1].value < player_two_cards[-1].value:   
                player_two.AddCards(player_one_cards)    
                player_two.AddCards(player_two_cards) 
                at_war = False
                break
            else:
                print('Player One at war with player Two!')

                if len(player_one.my_cards) < 10:
                    print('Player One does not have enough cards. Player TWO WINS!!')
                    game_on = False
                    break

                elif len(player_two.my_cards) < 10:
                    print('Player Two does not have enough cards. Player ONE WINS!!')
                    game_on = False
                    break                
                
                else:

                    for num in range(10):
                        player_one_cards.append(player_one.RemoveCard())
                        player_two_cards.append(player_two.RemoveCard())
