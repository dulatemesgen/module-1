"""
Author: Dula Temesgen
program: invoice.py

"""

from customers import Customer
TAX_RATE = 0.06

class Invoice:
    """invoice class"""
    # Constructor
    def __init__(self, invoice_id, customer, item_price={}):
        self.invoice_id = invoice_id
        self.customer = customer
        self.item_price = item_price

    @property
    def invoice_id(self):
        return self.invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        if not isinstance(value, int):
             raise ValueError
        self.invoice_id = value

    @property
    def customer(self):
        return self.customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self.customer = value
        else:
            raise ValueError("Not a Cutomer")

    @property
    def item_price(self):
        return self.item_price

    @item_price.setter
    def item_price(self, value):
        if isinstance(value, dict):
            self.item_price = value
        else:
            raise ValueError("That's not a dictionary")

    def add_item(self, value):
        self.item_price.update(value)

    def creat_invoice(self):
        total = 0.0
        for x in self.item_price:
            total += self.item_price[x]
            print(str(x) + ': ' + str(self.item_price[x]))
        TAX_RATE = total * TAX_RATE
        return ('Tax: {0:.2f}'.format(TAX_RATE))
        return ('Total: {0:.2f}'.format(total + TAX_RATE))

    def display(self):
        return (str(self.customer.customer_id) + "\n" + str(self.customer.first_name) + " " + str(self.customer.last_name) + "\n" + str(self.customer.address) + "\n" +
               self.customer.phone_number)

    def str(self):
        """returns a string of the Invoice object. same as repr()"""
        return self.customer.first_name + ' ' + self.customer.last_name + ', ' + self.customer.phone_number
        

    def repr(self):
        """returns a string of the Invoice object. same as str()"""
        return self.customer.first_name + ' ' + self.customer.last_name + ', ' + self.customer.phone_number
        

# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
