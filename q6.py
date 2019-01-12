
import math
import random,sys
from decimal import Decimal

import matplotlib.pyplot as plt

def birthday(n,d):
    listOfBirthdays = []

    for i in range(1, int(n)):
        listOfBirthdays.append(random.randint(1, int(d)))

    seen = []
    for x in listOfBirthdays:
        if x in seen:
            # print("there is a duplicate in list", x)
            return True
        seen.append(x)
    # print("there is no duplicates in list")
    return False


def main(d):

    xaxis= []

    Xn=[]
    for i in range(1, 70):
        xaxis.append(i)


    for i in range(1, 70):
        numOfDuplicates = 0
        # print(numOfDuplicates)
        for j in range(1, 1000):
            if birthday(i,d): numOfDuplicates += 1
        Xi =  Decimal(numOfDuplicates)/Decimal(1000)
        Xn.append(float(Xi))
    print(Xn)

    Yn = []
    for i in range(1, 70):
        factorial1 = math.factorial(int(d))
        factorial2 = math.factorial(int(d)-i)
        power = math.pow(int(d),i)
        Yi = 1-Decimal(factorial1)/(Decimal(
            Decimal(factorial2)*Decimal(power)))
        Yn.append(float(Yi))
    print(Yn)
    plt.xlabel('n: num of tries')
    plt.ylabel('probability')
    plt.plot(xaxis, Xn, 'ro',label='X(n)')
    plt.plot(xaxis, Yn, 'g^',label='Y(n)')
    plt.legend()
    plt.show()
    return




if __name__ == "__main__":
    main(sys.argv[1])