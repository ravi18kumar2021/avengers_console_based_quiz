from quiz_questions import quiz, check_answer

score = 0
attempt = 3

for question in quiz:
    
    while attempt > 0:
        print(quiz[question]['question'])
        answer = input("Enter Answer : ")
        if check_answer(question, answer):
            score += 10
            break
        else:
            attempt -= 1
            print("Wrong !\nAttempt : {} left".format(attempt))
    if attempt == 0:
        print("You lose")
        print("Your score :", score)
        break

if attempt > 0:
    print("You win")
    print("Your score :", score)
