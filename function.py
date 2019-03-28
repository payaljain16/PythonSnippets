def abc(a,b):
    print("a : ",a);
    print("b : ",b);

def xyz(a,b):
     print("a : ",a);
     print("b : ",b);

def add(*a):
    res=0;
    for i in a:
       res=res+int(i);
    print("result :",res);

abc(10,20);
xyz(b=20,a=10);
add(10,20);
add();
add(11,22,33,44);
add(25);
