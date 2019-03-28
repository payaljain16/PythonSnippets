class Emp :
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def display(self) :
        print("Name : ",self.name);
        print("Age :",self.age);


##e1=Emp("Mohan",25);
##e2=Emp("Sohan",28);
##Emp.display(e1);
##Emp.display(e2);

class Calculator :
    def add(self,a,b):
        print("Add result : ",(a+b));


c1=Calculator();
Calculator.add(c1,10,20);
c1.add(30,50);

