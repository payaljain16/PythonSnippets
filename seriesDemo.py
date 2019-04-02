import pandas as pd
import numpy as np

data=np.array(['Aman','Ravi','Shobha','Payal','Naman']);
print(data);  #o/p=['Aman' 'Ravi' 'Shobha' 'Payal' 'Naman']

#for displaying serial no.
s=pd.Series(data);
print(s);

##
##O/P-
##0      Aman
##1      Ravi
##2    Shobha
##3     Payal
##4     Naman
##dtype: object

s=pd.Series(data,index=[101,102,103,104,105]);
print(s);
##o/p when given index in pd.Series-
##101      Aman
##102      Ravi
##103    Shobha
##104     Payal
##105     Naman
##dtype: object

print("-------------------");
s=pd.Series("hello",index=[100,102,103,104,105]); #101 omitted, its not in o/p also
print(s);

##o/p-
##100    hello
##102    hello
##103    hello
##104    hello
##105    hello
##dtype: object

s=pd.Series(['Geeta','Seeta','reeta','Meeta','Leeta'],index=['a','b','c','d','e']);
print(s[1]);     #Seeta
print(s['b']);   #Seeta

#Customized Indexing- Can be more than 1 char.
s=pd.Series(['Geeta','Seeta','reeta','Meeta','Leeta'],index=['geet','s','r','mee','l']);
print(s[1]);     #Seeta
print(s['r']);   #reeta
print(s['mee']); #Meeta
#print(s['b']);  error as b index not exists in s.

