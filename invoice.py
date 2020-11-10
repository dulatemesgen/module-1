from customers import Customer
TAX_RATE = 0.06

class Invoice:
    """invoice class"""
    def __init__(self, invoice_id, customer, item_price_dict={}):
        self.invoice_id = invoice_id
        self.customer = customer
        self.items_price_dict = item_price_dict

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
    def item_price_dict(self):
        return self.item_price_dict

    @item_price_dict.setter
    def item_price_dict(self, value):
        if isinstance(value, dict):
            self.item_price_dict = value
        else:
            raise ValueError("That's not a dictionary")

    def add_item(self, dict):
        self.items_price_dict
        # print(self.items_price_dict)

    def creat_invoice(self):
        sub_total = 0
        receipt = self.customer.display() + '\n'
        for key, value in self.items_price_dict()
            sub_total += value
            receipt += '{}........{:.2f\n'.format(key,value)
        tax = sub_total * TAX_RATE
        receipt += "Tax........{:.2f}\n".format(tax)
        receipt += "Tax........{:.2f}\n".format(total)
        return receipt

# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
