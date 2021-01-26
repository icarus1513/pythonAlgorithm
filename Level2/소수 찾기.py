import itertools

def is_prime_number(x):
    if(x<=1):
        return False
    for i in range(2, x):
        if x % i == 0:
    	    return False
    return True

def solution(numbers):
    val_set = set()
    for i in range(len(numbers),0,-1):
        for val in list(map("".join, itertools.permutations(numbers,i))):
            if is_prime_number(int(val)) is True:
                val_set.add(int(val))
    print(val_set)
    answer = len(val_set)
    return answer