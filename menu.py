def main():
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
			return;
   

def create():
	name=input("Enter name :");
	age=int(input("Enter age :"));
	salary=int(input("Enter salary :"));
	desig=input("Enter designation :");
	f1=open("emp.txt","a");
	data=name+"|"+str(age)+"|"+str(salary)+"|"+desig;
	f1.write(data);
	f1.write("\n");
	f1.close();

def display():
	f1=open("emp.txt","r");
	for line in f1:
		record=line.split("|");
		print("Name : ",record[0]);
		print("Age : ",record[1]);
		print("Salary : ",record[2]);
		print("Designation : ",record[3]);
	f1.close();

main()