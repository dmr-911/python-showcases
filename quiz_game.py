print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes" :
    quit()

totalQuestion = 0
result = 0

print("Okay! Let's play :) ")

answer = input("What does CPU stands for? ")
totalQuestion +=1

if(answer.lower() == "central processing unit") :
    result += 1

answer = input("What does GPU stands for? ")
totalQuestion +=1

if(answer.lower() == "graphics processing unit") :
    result += 1

answer = input("What does RAM stands for? ")
totalQuestion +=1

if(answer.lower() == "random access memory") :
    result += 1



print(f"You have scored {result} out of {totalQuestion}")