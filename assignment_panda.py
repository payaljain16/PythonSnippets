import pandas as pd;

df=pd.read_csv("assign1.csv",delimiter=',',names=['id','name','age','salary','designation','dept','project_id','project_name','manager','city','state']);
print(df);
#print(df[['id','name','designation']]);

#replacing NA in dataframe 
df["designation"].fillna("Employee", inplace = True);
print(df[['id','name','designation']]);

print("Eldest Employee : ");
max_age=df.max()['age'];
print(df.loc()[df['age']== max_age]);

##print("---------------------------");
##print("Youngest Employee : ");
##min_age=df.min()['age'];
##print(df.loc()[df['age'] == min_age]);

print("---------------------------");
print("Youngest Employee : ");
print(df[df.age == df.age.min()]);


print("---------------------------");
print("Second highest paid employee : ");
res=(df['salary'].nlargest(2));
print(res.iloc[1]);

print("---------------------------");
print("Cost department wise : ");
grouped=df.groupby(['dept']);
print (grouped[['salary']].sum());

print("---------------------------");
print("Cost project wise : ");
grouped=df.groupby(['project_name']);
print (grouped[['salary']].sum());

print("---------------------------");
print("Employees List Based On Manager : ");
mname=input("Enter the manager name to display employees under him : ");
grouped=df.groupby(['manager']);
print(grouped.get_group(mname));

print("---------------------------");
print("Employee by ID : ");
eid=int(input("Enter the employee id to be searched : "));
print(df[df.id == eid]);

print("---------------------------");
print("Average age department wise : ");
grouped=df.groupby(['dept']);
print (grouped[['age']].mean());

##z=df.groupby(['dept'])['age'].mean();
##mini=z.min();
##maxx=z.max();
##print("The min. of average of departmental age is : ",mini,"\n The max. of average of dept age is : ",maxx);
##if mini < 35 :
##    print("Youngest Employees Team.");
##else:
##    print("All are elder teams.");



z=df.groupby(['dept'])['age'].mean();
for i in z:
    #print(i);
    if i < 35 :
        print("Youngest Employees Team.");
    else:
        print("Eldest Employees Team.");


##
##eldest
##youngest
##2nd highest paid
##cost dept wise
##cost proj wise
##employees list based on manager name entered
##search emp by id

#replace desig - comes NA - replace by default - "Employee"
#avg age of dept- if below 35 youngest team else eldest
