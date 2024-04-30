class Menu_Items:

    def __init__(self,name,description,price,category):
        self.name=name
        self.description=description
        self.price=price
        self.category=category

    def get_name(self):
        return self.name

    def get_price(self):
        return  self.price



class Orders:

    def __init__(self,order_id):
        self.order_id=order_id
        self.menu_item=[]

    def get_order_id(self):
        return self.order_id

    def add_item(self,menu_item,):
        self.menu_item.append(menu_item)

    def remove_item(self,menu_item):
        self.menu_item.remove(menu_item)

    def get_total_price(self):
        total_price=0
        for item in self.menu_item:
            total_price += item.get_price()
        return total_price


class Billing_Process:

    def __init__(self,tax_rate):
        self.tax_rate=tax_rate
