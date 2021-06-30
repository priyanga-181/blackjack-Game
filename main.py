############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from replit import clear
from art import logo
def deal_card():
  cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw!"
  elif computer_score==0:
    return "you lose! The opponent has Blackjack"
  elif user_score==0:
    return "You win! You have Blackjack"
  elif user_score>21:
    return "You lose!Its more than 21"
  elif computer_score>21:
    return "You win!The opponent has more than 21"
  elif user_score>computer_score:
      return "you won the game"
  else:
      return "The opponent has won"
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  the_end=False
  while not the_end:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your Cards: {user_cards},your score: {user_score}")
    print(f"Computer's First card: {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
      the_end=True
    else:
      choise=input("Type 'y' to get another card or 'n' to pass: ")
      if choise=='y':
        user_cards.append(deal_card())
      elif choise=='n' or 'N':
        the_end=True
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"your final hand is: {user_cards},your final score is {user_score}")
  print(f"computer's final hand is: {computer_cards},your final score is {computer_score}")

  print(compare(user_score,computer_score))

  wish=input("Do you wanna restart the game?'y' or 'n'")
  if wish=='y' or 'Y':
    clear()
    play_game()
play_game()





#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

