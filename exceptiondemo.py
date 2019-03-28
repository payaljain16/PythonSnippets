#to create own exception
class AbcError(Exception):
    def display(self):
        print("custom exception handler.");


a=5;
try:
    b=int(input("Enter value for b :"));
    c=int(input("Enter value for c :"));
    print("Result : ",(b+c));
    for i in range(10):
        print(i);
        res=a/(a-i);
        if i == 8 :
            raise Exception;
        if i == 3:
            raise AbcError;

except ValueError as v:
    print("please enter no only : ",v);
        
except ZeroDivisionError:
    print("Denominator cant be zero");
except AbcError as a:
    print("user defined Exception");
    a.display();
except Exception as e:
    print("default exception handler : ",e);
else:
    print("Everything is fine.");
finally:
    print("always executed.");

print("Program continues.....");


