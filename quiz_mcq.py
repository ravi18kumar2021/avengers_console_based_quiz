from quiz_questions import quiz, check_answer
import random

score = 0

attempts = 3

for question in quiz:
        while attempts > 0:
                print()
                print(quiz[question]['question'])
                options = random.sample(quiz[question]['options'], 4)
                print("Choose a option number :")
                for i,j in enumerate(options):
                        print("{}. {}".format(i+1,j))
                answer = input("Enter a number : ")
                try:
                        answer = int(answer)
                except ValueError:
                        print("## Please enter a number (1/2/3/4) ##")

                                
                if type(answer) == int:
                        if answer > 0 and answer < 5:
                                answer = options[answer - 1]
                                if check_answer(question, answer):
                                        score += 10
                                        break
                                else:
                                        if score > 0:
                                                score -= 5
                                        attempts -= 1
                                        
                                        print("Wrong !\nAttempt left : {}".format(attempts))
                        else:
                                print("Invalid choice")
        if attempts == 0:
                print("You lose")
                print("Your score :", score)
                break

if attempts > 0:
    print("You win")
    print("Your score :", score)
                
