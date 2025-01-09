import random


class RockPaperScissors:
    def __init__(self):
        self.list_choises = ["rock","paper","scissors"]
    
    def get_user_choice(self):
        player_choice = input(f"please choice this one to run to game ({self.list_choises}): ")
        if player_choice.lower() in self.list_choises:
            print(f"You Choice: {player_choice.lower()}")
            return player_choice.lower()
        
        print(f"wrong please {self.list_choises}")
        return self.get_user_choice()
        
    def get_computer_choice(self):
        computer_choice = random.choice(self.list_choises)
        print(f"Computer Choice: {computer_choice}")
        return computer_choice
        
    def winner(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        if computer_choice == user_choice:
            return "It's Tie"
        
        user_win = [("paper", "rock"), ("rock", "scissors"), ("scissors", "paper")]
        for i in user_win:
            if (user_choice == i[0]) & (computer_choice== i[1]):
                return "congratulations You Win"
            
        return "You Lose"
    
    def play(self):
        #print(f"User Choise: {self.get_user_choice()}")
        #print(f"Computer Choise: {self.get_computer_choice()}")
        print(self.winner())
        
if __name__ == "__main__":
    Play = RockPaperScissors()    
    while True:
        Play.play()
        print("do you like play again?: (yes --> anykeywords) (no --> Q/q)")
        if input() in ('q' , 'Q'):
            break