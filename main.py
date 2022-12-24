"""
    Python Blackjack
For this project you will make a Blackjack game using Python. Click here to familiarize yourself with the the rules of 
the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version 
of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

Rules:
1. The game will have two players: the Dealer and the Player. 
The game will start off with a deck of 52 cards. 
The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. 
For each suit, there will be cards numbered 1 through 13.



Note: No wildcards will be used in the program
2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, 
it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own 
cards, but should only be able to see one of the Dealer's cards.
3. The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with 
the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player 
can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total 
more than 21.
4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as Blackjack. 
Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on 
the first deal.
5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the 
dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. 
Whoever has the higher number wins. Keep in mind that the Dealer can also bust.


This will be an exercise of how well you understand OOP(Object Oriented Programming). In this project, you will be using 
"Pair-Programming" to complete the assignment.
"""

from random import randint

class blackJack():
    def __init__(self):
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.deck = []
        for s in range(4):
            for num in range(1, 14):
                self.deck.append(f"{num} of {suit[s]}")
        self.dealt = {}
        self.p_hand = []
        self.d_hand = []

    # ***Process Breakdown***
    # Press any key to start, Q to quit
    def menu(self):
        """
        Starts the game
        """
        print("""Welcome to 'Lets Play Some Blackjack!
                 Press any key to play!
                 Press 'q' to quit!""")
        ui = input("> ")

        if ui.lower() == 'q':
            quit()
        else:
            self.game()

    def game(self):
        """
        Initiates game and contains all the options for the player to make
        """
        # Player is dealt a card        
        self.deal(self.p_hand)
        # Dealer is dealt a card
        self.deal(self.d_hand)
        # repeat so 4 cards are dealt
        self.deal(self.p_hand)
        self.deal(self.d_hand)

        while True:
            print(f"\n\nYour hand: {self.total(self.p_hand)}")
            for item in self.p_hand:
                print(f"{item}")

            # Player can see the first card Dealer is dealt
            print("\n\nDealer's hand:")
            print(f"{self.d_hand[0]}")
            print("■■■■■■■■\n")

            # If the 1st 2 cards in Players hand == 21 then Player wins
            # If the cards in Player hand > 21 then Player loses
            card_check = self.card_check(self.p_hand)
            if card_check == 'busted':
                print("You're busted! Better luck next time!")
                quit()
            elif card_check == 'blackjack':
                print("You got exactly 21! nice job!")
                quit()


            action = input("""
                        [H] hit
                        [S] stand
                        [Q] quit

                        >>> """)

            # Player chooses to Hit or Stand
            try:
                action.lower()[0]
            except:
                continue
            if action.lower()[0] == 'h':
                self.deal(self.p_hand)
            elif action.lower()[0] == 's':
                # Once Player chooses Stand both hands are shown to Player with totals.
                self.noMoreCards()
            elif action.lower()[0] == 'q':
                print("So long.")
                quit()
            else:
                continue
            
    def deal(self, hand):
        """
        Pull a random card from the deck and give it to the corresponding hand.
        Remove that card from the deck.
        """
        card = randint(0, len(self.deck)-1)
        hand.append(self.deck[card])
        self.deck.remove(hand[-1])

    def total(self, hand):
        """
        Returns the total of all face value cards in a hand
        """
        total = 0
        for item in hand:
            total += int(item.split()[0])
        return total

    def card_check(self, hand):
        """
        If the 1st 2 cards in Players hand == 21 then Player wins
        If the cards in Player hand > 21 then Player loses
        """
        if self.total(hand) > 21:
            return "busted"
        elif self.total(hand) == 21:
            return "blackjack"
        else:
            return self.total(hand)

    def noMoreCards(self):
        """
        Once the player has chosen to 'stand' this function calculates the winner
        """
        player = self.card_check(self.p_hand)
        dealer = self.card_check(self.d_hand)
        
        #* TEST CODE
        print(f"Player: {player}")
        print(f"Dealer: {dealer}")

        if type(player) == int() and type(dealer) == int():
            print(f"Player: {player}")
            print(f"Dealer: {dealer}")

        # Winner is declared.
        if player == 'blackjack':
            print("You got 21! Nicely done!")
            quit()
        elif dealer == 'blackjack':
            print("The Dealer got 21! Too bad for you!")
            quit()
        elif player == 'busted':
            print("You went over 21! You lose! Sorry!")
            quit()
        elif dealer == 'busted':
            print("The Dealer busted! Ouch! Well, you win!")
            quit()
        elif player > dealer:
            print("You got closer to 21! You win!")
            quit()
        elif dealer > player:
            print("The Dealer got closer to 21 than you did! They win!")
            quit()
        else:
            print("You aren't supposed to see this!")

s = blackJack()
s.menu()