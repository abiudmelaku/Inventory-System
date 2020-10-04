import io_Display_Manager
import io_Display_Customer
import Customer
import Item
import Model
import ReadWrite
from sys import argv
ui = io_Display_Manager.io_Display_Manager()
ui_Customer = io_Display_Customer.io_Display_Customer()
cart = Customer.Customer()
crud_data = Model.HashMap(100)

def check_file_path():
    arguments = len(argv)
    if arguments > 0 and arguments == 2:
        file_path = f'{argv[1]}'
        return file_path
    return None
rw = ReadWrite.read_Write(check_file_path())
def respond_to_err():
    argument_err = rw.dir_message
    if argument_err == "failed" or argument_err == "not_csv" or argument_err == "no_dir":
        ui.arg_err_display(argument_err)
        return
    return False
def load_data_to_memory():
    data = rw.load_data_to_memory
    return data

def start_program():
    greeting_responce = ui.greetings()
    if greeting_responce == 1:
        username_password = ui.verify_user();
        manager_exists = rw.search_any_user(username_password[0], username_password[1], "manager")
        manager_exists_responce = ui.accept_or_deny_login_attempt(username_password[0], manager_exists)
        if manager_exists_responce:
            manager_View()
    elif greeting_responce == 2:
        custumer_View()
    elif greeting_responce == 3:
        return ;
    start_program()

def manager_View():
    managers_choice = ui.managers_choices()
    if managers_choice != ValueError:
        handle_managers_choice(managers_choice)


def custumer_View ():
    customer_Choice = ui_Customer.Customer_Choice()
    if customer_Choice != ValueError:
        handle_Customer_Choice(customer_Choice)

def handle_managers_choice(managers_choice):
    if managers_choice == 1:
        add = ui.Add_Cat_item(None ,False)
        if add != ValueError and add != IndexError:
            if  crud_data.create_catagory(add[0] , False) != "cat_exists":
                managers_added_item = Item.baught_item(add[1],add[2],add[3]).set_item()   # Returns a dict with key ,value paris  of the new added item
                item_added_updated = crud_data.item_set_val( add[0] , managers_added_item)
                rw.write_new_item([add[0] , managers_added_item])
                ui.addCatResponce(item_added_updated , None)
            else:
                ui.addCatResponce(None,True)
    elif managers_choice == 2:
        cat_lst = crud_data.get_cat_lst()
        add_item = ui.Add_Cat_item(cat_lst,True)
        if add_item != ValueError and add_item != IndexError and add_item != "no_cat_found":
            managers_bought_item= Item.baught_item(add_item[1],add_item[2],add_item[3]).set_item()
            add_item_responce = crud_data.item_set_val(add_item[0] , managers_bought_item)
            if add_item_responce == "item_added":
                rw.write_new_item([add_item[0], managers_bought_item])
            else:
                rw.update_old_item([add_item[0] , managers_bought_item])
            ui.addCatResponce(add_item_responce ,None)

    elif managers_choice == 3:
        cat_list = crud_data.get_cat_lst()
        edit_cat = ui.edit_cat(cat_list , None)
        if edit_cat != "no_cat_found" and edit_cat != ValueError and edit_cat != IndexError :
            edit_cat_response = crud_data.edit_catagory(edit_cat[0] , edit_cat[1] , edit_cat[2])
            if edit_cat_response == "category_edited":
                rw.edit_cat(edit_cat[0] , edit_cat[2])
                ui.edit_cat(None,True)
            else:
                ui.edit_cat(None,False)
    elif managers_choice == 4:
        cat_list = crud_data.get_cat_lst()
        choosen_cat = ui.edit_item(cat_list , None , None)
        if choosen_cat != "no_cat_found" and choosen_cat != ValueError and choosen_cat != IndexError:
           item_lst =  crud_data.fetch_items(choosen_cat, False)
           new_item_details = ui.edit_item(None , item_lst,None)
           if new_item_details != ValueError and new_item_details != IndexError:
             update_item = Item.baught_item(new_item_details[0] , new_item_details[1] , new_item_details[2]).set_item()
             old_item_name = new_item_details[3]
             edit_item = crud_data.edit_item(choosen_cat,old_item_name,update_item)
             rw.edit_item(choosen_cat,old_item_name,update_item)
             ui.edit_item(None,None,edit_item)
    elif managers_choice == 5:
        search_choice_responce = ui.search_view_display()
        if search_choice_responce != "invalid_choice" and search_choice_responce != ValueError:
            if search_choice_responce == 1:
                search_Cat = ui.search_display(True , None , False ,False)
                if search_Cat:
                    search_result = crud_data.search_cat_only(search_Cat)
                    ui.search_display( False , None, search_result , False)
            elif search_choice_responce == 2:
                search_forItem()
            else:
                cat = ui.view_display(crud_data.get_cat_lst() ,None)
                view_cat = crud_data.get_items_in_cat(cat)
                if view_cat != ValueError and view_cat != IndexError:
                  ui.view_display(None , view_cat)
    elif managers_choice == 6:
        cat_lst = crud_data.get_cat_lst()
        del_Cat = ui.del_Cat(cat_lst , False)
        if del_Cat != ValueError and del_Cat != IndexError and del_Cat != "no_cat_found":
           cat_del_responce =  crud_data.del_cat(del_Cat)
           rw.del_cat(del_Cat)
           ui.del_Cat(None , cat_del_responce)
    elif managers_choice == 7:
        cat_list = crud_data.get_cat_lst()
        cat_name = ui.del_item(cat_list ,None, False)
        if cat_name != ValueError and cat_name != IndexError and cat_name != "no_cat_found":
            del_item_lst = crud_data.fetch_items(cat_name , False)
            item_del = ui.del_item(None , del_item_lst , False)
            if item_del != ValueError and item_del != IndexError and item_del !="no_cat_found":
                item_deleted = crud_data.del_item(cat_name, item_del)
                rw.del_item(cat_name, item_del)
                ui.del_item(None, None, item_deleted)
    else:
        return
    manager_View()

def handle_Customer_Choice(customer_Choice):
    if customer_Choice == 1:
        cat_lst = crud_data.get_cat_lst()
        item_toBuy_fromCat = ui_Customer.buy_items(cat_lst , None,False)
        if item_toBuy_fromCat != ValueError and item_toBuy_fromCat != IndexError and item_toBuy_fromCat != "nothing_found":
            item_lst = crud_data.fetch_items(item_toBuy_fromCat,True)
            item_toBuy = ui_Customer.buy_items(None , item_lst , False) # returns the item name  and the item quantity to be reduced as a tuple
            if item_toBuy != ValueError and item_toBuy != IndexError and item_toBuy != "wrong_Value":
                item_name,item_quantity,item_price = item_toBuy[0],item_toBuy[1],item_toBuy[2]
                item_details = crud_data.search_cat(item_toBuy_fromCat,item_name , False)
                update_quantity = item_details["item_quantity"] - item_quantity
                setupdatedItem = Item.baught_item(item_details["item_name"] , update_quantity , item_details["item_price"]).set_item() # gets the updated  item
                update_item = crud_data.item_set_val(item_toBuy_fromCat,setupdatedItem) #update the item
                if update_item == "item_updated":
                    rw.update_old_item([item_toBuy_fromCat, setupdatedItem]) #update the csv
                    cart.add_to_cart((item_toBuy_fromCat , item_name,item_quantity)) #add to cart
                    cart.add_to_Bill(item_quantity * item_price) #add to bill
                    ui_Customer.buy_items(None,None,True)


    elif customer_Choice == 2:
        baught_items = cart.get_cart()
        item_to_edit = ui_Customer.edit_item(baught_items , None , False)
        if item_to_edit != ValueError and item_to_edit != IndexError and item_to_edit != "noValue":
            cat_name,item_name,customer_baught_amount = item_to_edit[0],item_to_edit[1],item_to_edit[2]
            item_details = crud_data.search_cat(cat_name , item_name, False)
            new_amount = ui_Customer.edit_item((item_name,customer_baught_amount),item_details["item_quantity"] , False)
            if new_amount != ValueError and new_amount != IndexError and new_amount != "wrong_Value":
                item_num,new_quantity_inStock = new_amount[0],new_amount[1]
                diffrence,flag = item_num[0],item_num[1]
                if flag == "substract": # substract in a sence that it is substracting from the inventory and adding on the customers cart.
                    cart.update_cart(cat_name,item_name,diffrence , True) # update customers cart
                    cart.add_to_Bill(item_details["item_price"] * diffrence) # update customers bill
                    updated_item = Item.baught_item(item_name,new_quantity_inStock,item_details["item_price"]).set_item()
                    crud_data.item_set_val(cat_name,updated_item) #updates the item_quantity in the hashmap
                    rw.update_old_item([cat_name,updated_item]) #updates the csv file
                else:
                    cart.update_cart(cat_name, item_name, diffrence, False)  # update customers cart
                    cart.substract_from_Bill(item_details["item_price"] * diffrence) # update customers bill
                    updated_item = Item.baught_item(item_name, new_quantity_inStock,
                                                    item_details["item_price"]).set_item()
                    crud_data.item_set_val(cat_name, updated_item)  # updates the item_quantity in the hashmap
                    rw.update_old_item([cat_name,updated_item]) #updates the csv file
                ui_Customer.edit_item(None,None,True)
    elif customer_Choice == 3:
        '''This option uses the same technique as the  mangers option to search for an item in a category '''
        search_forItem()
    elif customer_Choice == 4:
        customerCart = cart.get_cart()
        bill = cart.get_bill()
        ui_Customer.displayCart(customerCart,bill , True)
    elif customer_Choice == 5:
        customerCart = cart.get_cart()
        del_display =  ui_Customer.displayCart(customerCart,None, False)
        if del_display != ValueError and del_display != IndexError and del_display != "noValue":
            cat_name, item_name, customer_baught_amount = del_display[0], del_display[1], del_display[2]
            item_details = crud_data.search_cat(cat_name, item_name, False) # returns a  dict value  for the searched item
            deletedAmont = cart.delete_fromCart(del_display , item_details["item_price"]) #updates the cart  and returns the baught amount
            newAmount = item_details["item_quantity"] + deletedAmont
            updated_item = Item.baught_item(item_details["item_name"] , newAmount , item_details["item_price"]  ).set_item()
            crud_data.item_set_val(cat_name, updated_item)  # updates the item_quantity in the hashmap
            rw.update_old_item([cat_name, updated_item])  # updates the csv file
            ui_Customer.delete_fromCart()
    else:
        return
    custumer_View()
def search_forItem():
    cat_list = crud_data.get_cat_lst()
    search_item = ui.search_display(False, cat_list, False, False)
    if search_item != ValueError and search_item != IndexError and search_item != "no_cat_found":
        cat_name, item_name = search_item[0], search_item[1]
        search_item_result = crud_data.search_cat(cat_name, item_name, False)
        ui.search_display(False, None, False, search_item_result)

if respond_to_err() == False:
    data = load_data_to_memory()
    if data != None:
        if len(data) > 0:
            for i in data:
                cat,item_details = i
                crud_data.create_catagory(cat,False)
                crud_data.item_set_val(cat,item_details)
    start_program()



