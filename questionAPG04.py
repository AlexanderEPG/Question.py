#1 question and 4 option quiz
#by APG
score = int(0)
qA = int()
q1 = False
print("choose from the choices below by choosing the number of the option")
print()
print()
print("""what is 1 + 1?
(1)54
(2)2
(3)625
(4)*click*""")
while q1 == False:
        try:
                qA = int(input("Your answer >"))
                if qA == 2:
                        score += 1
                        print("correct")
                        q1 = True
                elif 0 < qA < 5:
                        q1 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")
