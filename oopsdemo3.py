class A :
    def abc(self):
        print("HI");

class B:
    def xyz(self):
        print("HELLO");

##class C(B):  #multi level
##    def atoz(self):
##        print("DEMO");

##class C(A):  #hierarchical
##    def atoz(self):
##        print("DEMO");

class C(A,B):  #multiple inheritance
    def atoz(self):
        print("DEMO");


a1=A();
a1.abc();

b1=B();
#b1.abc();
b1.xyz();

c1=C(); #when c introduced,multi level inheritance otherwise single level.
c1.abc();
c1.xyz();
c1.atoz();

print(type(c1));

