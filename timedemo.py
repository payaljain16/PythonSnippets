import time;
import calendar;

ms=time.time();
print("Milliseconds : ",ms);
print("Current time : ",time.localtime(ms));
print("right time : ",time.asctime(time.localtime(ms)));

print("---------------------");
cal=calendar.month(2019,10);
print(cal);

str="hello eVeryBody";
print(str.center(20,' '));
