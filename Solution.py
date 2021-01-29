from math import erf,sqrt

def cumulative(m,sd,x):
    return (1 + erf((x - m) / (sd * sqrt(2)))) / 2

print round(cumulative(205*49, 15*sqrt(49), 9800), 4)
