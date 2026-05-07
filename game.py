import random

round = 1
total_round = 5

users = {"user1", "user2", "user3"}
score_board = {
    "user1": 0,
    "user2": 0,
    "user3": 0,
}


def generateRandomNumber():
    number = 0
    try:
        number = random.randint(1, 9)
    except Exception as e:
        number = 7
    finally:
        return number


def verifyNumber(input, number):
    if input == 0:
        print("Please enter a valid number")
    else:
        if user_input == number:
            currentScore = score_board.get(user)
            score_board[user] = currentScore + 1
            print("Correct!")
        else:
            print("Not a match!")


while round <= total_round:
    print(f"Round {round}: ")
    random_num = generateRandomNumber()
    for user in users:
        user_input = input(f"{user.capitalize()} Guess a number between 1 to 9: ")
        user_input = int(user_input)
        verifyNumber(user_input, random_num)
    round += 1

print("Final Scores: ", score_board)
