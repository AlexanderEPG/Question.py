#1 question and 4 option quiz
#by APG
qA = int()
q1 = False
print("""what is 1 + 1?
(1)2
(2)54
(3)625
(4)*click*""")
while q1 == False:
        try:
                qA = int(input())
                if qA == 1:
                        score = score + 1
                        q1 = True
                elif 0 < qA < 5:
                        q1 = True
                else:
                        print("Please only type positve whole integers from 1-4")
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")
