from math import sqrt,floor;

def findSqrt(num) :
	a=sqrt(num);
	if a-floor(a)== 0 :
		print(num," is a perfect square root");

list1=[]; //displays after all elements are input
for i in range(0,10) :
	list1.append(int(input("Enter value : ")));

for i in range(0,10) :
	findSqrt(list1[i]);

for i in range(0,10) :
	x=(int(input("Enter value : ")));
	findSqrt(x);