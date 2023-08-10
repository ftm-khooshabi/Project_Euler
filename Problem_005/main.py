import math

def Smallest_Multiple(x, y) : # # Smallest multiple for all af numbers in range (x, y)
    Rangeـofـnumbers = [i for i in range(x, y+1)]
    Multiple = math.lcm(x,y)
    for item in Rangeـofـnumbers:
        Multiple = math.lcm(Multiple, item)
    print('Smallest_Multiple = ', Multiple)


Smallest_Multiple(1,20)
