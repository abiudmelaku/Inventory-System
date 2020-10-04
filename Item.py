from abc import ABC , abstractmethod
class item(ABC):
    '''This is an abstract class '''
    def __init__(self ,  name , quantity , price):
        self.name = name;
        self.quantity = quantity;
        self.price = price;

    @ abstractmethod
    def set_item(self):
        '''This is a declarative method ... hence an abstract method  '''
        pass;


class baught_item(item):
    def set_item(self):
        return dict( item_name = self.name , item_quantity = self.quantity, item_price = self.price)



