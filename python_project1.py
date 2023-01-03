print("Welcom to my quiz!")
ready = input("Are u ready? ")
if ready.lower()=='yes':
    print("Okay! Let's start :)")
else:
    quit()
score=0

print("1, How many letters are in the alphabet?" )
print("A:26 letters\nB:11 letters\nC:28 letters")
answer=input("Type ur letter here (in CAP) ")
if answer!="B":
    print("INCORRECT\nThe answer is B: 11 letters (the alphabet)")
if answer=="B":
    print("CORRECT!")
    score+=1

answer=input("2, If the assistant captain of a sports team were to die, who would lead the team?\nType ur answer here ")
if answer.lower()=="the captain":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT\nThe answer is The captain")

print("3, If 7 adults can eat seven cupcakes in 7 minutes, how long would it take 30 adults to eat 30 cupcakes?" )
print("A:30 min\nB:210 min\nC:7 min")
answer=input("Type ur letter here (in CAP) ")
if answer=="C":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT! It is 7 minutes because one adult takes 7 minutes to eat a cupcake. haha")

answer=input("3, What is the answer to this qurstion?\nType ur answer here ")
if answer.lower()=="what":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT\nNo explanation for this...I thought you know how to read :/")

if score >= 3:
    print("Your total score is " +str(score)+ ". Great Job!" )
else:
     print("Your total score is " +str(score)+ ". I'm sure you can do better next time :)" )
print("____________________________________________________")
print("**All questions are from rd.com\nCode by Serema Zhu")

