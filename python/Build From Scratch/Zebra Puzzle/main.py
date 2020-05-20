from itertools import permutations


def imright(left, right):
    return right - left == 1


def neighbours(n1, n2):
    return abs(n1 - n2) == 1

"""
First determine
- variables - houses / nationality / pet..
- domains - what values can be assigned to each variables
- constraints
"""
def zebra_puzzle():
    houses = [1, 2, 3, 4, 5]
    first = 1
    middle = 3
    orderings = list(permutations(houses))
    # Generator - yield result only when required instead loop all
    return next((Water, zebra)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(ivory, green)
                for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings
                if Englishman is red
                if Norwegian is first
                if Norwegian is blue
                for (dog, snails, zebra, fox, horse) in orderings
                if Spaniard is dog
                if neighbours(Norwegian, fox)
                for (Coffee, Milk, Orange_Juice, Water, Tea) in orderings
                if Coffee is green
                if Ukrainian is Tea
                if Milk is middle
                for (Old_Gold, Kools, Chesterfields, Lucky_Strike, Parliaments) in orderings
                if Old_Gold is snails
                if Kools is yellow
                if neighbours(Kools, horse)
                if Lucky_Strike is Orange_Juice
                if Japanese is Parliaments )

print(zebra_puzzle())