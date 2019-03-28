class employee:
    count=0;
    def __init__(self):
        self.f1=open("data.txt","a");
        self.name=input("Enter your name:- ")
        self.age=input("Enter your age:- ");
        self.record=self.name+"|"+self.age+"|";
        employee.count+=1;
        self.f1.write(self.record);
        self.f1.close();
    def create():
        i=0;
        while i!=4 :
            print("\n------------");
            print("\n1:Clerk");
            print("2:Programmer");
            print("3:Manager");
            print("4:exit");
            print("\n------------");
            i=int(input("Enter your choice: "));
            if i==1:
                c1=Clerk();
            if i==2:
               p1=Programmer();
            if i==3:
                m1=Manager();
            
               
    def display():
        f1=open("data.txt","r");
        print("Details of Employees")
        for data in  f1:
            record=data.split("|");
            print("\nName:-",record[0]);
            print("Age:-",record[1]);
            print("Salary:-",record[2]);
            print("Designation:-",record[3]);
        f1.close();

class Clerk(employee):
    def __init__(self):
        super().__init__();
        self.f1=open("data.txt","a");
        self.salary=8000;
        self.designation="Clerk";
        self.record=str(self.salary)+"|"+self.designation+"\n";
        self.f1.write(self.record);
        self.f1.close();
class Programmer(employee):
    def __init__(self):
        super().__init__();
        self.f1=open("data.txt","a");
        self.salary=25000;
        self.designation="Programmer";
        self.record=str(self.salary)+"|"+self.designation+"\n";
        self.f1.write(self.record);
        self.f1.close();
class Manager(employee):
    def __init__(self):
        super().__init__();
        self.f1=open("data.txt","a");
        self.salary=80000;
        self.designation="Manager";
        self.record=str(self.salary)+"|"+self.designation+"\n";
        self.f1.write(self.record);
        self.f1.close();



i=0;
while i!=3:
    print("\n------------");
    print("\nMenu");
    print("1:create");
    print("2:display");
    print("3:exit");
    print("\n------------");
    i=int(input("Enter your choice: "));
    if i==1:
        employee.create();
    if i==2:
        employee.display();
    if i==3:
            print("Total employees added : ",employee.count);
           

