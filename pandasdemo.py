import pandas as pd;

weather_data = {
    'day':['1/3/2019','2/3/2019','3/3/2019','4/3/2019','5/3/2019','6/3/2019','7/3/2019','8/3/2019'],
    'temperature':[25,32,29,35,33,26,28,24],
    'windspeed':[4,9,6,8,3,5,6,5],
    'event':['sunny','raining','snow','spring','sunny','sunny','snow','raining']
    }

df=pd.DataFrame(weather_data);
#print(df);
print(df.shape);  #print(rows,cols) o/p-(8,4)
rows,columns = df.shape;
print("Rows : ",rows);
print("Columns : ",columns);

print(df.day);  #to print only day column
print(df['event']);  #to print event column, only data printed no heading
print(df[['event']]); #use 2 square brackets to print event column with heading

print(df[['event','day']]);   #print multiple cols together

print(df.head()); #to print first 5 records
print(df.tail()); #to print last 5 records

print(df.head()[['day','windspeed']]);  #print only day and event of first 5 data
 
print(df.min()[['temperature']]);
print(df.max()[['temperature']]);
print(df.mean()[['temperature']]);  #average
