from numpy import *;

arr=array([1,2,3,4,5,'ab']);
print(arr);

print(arr.dtype);
print(type(arr));


ls=linspace(1,10);
print(ls);

logs=logspace(1,50);
print(logs);
print("%.1f" %logs[1]);

ar=arange(50,1,-5);
print(ar);

a=arange(1,50,-5);
print(a);

z=zeros(5);
print(z);

z1=zeros(5,int);
print(z1);

z2=zeros(4,str);
print(z2);

z=zeros(5,bool);
print(z);

z4=ones(5);
print(z4);

z=ones(2,bool);
print(z);

arr2=arr;
print(arr2);
print(id(arr));
print(id(arr2));

arr2=arr.view();
arr[1]=100;
print(arr);
print(arr2);
print(id(arr));
print(id(arr2));

arr2=arr.copy();
arr[1]=200;
print(arr);
print(arr2);
print(id(arr));
print(id(arr2));
