def abc():       #returns an abc object(collection) with these elements in list
	yield 1;
	yield 21;
	yield 3;
	yield 4;
	yield 5;

collection = abc();

#print(collection.__next__());  #o/p =1
#print(collection.__next__());  #o/p =21
#print(collection.__next__());  #o/p =3

for i in collection:
	print(i);  #o/p= 1,21,3,4,5  all printed since inside for loop.

def cube():
	for i in range(1,11):
		num=i*i*i;
		yield num;

cb=cube();
for i in cb:
	print(i);