import pickle;
from Personn import Personn; 

p1=Personn("Sujatha",25);

f1=open("person.ser","wb");  #bytestream, thus wb-binary format
pickle.dump(p1,f1);
f1.close();

print("Pickled successfully...");