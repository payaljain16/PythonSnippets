#i=1;
#while i<=10 :
#	print("just for demo : ",i);
#	i+=1;

l1=[11,22,33,44,55];
for item in l1 :
	print(item)
print("----------------");

for i in range(200,0,-50):
	print(i);
print("----------------");

for i in range(11):
	if i==5 :
		#break;
		continue;
	print(i);