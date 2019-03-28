from threading import *;
from time import *;

class A(Thread):
    def run(self):
        for i in range(1,21):
            print("i : ",i);
            sleep(1);

class B(Thread):
    def run(self):
        for j in range(1,21):
            print("j : ",j);
            sleep(2);


class C(Thread):
    def run(self):
        for k in range(1,21):
            print("k : ",k);
            sleep(3);


a1=A();
b1=B();
c1=C();

a1.setDaemon(True);  #only set b4 starting the thread else error

a1.start();
b1.start();
c1.start();

print("\n a1 is alive",a1.isAlive());
print("b1 is alive",b1.isAlive());
print("c1 is alive",c1.isAlive());

print("\n a1 is daemon",a1.isDaemon());
print("\n b1 is daemon",b1.isDaemon());
print("\n c1 is daemon",c1.isDaemon());

b1.join();

print("\n a1 is alive",a1.isAlive());
print("b1 is alive",b1.isAlive());
print("c1 is alive",c1.isAlive());

print("Program Exit.");
