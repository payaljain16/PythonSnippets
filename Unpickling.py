import pickle;
from Personn import Personn; 

f2=open("person.ser","rb");
p1=pickle.load(f2);
print(p1);  #o/p= Name: Sujatha /n Age : 25

print(p1.name);  #o/p= Sujatha
print(p1.age);  #o/p=25