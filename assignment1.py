import math

def isPerfectSquare(x): 
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0) 

def my_solution():
	numbers = [input('Enter a value: ') for i in range(10)]
	sq=[isPerfectSquare(y for y in numbers)] 
	for e in sq :
		print(e);

my_solution();