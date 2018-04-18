from builtins import ValueError


def calculateBmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError('weight and height can not be less than 0')
    return weight/(height/100)**2
