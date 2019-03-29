import pandas as pd;

#specify where to break columns by ";" can give any.
#also tell what column names heading should be as not present
fd=pd.read_csv("pandas_tutorial_read.csv",delimiter=";",names=['date_time','read/write','country','user_id','d_market','continent']);
#print(fd);
print(fd.head());
print(fd.tail());  #last 5 printed
print(fd.tail(3));  #last 3 printed

print(fd[fd.d_market=="SEO"]);   #print deatils where d_market col has values="SEO"
print(fd[fd.continent=="Asia"]);

print(fd[['country','continent','user_id']]); #print specific cols.
print(fd.head()[['country','continent','user_id']]); #print specific cols but top 5


print(fd.sample(5)[['country','continent','user_id']]); #print randomly 5 rows on these specific cols.
#re run the code, can see different samples everytime.

