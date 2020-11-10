"""
Author: Dula Temesgen
program: students.py
creating class for customer
"""
class Customer:
    """Customer class"""
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        print("Setting the customer id")
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address


    @property
    def customer_id(self):
        return self.customer_id

    @customer_id.setter
    def customer_id(self, value):
        print("Set the customer id")
        if isinstance(value, int):
            self.customer_id = value
        else:
            raise AttributeError("\'Customer\' object has no attribute \'cid\'")

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, value):
        self.last_name = value

    @@property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self.first_name = value

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.phone_number = value

    @property
    def address(self):
        return self.address


    @phone_number.setter
    def address(self, value):
        self.address = value

    def display(self):
        return f"Customer: {self.customer_id},\nName: {self.first_name} {self.last_name}\nAddress:                                    400 E york st., Miami, FL 30234\nPhone Number: {self.phone_number}"

"""
customer_2 = (cid, "Temesgen", "Dula", "515-100-2003", "909 Robert D. Ray Dr, Des Moines, IA 50309")
print(customer_1.display())
"""