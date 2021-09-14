import random
import time
from os import stat, system, name


def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

  
choices = ["Rock", "Paper", "Scissors"]

num_win_bot = 0

num_win_player = 0
# random_select_bot = random.choice(choices)
def help_game():
    print("********************************************************")
    time.sleep(1)
    print("* This game is prepared by Pouya Nasiri                *")
    time.sleep(1)
    print("* Victory condition :‌ The rock overcomes the scissors  *")
    time.sleep(1)
    print("* Victory condition :‌ The scissors overcomes the paper *")
    time.sleep(1)
    print("* Victory condition :‌ The paper overcomes the rock     *")
    time.sleep(1)
    print("********************************************************")
    while True:
        print("1 : Exit\n2 : Back")
        number = input("please choose on of the choices : ")    
        clear()
        if number == "1" :
            exit()
        elif number == "2":
            menu()
        else:
            print("Please select true choice !")
            time.sleep(2)
            help()
            
    
        
def set_choice():
    print("1 : Rock \n2 : Paper\n3 : Scissors\n4 : Exit")
    number = input("please choose on of the choices : ")
    if number == "1":
        return  "Rock"
    elif number == "2":
        return  "Paper"
    elif number == "3":
        return "Scissors"
    elif number == "4":
        exit()
    else :
        clear()
        show_info()
        print("Please select true choice !")
        time.sleep(2)
        return set_choice()
        
def menu() :
    print("* 1 : new game\n* 2 : Help \n* 3 : Exit")
    number = input("please choose on of the choices : ")
    clear()
    if number == "1":
        game()
    elif number == "2":
        help_game()
    elif number == "3":
        exit()
    else:
        print("Please select true choice !")
        time.sleep(2)
        menu()
        
def check_result(player_choice ,bot_choice):
    result = ""
    global num_win_bot
    global num_win_player
    print(f"you choose : {player_choice}")
    print(f"the Opponent choose : {bot_choice}")
    if player_choice == "Rock" and bot_choice == "Paper":
        result = "You lost in this round"
        num_win_bot+=1
        
    elif player_choice == "Paper" and bot_choice == "Scissors":
        result = "You lost in this round"
        num_win_bot+=1
        
    elif player_choice == "Scissors" and bot_choice == "Rock":
        result = "You lost in this round"
        num_win_bot+=1
        
    elif player_choice == bot_choice:
        result = "You equalized in this round"
    else :
        result = "You won this round"
        num_win_player+=1
        
    print(result)
    time.sleep(4)
    clear()
    
def show_info():
    global num_win_bot
    global num_win_player
    print(f"number of you win : {num_win_player}")
    print(f"number of bot win : {num_win_bot}") 

        
        
def game():
    num_win_bot = 0
    num_win_player = 0
    criterion_end = 0
    criterion_end = input("What is the number of wins for the end of the game : ")
    if not criterion_end.isnumeric():
        game()
    if int(criterion_end) == 0:
        menu()
    while(True):
        check_result(set_choice(),random.choices(choices)[0])
        show_info()
        time.sleep(2)
        if num_win_bot == int(criterion_end) :
            print("GAME OVER")
            time.sleep(2)
            break
        elif num_win_player == int(criterion_end):
            print("You win at all !!!")
            time.sleep(2)
            break
    
    menu() 
    
    

def main():
    print("\t****Welcome to Rock Paper Scissor Game***")
    menu()
    
    
if __name__ == '__main__':
    main()

    
    