# to calculate the time of the drop
import math


def time(h):
    h = float(h)
    t = 2 * h / 9.8
    t = math.sqrt(t)
    return t


t = time(100)
print("Time taken for 100m drop is (in sec)::" + str(t) + " s \n")


h = input("Enter the height(in meters) for which you wanna calculate!!\n")
t = time(h)
print("Time taken is (in sec)::" + str(t) + " s\n")
