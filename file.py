f1=open("abc.txt","r");

#print(f1.read());
print(f1.readline(), end=""); 
print(f1.readline(), end="");
print(f1.readline(), end="");   #reads single line
print(f1.readline(5)); #to read 5 chars only
#f1.seek(50);
#f1.close();


f2=open("xyz.txt","a");
for data in f1:
	f2.write(data);
f2.close();      #copy f1 to f2 
