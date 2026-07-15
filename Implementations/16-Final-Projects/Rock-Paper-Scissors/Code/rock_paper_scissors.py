import random

def get_Choice():
    player_choice=str(input(" Enter a Choice (Rock,Paper,scissors)? ")).lower()
    machine_choice=['rock','paper','Scissors']
    Computer_choice=random.choice(machine_choice)

    Choices = {'player' : player_choice, 'machine': Computer_choice}
    return Choices

def check_win(player,computer):
    print(f"\nYou Chose {player}\nComputer Chose {computer}\n")
    if player == computer :
        return "It's a Draw"
    
    elif player == 'rock' :
        if computer == 'paper' :
            return "Computer Wins!"
        return "Player Wins!"
    
    elif player =="paper" :
        if computer == "rock" :
            return "player Wins!"
        return "Computer Wins!"
    
    elif player == "scissors":
        if computer == "paper":
            return "Player Wins!"
        return "Computer Wins!"
        
    else:
        return "Invalid Choice"
    

 
   
    

Choices = get_Choice()

result = check_win(Choices["player"],Choices["machine"])
print (result)

      
