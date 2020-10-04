import io_Display_Manager
man_display = io_Display_Manager.io_Display_Manager()
class io_Display_Customer:
    def Customer_Choice(self):
        try:
            print("Hello our valued Customer ! ")
            print("Do you want to Buy items? (Press 1)")
            print("Do you want to Edit  items ? (Press 2)")
            print("Do you want to Search items ? (Press 3)")
            print("Do you want to View your cart? (Press 4)")
            print("Do you want to Delete  items ? (Press 5)")
            print("Press any other number to exit ")
            customer_responce = int(input("---> "))
            if customer_responce < 1 and customer_responce > 5:
                int("Raise an error ")
            return customer_responce
        except ValueError:
            man_display.unknown_value_err_display()
            return ValueError
    def buy_items(self,cat_lst,item_lst , item_baught):
        try:
            if item_baught:
                man_display.add_spacing()
                print("                Your item has been added to your cart")
                man_display.add_spacing()
                return
            if cat_lst != None:
                if len(cat_lst) > 0:
                    man_display.display_lst(cat_lst)
                    buy_from_cat = int(input("From which category do you want to Buy : ")) - 1
                    return cat_lst[buy_from_cat]
                else:
                    return man_display.nothing_to_display()
            elif item_lst !=None:
                if len(item_lst) > 0:
                    counter = 1
                    for i in item_lst:
                        item_name, item_left_inStock,item_pirce = i
                        print(f"   {counter})   {item_name[0].upper() + item_name[1:]}             Item Left = {item_left_inStock}")
                        counter += 1
                    buy_from_cat = int(input("Which item do you want to Buy : ")) - 1
                    item_toBuy = item_lst[buy_from_cat]
                    item_name, item_left_inStock, item_pirce = item_toBuy[0],item_toBuy[1],item_toBuy[2]
                    item_qunatity = int(input(f"How many {item_name} do you want to buy ? "))
                    if item_qunatity > 0:
                        if item_left_inStock - item_qunatity < 0:
                            self.amount_exeeds()
                            return "wrong_Value"
                        return (item_name, item_qunatity, item_pirce)
                    else:
                        self.more_thanZerow()
                        return  "wrong_Value"
                else:
                    return man_display.nothing_to_display()
        except ValueError:
            man_display.unknown_value_err_display()
            return ValueError
        except IndexError:
            man_display.unknown_value_err_display()
            return IndexError


    def displayCart(self, cart,bill,displayOnly):
        try:

            if len(cart) > 0:
                man_display.add_spacing()
                print("    Category            Item                   Amount ")
                print("___________________________________________________________")
                counter = 1
                for i in cart:
                    cat_name, item_name, item_amount = i
                    print(f"{counter})  {cat_name[0].upper() + cat_name[1:]}    {item_name[0].upper() + item_name[1:]}               {item_amount}")
                    counter += 1
                man_display.add_spacing()
                if not displayOnly:
                    edit_item = int(input("Which item do you want to edit or delete ? ")) - 1
                    return cart[edit_item]# returns the whole row of the item
                else:
                    print(bill)
            else:
                man_display.nothing_to_display()
                man_display.add_spacing()
                return "noValue"
        except ValueError:
            man_display.unknown_value_err_display()
            return ValueError;
        except IndexError:
            man_display.unknown_value_err_display()
            return IndexError;



    def edit_item(self , baught_item , item_qunatity , edited):
        try:
            if edited:
                man_display.add_spacing()
                print("                Your Item has been edited Successfully !!!")
                man_display.add_spacing()
                return
            elif item_qunatity:
                item_name,customer_baught_amount = baught_item[0] , baught_item[1]
                amount = int(input(f"What should be the new amount of {item_name} ? "))
                if amount > 0:
                    if amount > customer_baught_amount:
                        #Greater (Added to cart substract from inventory)
                        new_amount = amount - customer_baught_amount
                        check_item_isAvailable = item_qunatity - new_amount
                        if check_item_isAvailable < 0:
                            self.amount_exeeds()
                            return "wrong_Value"
                        return  ((new_amount,"substract") , check_item_isAvailable)
                    elif amount < customer_baught_amount:
                        # less than (Substracted from cart Added  to inventory)
                        new_amount = customer_baught_amount - amount
                        new_quantity_inStock = item_qunatity + new_amount
                        return ((new_amount,"add") ,new_quantity_inStock)
                else:
                    self.more_thanZerow()
                    return "wrong_Value"
            else:
                return (self.displayCart(baught_item,None, False))
        except ValueError:
            man_display.unknown_value_err_display()
            return ValueError
        except IndexError:
            man_display.unknown_value_err_display()
            return IndexError
    def amount_exeeds(self):
        man_display.add_spacing()
        print("                Amount exceeds the  item found in stock!!! Please enter a lower amount")
        man_display.add_spacing()
    def delete_fromCart(self):
        man_display.add_spacing()
        print("                Item has been deleted successfully !!! ")
        man_display.add_spacing()
    def more_thanZerow(self):
        man_display.add_spacing()
        print("                Please enter a number bigger than 0 !!")
        man_display.add_spacing()








