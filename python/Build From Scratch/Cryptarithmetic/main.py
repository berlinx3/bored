import re
from itertools import permutations
import cProfile

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == CY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def solve(statement):
    for fx in fill_in(statement):
        if(valid(fx)):
            return fx
    return "No solution found!"

def valid(statement):
    try:
        return not re.search(r'\b0[0-9]', statement) and eval(statement) is True
    except ArithmeticError:
        return False
        

def fill_in(statement):
    letters = "".join(set(re.findall(r'[A-Z]', statement)))
    for digits in permutations('1234567890', len(letters)):
        trans = statement.maketrans(letters, "".join(digits))
        yield statement.translate(trans)

def testrun():
    for example in examples:
        answer = solve(example)
        print(example, " : " , answer)



def solveFaster(statement):
    f, letters = compile_formula(statement)
    for digits in permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                trans = statement.maketrans(letters, "".join(map(str, digits)))
                return statement.translate(trans)
        except ArithmeticError:
            pass
    
def compile_word(word):
    if word.isupper():
        conv = [f'10**{i} * {c}' for i, c in enumerate(word[::-1])]
        return '(' + ' + '.join(conv) + ')'
    else:
        return word

"""
eval will always have to evalate whole structure token by token in tree travesal
To reduce ncalls of eval, we take the repeated structure out and evaluate only once as function
subsequently we perform repeated functional call using evaluated f on our permutation
"""
def compile_formula(statement):
    letters = "".join(set(re.findall(r'[A-Z]', statement)))
    params = ", ".join(letters)
    firstletters = set(re.findall(r'\b([A-Z])[A-Z]', statement))
    tokens = map(compile_word, re.split(r'([A-Z]+)', statement))
    body = ''.join(tokens)
    if firstletters:
        zero_test = " and ".join([f'{fl} != 0'for fl in firstletters])
        body = f'{zero_test} and {body}'
    f = f'lambda {params}: {body}'
    return eval(f), letters


def testrunFaster():
    for example in examples:
        answer = solveFaster(example)
        print(example, " : " , answer)


print("Faster")
print("======")
testrunFaster()
print("\n\n")
print("Slower")
print("======")
testrun()
# cProfile.run('testrun()')

