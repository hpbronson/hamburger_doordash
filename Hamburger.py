#my own version of the group project in order to understand 
import random 
from collections import deque

class Order: 

    def __init__(self, burgerCount):
        self.burger_count = int(burgerCount)
        self.randomBurgers(burgerCount)

    #TA: declare separate variable? or mention method  
    def randomBurgers(self):
        #keep method now that we have declared the variable? 
        self.burgerCount = random.randint(0, 20)

class Person: 
    def __init__(self, sName):
        self.customer_name = sName 

# THE PERSON constructor should call the randomName() 
# method and assign the return value (a random name) to the 
# customer_name instance variable
        self.randomName(sName)

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", 
                       "Dusty Bottoms", "Harry Flugleman", "Carmen", 
                       "Invisible Swordsman", "Singing Bush"]
        #returns random name from list
        self.sName = random.choice(asCustomers)
        

#parent: Person child: Customer 
class Customer(Person):
    #do i need to put class in parameter/argument ?
    def __init__(self, sName):
        super().__init__(sName)
        self.Order = oOrder 
        self.dictCustomers = {}

 #CREATE a variable for a Queue that will 
    # be assigned items of type Customer 
        self.queueCustomer = ()

    def add_to_queue(line): 
        #TA: for loop to add 100 customers into the queue? 
        # is there another way to add Customers? ("Customer 1", "Customer 2")
        # append() function to push item at top of the stack

        queueCustomers.append("Customer 1") 
        queueCustomers.append("Customer 2")
        queueCustomers.append("Customer 3")
        queueCustomers.append("Customer 4")
            
        
        #Start at the bottom element or the First one (oldest) added
        for iCount in range(0, len(queueCustomers)) :
            print(queueCustomers[iCount])
        
        #The FIRST one added will be the FIRST one out
        for iCount in range(1, len(queueCustomers) + 1) :
            queueCustomers.popleft()
        
            for iCount in range(0, len(queueCustomers)) :
                print(queueCustomers[iCount])
        
        print("\nThere are no more customers to help")  



    #input for the dictionary 
        for customer in queueCustomers:
            Customer.dictCustomers[Person.customer_name] = Order.burger_count

        if Person.customer_name not in Customer.dictCustomers:
            Customer.dictCustomers[Person.customer_name] = Order.burger_count
        else:
            #FIGURE OUT
            Customer.dictCustomers[Person.customer_name] = Order.burger_count


oOrder = Order("")
oCustomer = Customer("")
queueCustomers = deque()

#returning sorted list of customers from the dictionary 
listSortedCustomers = sorted(Customer.dictCustomers.items(), key=lambda x: x[1], reverse=True)

#NOW display the customer name and the total number of burgers consumed. 
# Do this using a for loop displaying the contents of the list in positions 0 and 1. 

#MAKE the customer name an even sized value using the ljust() function with the value of 
#19 as the parameter like customer[0].ljust(19) where customer is each list item object in the for loop.
