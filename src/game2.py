"""
   author: MohammadHesam Pourakbar
   date: 2025.1.12
   summery: The game RockPaperScissors
"""


import random
from typing import List, Tuple

class RockPaperScissors:
    """This is main class RockPaperScissors"""
    
    def __init__(self):
        self.list_choises: List[str] = ["rock","paper","scissors"]
    
    def get_user_choice(self) -> str:
        """user gets random --> ["rock","paper","scissors"]"""  
        player_choice: str = input(f"please choice this one to run to game: {self.list_choises}: ")
        
        if player_choice.lower() in self.list_choises:
            print(f"You Choice: {player_choice.lower()}")
            return player_choice.lower()
        
        print(f"wrong please {self.list_choises}")
        return self.get_user_choice()
        
    def get_computer_choice(self) -> str:
        """Computer gets random --> ["rock","paper","scissors"]"""  
        computer_choice: str = random.choice(self.list_choises)
        print(f"Computer Choice: {computer_choice}")
        return computer_choice
        
    def choice_winner(self, user: str, computer: str) -> str:
        """this method: who is the winner (computer or user)
        
        :param user: The user choice, Must be one of ["rock","paper","scissors"]
        :param computer: The computer choice, Must be one of ["rock","paper","scissors"]
        :return: who is won!
        """
        if user == computer:
            return "It's Tie"
        
        user_win: List[Tuple[str, str]] = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]
        
        for i in user_win:
            if (user == i[0]) and (computer== i[1]):
                return "congratulations You Win"
            
        return "You Lose"
    
    def play(self):
        """one of the main methode, run this project"""
        user_choice: str = self.get_user_choice()
        computer_choice: str = self.get_computer_choice()
        #print(f"Computer Choise: {self.get_computer_choice()}")
        print(self.choice_winner(user_choice, computer_choice))
        
if __name__ == "__main__":
    Play = RockPaperScissors()    
    while True:
         Play.play()
         print("do you like play again?: (yes --> anykeywords) (no --> Q/q)")
         if input().lower() == 'q': # چرا در پارنتز قرار دادن Q بزرگ کار نمیکنه
             break
