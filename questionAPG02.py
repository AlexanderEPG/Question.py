#1 question and 4 option quiz
#by APG
Print("what is 1 + 1")
while qC == False:
        try:
                qO = int(print("(1)2 (2)54 (3)625 (4)*click*")
                if 0 < qO < 5:
                        qC = True
                        if qO == 1:
                                score = score + 1
        except ValueError:
                print("you didnt't enter one of the numbers given, please try again")
