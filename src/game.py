import random


class RockPaperScissors():
    def __init__ (self):
       self.list_choice = ["rock", "paper", "scissors"] 

    def get_player_choice(self):
        user_input = input(f"Enter your choice {self.list_choice}: ")
        if user_input.lower() in self.list_choice:
            return user_input.lower()
     
        print(f"Invalid choice, you must select from {self.list_choice}")
        return self.get_player_choice()
    
    def get_computer_choice(self):
        return random.choice(self.list_choice)
    
    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        
        win_combinetions = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
        for i in win_combinetions:
           if (user_choice == i[0]) & (computer_choice == i[1]):
               return "User winner"
        return "computer winner"
    
    # def play_again(self):
    #     print("do you like play again? (no --> q/Q) (yes --> anykeys)")
    #     if input() == "q" or "Q":
    #         return
    #     self.play()
        
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(user_choice, computer_choice)
        print(self.decide_winner(user_choice, computer_choice))
        #self.play_again()
    
    
if __name__ == "__main__":
        game = RockPaperScissors()

        while True:
            game.play()
            print("do you want play again? (no --> q/Q) (yes --> anykeys)")

            if input().lower() == 'q':
                break   
