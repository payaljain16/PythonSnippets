class Emp:
    def __init__(self,name,age,state,city,pin):
        self.name=name;
        self.age=age;
        self.addr=Address(state,city,pin);
        self.computer=self.Computer("HP","FS01343","pentium i5","2GHz", "8GB");
        
    def display(self):
        print("Name : ",self.name);
        print("Age : ",self.age);
        self.addr.display();
        self.computer.display();
                            #association - has a relationship
    class Computer :
        def __init__(self,brand,model,processor,speed,ram):
            self.brand=brand;
            self.model=model;
            self.processor=processor;
            self.speed=speed;
            self.ram=ram;

        def display(self):
            print("Company : ",self.brand);
            print("Model : ", self.model);
            print("Processor : ", self.processor);
            print("Speed : ", self.speed);
            print("Ram : ", self.ram);

class Address:
    def __init__(self,state,city,pin):
        self.state=state;
        self.city=city;
        self.pin=pin;

    def display(self):
        print("State : ",self.state);
        print("City : ",self.city);
        print("Pin : ",self.pin);        



        
e1=Emp("Payal",22,"Uttar Pradesh","Kanpur",208022);
e1.display();

a1=Address("MP","Panchmarhi",2545454);
a1.display();
