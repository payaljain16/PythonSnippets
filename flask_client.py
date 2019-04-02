import requests;

url="http://localhost:5000";
result = requests.get(url).json();
print(result);
result = requests.post(url).json();
print(result);

url2="http://localhost:5000/abc/";
result2 = requests.get(url2).json();
print(result2);
result2 = requests.post(url2).json();
print(result2);

#url3="http://localhost:5000/cube/5";
url3="http://localhost:5000/cube/";
num=input("Enter no to find cube : ");
url3=url3+num;
result3 = requests.get(url3).json();
print(result3);

