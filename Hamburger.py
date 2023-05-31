# hamburger_doordash
# IS 303 Group Project
#Hailey Bronson, Nate Sibbett, Harrison Stone, Caleb Barlow, Claire Woodman
#Hamburger Door Dash
#this program tracks exactly how many hamburgers each customer eats

import random 

#Create an Order class
class Order(): 
    #Create a constructor that defines 
    # an instance variable called burger_count
    def __init__(self):
        self.burger_count = self.randomBurgers()

    #Create a method called randomBurgers 
    # that returns a number between 1 and 20
    def randomBurgers(self):
        return random.randint(1, 20)
    
    #The constructor should call the randomBurgers() method and assign the return
    #value to the burger_count instance variable

#Create a Person class
class Person(): 
        #Create a constructor that defines 
        # an instance variable called customer_name
        def __init__(self):
            self.customer_name = self.randomName()

        def randomName(self): 
            #Make changes to customer list here
            asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", 
                       "Dusty Bottoms", "Harry Flugleman", "Carmen", 
                       "Invisible Swordsman", "Singing Bush"]
            return random.choice(asCustomers)
        #This method randomly returns one of the 9 names when called
        #The Person constructor should call the randomName() method and assign the
        #return value (a random name) to the customer_name instance variable
    
#Create a Customer class that inherits from the Person class
class Customer(Person):
    #Create a constructor that calls the parent constructor
    def __init__(self):
        super().__init__()
        #Create an instance variable called order in the 
        #constructor that is assigned an order object
        self.order = Order()

    #Create a variable for a Queue that will be assigned 
    #items of type Customer

#working outside of the realm of the classes we instantiated so define method main 
def main():
    Customerqueue = []
    #This variable will represent your line of customers (objects) waiting outside to
    #place their hamburger orders

    #Create a variable for a Dictionary with keys of type string and values of type int.
    Customerdict = {}
    #This variable will hold information about each customer

    #Put 100 customers into the queue. Each customer object will already have a random
    #number of burgers for each order
    for customer in range(100):
        #by referencing the entire class, it will reference the class, then the super() function, and then grab 
        #the customer name and burger count, ultimately creating objects as it goes 
        Customerqueue.append(Customer())
        
    for customer in Customerqueue: 
        if customer.customer_name in Customerdict: 
            Customerdict[customer.customer_name] += customer.order.burger_count
        else: 
            Customerdict[customer.customer_name] = customer.order.burger_count 


    #create new dict that is sorted by referancing and manipulating current dictionary 
    SortedDict = sorted(Customerdict.items(), key = lambda item : item[1], reverse = True)
    # Print out each customer and their total burgers ordered sorted by the most number of
    # burgers ordered
    for customer in SortedDict:

        customer_name = customer[0]
        total_burgers = customer[1]
        formatted_name = customer_name.ljust(19)

        print(f"{formatted_name}     {total_burgers}")


#calling main to have it run       
main()
