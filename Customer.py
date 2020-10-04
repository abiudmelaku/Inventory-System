class Customer:
    def __init__(self):
        self.__baughtItems = []
        self.__bill = 0
    def get_cart(self):
        return self.__baughtItems
    def get_bill(self):
        return f"Your current bill is ${round(self.__bill , 2)}";
    def add_to_cart(self , item):
        self.__baughtItems.append(item)
    def add_to_Bill(self , bill):
        self.__bill += bill
    def substract_from_Bill(self, bill):
         self.__bill -= bill
    def update_cart(self,catName,itemName,diffrence,add):
        newAmount = None
        if add:
            for index , i in enumerate(self.__baughtItems):
                cat_name, item_name, item_amount = i
                if cat_name == catName and item_name == itemName:
                    newAmount = item_amount
                    break;
            newAmount += diffrence
            self.__baughtItems.pop(index)
            self.__baughtItems.append((cat_name, item_name, newAmount))
        else:
            for index, i in enumerate(self.__baughtItems):
                cat_name, item_name, item_amount = i
                if cat_name == catName and item_name == itemName:
                    newAmount = item_amount
                    break;
            newAmount -= diffrence
            self.__baughtItems.pop(index)
            self.__baughtItems.append((cat_name, item_name, newAmount))
    def delete_fromCart(self , item , price):
        catName,itemName,itemAmount = item[0],item[1],item[2]
        for index , i in enumerate(self.__baughtItems):
            cat_name, item_name, item_amount = i
            if cat_name == catName and item_name == itemName:
                break;
        self.substract_from_Bill(itemAmount * price) # Subtracts from bill
        self.__baughtItems.pop(index) # deletes from cart
        return item_amount




