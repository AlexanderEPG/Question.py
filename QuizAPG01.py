#1 question and 4 option quiz
#by APG
score = int(0)
qA = int()
q1 = False
q2 = False
print("choose from the choices below by choosing the number of the option")
print()
print()
Q1 = print("""what is 1 + 1?
(1)54
(2)2
(3)625
(4)*click*""")
while q1 == False:
        print (Q1)
        try:
                qA = int(input("Your answer >"))
                if qA == 2:
                        score += 1
                        q1 = True
                elif 0 < qA < 4:
                        q1 = True
                elif qA == 4:
                        print("my brotha, do you know da wey")
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")


Q2 = print("""what is the square root of 625?
(1)25
(2)15
(3)65
(4)69""")
while q2 == False:
        print (Q1)
        try:
                qA = int(input("Your answer >"))
                if qA == 1:
                        score += 1
                        q2 = True
                elif 0 < qA < 4:
                        q2 = True
                elif qA == 4:
                        print("hahaha( ͡° ͜ʖ ͡°)")
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")

print("you have", score,"point(s)")
                
