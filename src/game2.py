import random
from typing import List

class RockPaperScissors:
    def __init__(self):
        self.list_choises: list[str] = ["rock","paper","scissors"]
    
    def get_user_choice(self) -> str:
        player_choice: str = input(f"please choice this one to run to game: {self.list_choises}: ")
        
        if player_choice.lower() in self.list_choises:
            print(f"You Choice: {player_choice.lower()}")
            return player_choice.lower()
        
        print(f"wrong please {self.list_choises}")
        return self.get_user_choice()
        
    def get_computer_choice(self) -> str:
        computer_choice: str = random.choice(self.list_choises)
        print(f"Computer Choice: {computer_choice}")
        return computer_choice
        
    def choice_winner(self, user: str, computer: str) -> str:
        if user == computer:
            return "It's Tie"
        
        user_win: list[str] = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]
        
        for i in user_win:
            if (user == i[0]) and (computer== i[1]):
                return "congratulations You Win"
            
        return "You Lose"
    
    def play(self):
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
