from employees import *;

def main():
    while True:
        print("--------------");
        print("1. CREATE");
        print("2. DISPLAY");
        print("3. EXIT");
        print("-------------");
        ch1=int(input("Enter choice : "));
        if(ch1==1):
            while True:
                print("--------------");
                print("1. CLERK");
                print("2. programmer");
                print("3. MANAGER");
                print("4. EXIT");
                print("-------------");
                ch2=int(input("Enter choice : "));
                if ch2==1:
                    Clerk();
                if ch2==2:
                    Programmer();
                if ch2==3:
                    Manager();
                if ch2==4:
                    break;
        if ch1==2:
           Emp.display();

        if ch1==3:
            print("Total no of employees: ",Emp.count);
            break;

                
