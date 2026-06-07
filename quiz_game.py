# Project: Python Quiz Game
# Author: Sri Sahana
# Concepts Used:
# - Lists
# - User Input
# - Conditional Statements
# - Score Tracking
print("Welcome to quiz time\nAre u ready!!!!")
correct_answer=[]
wrong_answer=[]
answered=[]
print("Who introduced python?\na)Charles Babbage\nb)Guido Van Rossum")
Q1=input("Enter your option: ").lower()
answered.append(Q1)
if Q1 == "a" or Q1 == "b":
    if Q1 == "b":
        correct_answer.append("Guido Van Rossum")
    else:
        wrong_answer.append("Charles Babbage")
else:
    print("Invalid choice")
print("In which year python released?\na)1989\nb)1991")
Q2=input("Enter your option: ").lower()
answered.append(Q2)
if Q2 == "a" or Q2 == "b":
    if Q2 == "b":
        correct_answer.append("1991")
    else:
        wrong_answer.append("1989")
else:
    print("Invalid choice")
print("Why did the creator start building python in december?\na)As a hobby\nb)To hack into early internet system")
Q3=input("Enter your option: ").lower()
answered.append(Q3)
if Q3 == "a" or Q3 == "b":
    if Q3 == "a":
        correct_answer.append("As a hobby")
    else:
        wrong_answer.append("To hack into early internet system")
else:
    print("Invalid choice")
print("Which is Older?\na)JAVA\nb)Python")
Q4=input("Enter your option: ").lower()
answered.append(Q4)
if Q4 == "a" or Q4 == "b":
    if Q4 == "b":
        correct_answer.append("Python")
    else:
        wrong_answer.append("JAVA")
else:
    print("Invalid choice")
print("Where was python originally developed?\na)The Netherlands\nb)USA")
Q5=input("Enter your option: ").lower()
answered.append(Q5)
if Q5 == "a" or Q5 == "b":
    if Q5 == "a":
        correct_answer.append("The Netherlands")
    else:
        wrong_answer.append("USA")
else:
    print("Invalid choice")
print("Correct answers: ",correct_answer)
print("Wrong answers: ",wrong_answer)
print("Attended questions: ",len(answered))
print("Score = ",len(correct_answer))
print("Number of wrong answers: ",len(wrong_answer))
percentage = (len(correct_answer) / 5) * 100
print("Percentage =", percentage, "%")
