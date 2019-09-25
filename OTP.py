import math
import random as r
def otpgen():
    otp=""
    for i in range(2):
        otp+=str (r.randint(1,9))
    print ("Your One Time Password is " + otp)
    

