def abc(x):
    return x*x;

xyz=lambda y : y*y;

add= lambda x,y : x+y;  #use of lambda-security,improves performance,reduction of code, can hv multiple references of same func.
demo=add;   #func pointers.

res=abc(10);
print(res);  #100
res=xyz(5);
print(res);  #25
res=add(10,5);
print(res);  #15
res=demo(10,20);
print(res);  #30

numbers=[22,330,44,11,665,88,4,5,210,24,195,80];

def div5(i):  #this func can be called by anyone.
          if i%5==0:
            return True;

def div2(i):
    return i/2;  #if use i//2- o/p will be without decimal--> [11, 165, 22, 5, 332, 44, 2, 2, 105, 12, 97, 40]

print(numbers);  #[22, 330, 44, 11, 665, 88, 4, 5, 210, 24, 195, 80]

#to display multiples of 5?
res=list(filter(div5,numbers));  #create customized div5 func.
print(res);   #[330, 665, 5, 210, 195, 80]

res=list(filter(lambda n : n%10==0,numbers));  #Anonymous func.no name, to be used by only one func no one else.
#created lambda func so no one else can call it as lambda func has no name.<--USE
print(res);   #[330, 210, 80]

res=div5(21);   #Div5 can be accessed by anyone.
print(res);   #None

#map- to perform operation on all elements(each element of list.) 
#filters- to perform operations on some selected elements.

print(numbers);  #[22, 330, 44, 11, 665, 88, 4, 5, 210, 24, 195, 80]
half=list(map(div2,numbers));
print(half); #[11.0, 165.0, 22.0, 5.5, 332.5, 44.0, 2.0, 2.5, 105.0, 12.0, 97.5, 40.0]

third=list(map(lambda n:n//3,numbers));   #scope of lambda till here only. after mappping automatically garbage collected, so object of lambda is destroyed.
print(third);   #[7, 110, 14, 3, 221, 29, 1, 1, 70, 8, 65, 26]

def somefunc():   
    return lambda i:i*i;

#res=somefunc(3);  #error
sq=somefunc(); #will return reference of lambda func.
print(sq(4));   #16

def some(n):
    if n==1:
        return lambda i:i*i;  #can also do i:i*n; use of n here possible.
    else:
        return lambda i:i*i*i;

f1=some(2);
print(f1(4));   #64

f1=some(1);
print(f1(4));   #16

#mapping and then applying filter(reducing(map-reduce)-div by 3 printed)-
res=list(filter(lambda n:n%3==0,list(map(lambda n:n*2,numbers))));
print(res);   #[660, 420, 48, 390]

#in python functions are objects.
print(type(f1));  #<class 'function'>
print(type(somefunc));  #<class 'function'>
print(type(abc));  #<class 'function'>  thus either create through def, lambda or reference, function is an object.
