#  File: War.py
#  Description: Homework #3
#  Student's Name: Sarah Teng
#  Student's UT EID: st29653
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: February 20, 2019
#  Date Last Modified: March 1, 2019

#import the python tools needed to shuffle the deck
import itertools, random
from random import shuffle

#define lists for card rank and suit
def RANKS(): return [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14" ]
def SUITS(): return [ "C", "D", "H", "S" ]

#define the Card class
class Card:

    #assign a suit and rank attribute to each Card object that gets created
    def __init__(self,suit,rank):

        self.suit = suit
        self.rank = rank

    #define a string method to be able to print cards
    def __str__(self):

        if self.rank == "11":
            rankDisplay = "J"
        elif self.rank == "12":
            rankDisplay = "Q"
        elif self.rank == "13":
            rankDisplay = "K"
        elif self.rank == "14":
            rankDisplay = "A"
        else:
            rankDisplay = str(self.rank)

        #return an outString 
        outString = str(rankDisplay) + str(self.suit)
        
        #format the outString to be right justified and take up 3 characters
        return outString.rjust(3)

#define the Deck class
class Deck:

    #create a deck of cards using each rank and suit
    #append it to a card deck list
    def __init__(self):

        self.cardList = []
        for suit in SUITS():
            for rank in RANKS():
                card = Card(suit, rank)
                self.cardList.append(card)

    #define a method to shuffle the cards the same way each time
    def shuffle(self):
        random.seed(15)
        random.shuffle(self.cardList)

    #define a method to deal one card to each player 
    def dealOne(self,player):

        topCard = self.cardList.pop(0)
        player.hand.append(topCard)
        player.handTotal += 1

    #define the string method to output a deck of cards
    #format it so that a new row starts every 13 cards
    def __str__(self):
        
        outString = ""
        count = 0

        for i in self.cardList:
            
            cardString = str(i)
            count += 1
            outString += cardString + " "
            if count % 13 == 0:
                outString += "\n"
            
        return outString       

#define the Player class
class Player:

    #each player should have a list of cards in their hand and a total number of cards
    def __init__(self):

        self.hand = []
        self.handTotal = 0

    #define the string method to output a players hand
    #formatted the same way as printing the card deck
    def __str__(self):
        
        outString = ""
        count = 0

        for i in self.hand:
            
            cardString = str(i)
            count += 1
            outString += cardString + " "
            if count % 13 == 0:
                outString += "\n"
            
        return outString
    
#define the playGame method which takes arguments for cardDeck and two players
def playGame(cardDeck,player1,player2):

    #set the round number
    roundNum = 1

    #while any player still has cards in their hand, continue through the loop
    while len(player1.hand) != 0 and len(player2.hand) != 0:

        #create two empty lists to store cards as they're played
        cardPile1 = []
        cardPile2 = []

        print(" ")
        print("\nROUND " + str(roundNum) + ":")

        #flip over the each players top two cards
        topCard1 = player1.hand.pop(0)
        topCard2 = player2.hand.pop(0)

        #print the result
        print("Player 1 plays:",topCard1)
        print("Player 2 plays:",topCard2)

        #if the cards are equal in rank, begin war
        if topCard1.rank == topCard2.rank:
            print("\nWar starts:",topCard1,"=",topCard2)
            cardPile1.append(topCard1)
            cardPile2.append(topCard2)

            #draw three cards alternating between players face down
            #and append them to their respective piles
            for i in range(3):
                card1 = player1.hand.pop(0)
                card2 = player2.hand.pop(0)
                print("Player 1 puts",card1,"face down")
                print("Player 2 puts",card2,"face down")
                cardPile1.append(card1)
                cardPile2.append(card2)

            #draw one more card alternating between players face up
            #and append them to their respective piles
            for i in range(1):
                card1up = player1.hand.pop(0)
                card2up = player2.hand.pop(0)
                print("Player 1 puts",card1up,"face up")
                print("Player 2 puts",card2up,"face up")

            #compare the war card ranks and determine the winner
            #append all card piles to the bottom of the winning players hand
            if int(card1up.rank) > int(card2up.rank):
                print("\nPlayer 1 wins round " + str(roundNum) +": " + str(card1up) + " > " + str(card2up))
                cardPile1.append(card1up)
                cardPile2.append(card2up)
                player1.hand = player1.hand + cardPile1 + cardPile2
                roundNum = roundNum + 1
            else:
                print("\nPlayer 2 wins round " + str(roundNum) + ": " + str(card2up) + " > " + str(card1up))
                cardPile1.append(card1up)
                cardPile2.append(card2up)
                player2.hand = player2.hand + cardPile1 + cardPile2
                roundNum += 1
                
        #if there's no war, determine who gets the two cards
        #append them to the bottom of the winning players hand
        else:
            if int(topCard1.rank) > int(topCard2.rank):
                print("\nPlayer 1 wins round " + str(roundNum) + ": " + str(topCard1) + " > " + str(topCard2))
                cardPile1.append(topCard1)
                cardPile2.append(topCard2)
                player1.hand = player1.hand + cardPile1 + cardPile2
                roundNum += 1
            else:
                print("\nPlayer 2 wins round " + str(roundNum) + ": " + str(topCard2) + " > " + str(topCard1))
                cardPile1.append(topCard1)
                cardPile2.append(topCard2)
                player2.hand = player2.hand + cardPile1 + cardPile2
                roundNum += 1

        #output the number of cards each player has remaining
        #output the cards in each players hand
        print("\nPlayer 1 now has",str(len(player1.hand)),"card(s) in hand:")
        print(player1)

        print("\nPlayer 2 now has",str(len(player2.hand)),"card(s) in hand:")
        print(player2)

#define the handNotEmpty method to see who's the winner
def handNotEmpty(player):

    #if the player's hand is not empty, return true
    if len(player.hand) != 0:
        return True 
    else:
        return False


#define the main method to play the game
def main():
    
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    cardDeck.shuffle()                 # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
   
    player1 = Player()              # create a player
    player2 = Player()              # create another player
    
    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)

    #print each players initial hands
    print("Initial hands:")
    print("Player 1:")
    print(player1)

    print("Player 2:")
    print(player2)

    #play the game!
    playGame(cardDeck,player1,player2)

    #check to see who won
    if handNotEmpty(player1):
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    #print the final hands
    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
        
        
        
    
