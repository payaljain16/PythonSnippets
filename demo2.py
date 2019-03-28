class A :
    z=30;
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    #types of methods
    #1. instance method
    def display(self):
        print("x : ",self.x);
        print("y : ",self.y);
        
    @classmethod
    def abc(cls):   #can give any name to variable at cls place
        print("From class method : ",cls.z);
        
    @staticmethod
    def xyz(str):
        print("this is from static method.........",str);  #should not operate any variables here



a1=A(10,20);
a1.display();
#A.abc(A); used when not providing annotation with @
A.abc();
A.xyz('hi');
