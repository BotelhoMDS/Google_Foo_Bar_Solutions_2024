import pandas as pd 
import  numpy as np
#from itertools import permutations
def permutations(lst, n):
    if n == 0:
        return [[]]
    
    all_permutations = []
    for i in range(len(lst)):
        current_element = lst[i]
        remaining_elements = lst[:i] + lst[i+1:]

        for perm in permutations(remaining_elements, n - 1):
            all_permutations.append([current_element] + perm)

    return all_permutations

def list_to_int(lst):
    return int(''.join(map(str, lst)))

def solution(L):
    L.sort(reverse=True)
    aux = L.copy()
    length = len(L)
    max_number = 0
    for a in range(length,0,-1):
        #perms = permutations(L, a)
        #resultados = [int(''.join(map(str, perm))) for perm in perms]
        resultados = permutations(L,a)
        resultados.sort(reverse=True)
        
        
        for numbers in resultados:
            number = list_to_int(numbers)
            if number % 3 == 0 and number > max_number:
                max_number = number
            if max_number != 0:
                return number
    return 0
                
        

print(solution([3,1,4,1])) # 4311
print(solution([3,1,4,1,5,9])) # 94311 
print(solution([4,7]))#0

#This solution is not efficient enough to pass the tests
#I need research more about this problem to resolve it

