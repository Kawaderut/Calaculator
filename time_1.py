from time import *
import random as r
# print(time())

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error = error+1
        except:
            error = error+1
    return error
def spped_time(time_s,time_e,userinput):
    time_dealy = time_e- time_s
    time_R =round(time_dealy,2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
    ck=input("ready to test: yes/no:")
    if ck == "yes":
        test = ["a paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea",
         "my name is rutuja", "welcome to pune"]
        test1 = r.choice(test)
        print("          ***** typing speed ***** ")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter:")
        time_2 = time()

        print('Speed:', spped_time(time_1, time_2, testinput), "w/sec")
        print("Error:", mistake(test1, testinput))
    elif ck == 'no':
       print(" thnk you ")
       break
    else:
       print(" wrong input ")

    




           

    
