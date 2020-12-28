import math
#my brain exploded by the way please pay for surgery
def first_exponent(b, e, tower_base):
    return(e*math.log(b, tower_base))

def bhatlog(x, n, b):
    #log(log(log(log(x))))//n times, with b base
    for time in range(0, n):
        x=math.log(x, b)
        if x<=0:
            return 0
    return x

def check_for_unsolvables(exponents):
    if type(exponents) != list and type(exponents) != tuple:
        raise Exception("The first parameter is not a valid list!")
    for item in exponents:
        if item<=0:
            raise Exception("One of the values was not a positive rational number!")

def solve_large_exponents(exponents, towers_number=10):
    check_for_unsolvables(exponents)
    powers = 0
    e=0
    for i in range(len(exponents)-1, 0-1, -1):
        if i==len(exponents)-1:
            e=first_exponent(exponents[i-1], exponents[i], towers_number)
            powers += 1
        else:
            e += bhatlog(exponents[i-1], powers+1, towers_number)
            powers += 1
    while e>=21:
        e=math.log(e, towers_number)
        powers += 1
    return powers-1, e


def main():
    expression = input("Please enter your expression (for eg. 101^9874973^1098^12.123, currently only the power operation is supported): ")
    try:
        expression=expression.split("^")
        expression=[float(i) for i in expression]
    except:
        return print("Please check your values again!")
    raw_result = solve_large_exponents(expression)
    processed_result="10^"*int(raw_result[0])
    print(processed_result+str(raw_result[1]))


main()

