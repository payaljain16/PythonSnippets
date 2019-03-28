class Clerk:
    salary=8000;
    desig="Clerk";

class Programmer:
    salary=25000;
    desig="Programmer";

class Manager:
    salary=80000;
    desig="Manager";

class Emp(Clerk,Programmer,Manager):
        
    def emp():
        choice = 0;
        count=0;
        while True:
            print("Select your choice:");
            print("1. Create");
            print("2. Display");
            print("3. Exit");
            choice = int(input("Please type 1-3 from the menu. "))
            if choice == 1:
                count+=1;
                create();
            elif choice == 2:
                display();
            elif choice == 3:
                print("Total no of employees added : ",count);
                
   

def create():
        while True:
            print("Select your choice:");
            print("1. Clerk");
            print("2. Programmer");
            print("3. Manager");
            print("4. Exit");
            ch = int(input("Please type 1-4 from the menu. "))
            if ch == 1:
                name=input("Enter name :");
                age=int(input("Enter age :"));
                f1=open("employee.txt","a");
                data=name+"|"+str(age)+"|"+str(Clerk.salary)+"|"+Clerk.desig;
                f1.write(data);
                f1.write("\n");
                f1.close();
            elif ch == 2:
                name=input("Enter name :");
                age=int(input("Enter age :"));
                f1=open("employee.txt","a");
                data=name+"|"+str(age)+"|"+str(Programmer.salary)+"|"+Programmer.desig;
                f1.write(data);
                f1.write("\n");
                f1.close();
            elif ch == 3:
                name=input("Enter name :");
                age=int(input("Enter age :"));
                f1=open("employee.txt","a");
                data=name+"|"+str(age)+"|"+str(Manager.salary)+"|"+Manager.desig;
                f1.write(data);
                f1.write("\n");
                f1.close();
            elif ch == 4:
                Emp.emp();

	
	

def display():
	f1=open("employee.txt","r");
	for line in f1:
		record=line.split("|");
		print("Name : ",record[0]);
		print("Age : ",record[1]);
		print("Salary : ",record[2]);
		print("Designation : ",record[3]);
	f1.close();

Emp.emp()
