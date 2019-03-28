class emp :
    count=0;
    def __init__(self,name,age,salary,desig):
        self.name=name;
        self.age=age;
        self.salary=salary;
        self.desig=desig;
        emp.count+=1;
    def display(self):
        print("Name : ",self.name);
        print("Age : ",self.age);
        print("salary : ",self.salary);
        print("Designation : ",self.desig);
    def set_age(self,age):   #preferred is all small letters with underscore between words
        self.age=age;
    def __del__(self):
        print("Object with name : '%s' getting destroyed " %self.name);


e1=emp("Raju",22,100000,"MAnager");
e1.display();

e2=emp("ghj",27,900000,"Associate");
e2.set_age(29);
#e2.age=45;  #modified
e2.count=5; #not modified coz class variable
#emp.count=5; this will affect and no of emp shows=5
e2.display();

del e1;

print("\n Total no. of employees created : ",emp.count);
print(e1.name);
