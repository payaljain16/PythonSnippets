class Emp:
    count=0;
    def __init__(self,salary,desig):
        self.name=input("Enter your name:- ");
        self.age=input("Enter your age:- ");
        self.salary=salary;
        self.desig=desig;
        f1=open("empp.txt","a");
        f1.write(self.name+"|"+str(self.age)+"|"+str(self.salary)+"|"+self.desig+"\n");
        f1.close();
        Emp.count+=1;
               
    def display():
        f2=open("empp.txt","r");
        for record in f2:
            rec=record.split("|");
            print("\n Name : ",rec[0]);
            print("Age :",rec[1]);
            print("Salary :",rec[2]);
            print("Designation : ",rec[3]);
    

class Clerk(Emp):
    def __init__(self):
        super().__init__(8000,"Clerk");
    
        
class Programmer(Emp):
    def __init__(self):
        super().__init__(25000,"Programmer");
        
class Manager(Emp):
    def __init__(self):
        super().__init__(80000,"Manager");

           

