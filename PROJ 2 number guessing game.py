def play_game():
    import random
    number=random.randint(1,100)
    while True:
        
        try:
            
            
            guess=int(input("take your guess:"))
            
        except ValueError:
            
            print("Number only")
            
            continue
        
        
            
        if guess<number:
            print("low")
        elif guess>number:
            print("high")
        else:
            print("correct")
            break


while True:
    play_game()
    choice=input("do u want to play again?(Yes/No): ")
    if choice=="no":
        print("game ended")
        break
