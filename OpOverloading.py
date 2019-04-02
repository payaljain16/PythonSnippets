class Emp:
    def __init__(self,name,age,salary):
        self.name=name;
        self.age=age;
        self.salary=salary;

    def __str__(self):  #toString method in java, here predefined method in python
        print("name: ",self.name);
        print("Age : ",self.age);
        print("Salary : ",self.salary);
        return "";

    def __add__(obj1,obj2):
        x=obj1.salary;
        y=obj2.salary;
        z=x+y;
        e3=Emp(obj1.name,obj1.age,z);
        return e3;

    def __gt__(obj1,obj2):
        x=obj1.age;
        y=obj2.age;
        if x>y:
            return True;
        else:
            return False;


e1=Emp("Ravi",42,32000);
e2=Emp("Ravi2",23,36000);
e4=Emp("Adi",34,34000);
#print(e1);  #when no str method print Emp object with hexcode like in java without toString method.
#when str method present e1 returns toString wala code python one.
#print(e1.name);
#print(e1.salary);

print(e1);
print(e2);
print(e4);

#e3=e1+e2;
#print(e3);  Invalid without add function

e3=e1+e2;  #+ operator calls add func thus its code is implemented.
print(e3);

e=e1+e2+e4;  #valid since e1+e2 gets replaced by e3 in add func and add func gets again implemented for e3+e4.
print(e);

print("Comparing which employee is senior in age : ");
if e1 > e2:
    print(e1.name,"is senior.");
else:
    print(e2.name,"is senior.");

#s1="Hello";  #need to keep gt in String class for overloading.
#print(s1>3); #3 char shifted to right but total length of str remains same. o/p="   He"
#print(s1<2); #o/p= "llo  " left shifted by 2
#thus this is not possible as need to modify string class which is not possible.
