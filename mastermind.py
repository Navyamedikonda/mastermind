import random
def generate_code():
    return str(random.randint(1000,9999))
def validate_input(input_str):
    if not input_str.isdigit():
        return False
    if len(input_str) != 4:
        return False
    return True
def get_valid_input(prompt):
    while True:
        user_input=input(prompt)
        if validate_input(user_input):
            return user_input
        print("Please enter a valid 4 digit number")
def check_guess(secret_code,guess):
    return sum(a==b for a,b in zip(secret_code,guess))
def player1_turn():
    print("Player1 ,set ur code(4-digit number)")
    return get_valid_input("Enter ur code")
def player2_turn(secret_code):
    attempts=0
    while True:
        print("Player2 guess the code:")
        guess=get_valid_input("Enter ur guess:")
        attempts+=1
        correct_digits=check_guess(secret_code,guess)
        if correct_digits==4:
            print("Player2 wins in",attempts,"Attempts")
            return attempts
        else:
            print("You got ",correct_digits,"digits corrrect.Try again")
def main():
    while True:
        secret_code=player1_turn()
        player2_attempts=player2_turn(secret_code)
        if player2_attempts==1:
            print("player2 wins")
            break
        print("\n Now its player2 s turn to set code:")
        secret_code=generate_code()
        player1_attempts=player2_turn(secret_code)
        if player1_attempts<player2_attempts:
            print("player1 wins")
        elif player1_attempts>player2_attempts:
            print("player2 wins")
        else:
            print("Its draw!")
        play_again=input("Do u want to play agin?(yes/no):")
        if play_again.lower()!="yes":
            break
if __name__=="main_":
    main()