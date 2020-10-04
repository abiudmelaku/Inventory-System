class io_Display_Manager:

    def greetings(self):
        try:
            print("                             W e l l c  o m e  T o                                  ")
            print("                     M e t r o p o l i t a n D e l i + C a f e  ")
            print(" ")
            print("Enter as Manager ? (Press 1)")
            print("Enter as a Customer ? (Press 2)")
            print("Exit ? (Press 3)")
            user_responce = int(input("---> "))
            if user_responce < 1 or  user_responce > 3:
                int("Raise an error ")
            return user_responce
        except ValueError:
            self.unknown_value_err_display()
            return ValueError

    def arg_err_display(self , argument_err):
        if argument_err == "failed":
            self.add_spacing()
            print("                Please Enter a correct directory and a filename")
            self.add_spacing()
        elif argument_err == "not_csv":
            self.add_spacing()
            print("                File extension is not csv ")
            self.add_spacing()
        elif argument_err == "no_dir":
            self.add_spacing()
            print("                There is no directory within the specified path ")
            self.add_spacing()

    def verify_user(self):
        username =  input("Username :")
        password =  input("Password :")
        return (self.replace_spacing(username.lower()),self.replace_spacing(password))

    def accept_or_deny_login_attempt(self,usename , user_exists):
        if user_exists == True:
            print(f"         Hello {usename.upper()}                                   ")
            return True
        else:
            self.add_spacing()
            print("                Wrong username/password please try again  !!!")
            self.add_spacing()
            return False

    def managers_choices(self):
        try:
            print("What do you want to do today .... ? ")
            print("Add a category ? (Press 1) ")
            print("Add an item in a category  ? (Press 2) ")
            print("Edit a category ? (Press 3) ")
            print("Edit an item in a category ? (Press 4) ")
            print("View or  search  category ? (Press 5) ")
            print("Delete  a category ? (Press 6) ")
            print("Delete  an item in a category ? (Press 7) ")
            print("Press any number to exit")
            man_choice =  int(input(("-------------> ")))
            if man_choice < 1 :
                int("Raise an error ")
            return man_choice
        except ValueError:
            self.unknown_value_err_display()
            return ValueError
    def addCatResponce(self , added_responce , cat_exists):
        if added_responce == "item_added":
            self.add_spacing()
            print("                Your Category and item has be added successfully  !!!")
            self.add_spacing()
            return
        elif added_responce == "item_updated":
            self.add_spacing()
            print("                The item already exists !!!!")
            print("                And now has been updated by the new values  provided !!! ")
            self.add_spacing()
            return
        elif cat_exists == True:
            self.add_spacing()
            print('                Category already exists Please enter a different category name !!!')
            self.add_spacing()
            return
    def Add_Cat_item(self ,cat_list ,add_item_only):
        try:
               if add_item_only:
                   if len(cat_list) > 0:
                       self.display_lst(cat_list)
                       choose_cat = int(input("Where do you want to put the item ? ")) - 1
                       item_details = self.ask_item_details()
                       if item_details != ValueError and item_details != IndexError:
                           return (cat_list[choose_cat], item_details[0], int(item_details[1]), float(item_details[2]))
                       else: return item_details
                   else:
                       self.manager_nothing_to_display()
                       return "no_cat_found"
               else:
                   cat_name = input("What's the name of the category ? : ")
                   item_details = self.ask_item_details()
                   if item_details != ValueError and item_details != IndexError:
                       return (self.replace_spacing(cat_name).lower(), item_details[0], int(item_details[1]), float(item_details[2]))
                   else: return item_details
        except ValueError :
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError
    def ask_item_details(self):
        try:
            item_name = input("What's the new  name of the item ? : ")
            item_quantity = int( input(f"What's the new quantity  of {item_name}  ? : "))
            item_price = float(input(f"What's the new  price   of {item_name}  ? : "))
            return [self.replace_spacing(item_name.lower()), item_quantity, item_price]
        except ValueError :
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError


    def edit_cat(self , cat_list , edited):
        try:
            if edited == True:
                self.add_spacing()
                print ("                Category Edited !!!!!")
                self.add_spacing()
            elif edited == False:
                self.add_spacing()
                print("                A category with a Similar name already exists ! Please use a different Name !!")
                self.add_spacing()
            else:
                if len(cat_list) > 0:
                    self.display_lst(cat_list)
                    edit_index  = int(input("Which category do you want to edit : "  )) -1
                    new_cat_name = input("What should be the new name of the category ? : ")

                    '''check if the chosen category index exists if not it will throw an index error  '''
                    return ( cat_list[edit_index], edit_index  , self.replace_spacing(new_cat_name.lower()))
                else:
                    self.manager_nothing_to_display()
            return "no_cat_found"
        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError
    def edit_item(self,cat_list , item_lst , edited_responce):
        if edited_responce == "Item_already_exists":
            self.add_spacing()
            print("                This Item already exists Please enter a different  name for the editing Item !!")
            self.add_spacing()
            return
        elif edited_responce == "item_edited":
            self.add_spacing()
            print("                Item has been edited successfully !!!")
            self.add_spacing()
            return
        try:
            if item_lst != None:
                if  len(item_lst) > 0:
                    self.display_lst(item_lst)
                    item_index = int(input("Which item do you want to edit ? : ")) - 1
                    new_item_details = self.ask_item_details()
                    if new_item_details != ValueError and new_item_details != IndexError:
                        new_item_details.append(item_lst[item_index])
                    return new_item_details
                else:
                    self.manager_nothing_to_display()
            elif cat_list!= None:
                if len(cat_list) > 0:
                    self.display_lst(cat_list)
                    edit_index = int(input("From which category do you want to edit an item : ")) - 1
                    return (cat_list[edit_index])
                else:
                    self.manager_nothing_to_display()
            else:
                self.manager_nothing_to_display()

            return "no_cat_found"

        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError

    def search_view_display (self):
        try:
            print("Search a category (Press 1) ")
            print("Search an item in a category  (Press 2) ")
            print("View item's  (Press 3) ")
            choice  =  int(input("--- > "))
            if choice > 0 and choice < 4:
                return choice
            else:
                self.unknown_value_err_display()
                return "invalid_choice"
        except ValueError:
            self.unknown_value_err_display()
            return ValueError
    def search_display(self ,search ,  cat_list , cat_found  , item_found):
        try:
           if search:
               cat_search = input("Search For ?  : ")
               return cat_search
           elif cat_list != None:
               if len(cat_list) > 0:
                   self.display_lst(cat_list)
                   search_in_cat = int(input("From which category do you want to search an item : ")) - 1
                   search_item = input("Search Item ? : ")
                   return (cat_list[search_in_cat] , self.replace_spacing(search_item.lower()))
               else:
                   self.add_spacing()
                   print("                Sorry but there is nothing in the inventory to  search !")
                   self.add_spacing()
                   return  "no_cat_found"

           elif  item_found != False:
               self.add_spacing()
               print("              Item                   Amount                        price  ")
               print("          __________________________________________________________________")
               print(f"                  {item_found['item_name']}                        {item_found['item_quantity']}           {item_found['item_price']}")
               self.add_spacing()
           elif cat_found:
               self.add_spacing()
               print("                Category is found !!!!!")
               self.add_spacing()
           else:
               self.searchMessage()
           return
        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError

    def view_display(self , cat_list , items_to_view):
        try:
            if cat_list != None:
                if len(cat_list) > 0 :
                    counter = 1
                    for i in cat_list:
                        print(f"   {counter})   {i[0].upper() + i[1:]}")
                        counter += 1
                    view_in_cat = int(input("From which category do you want to view an item : ")) - 1
                    '''check if the chosen category index exists if not it will throw an index error  '''
                    return cat_list[view_in_cat]
                else:
                    self.manager_nothing_to_display()
            elif items_to_view != None:
                if len(items_to_view) > 0 :
                    self.add_spacing()
                    counter = 1
                    print("    Name                  Quantity                   Price")
                    print("___________________________________________________________")
                    for i in items_to_view:
                        print(f" {counter}) {i['item_name'][0].upper() + i['item_name'][1:]}                    {i['item_quantity']}                          {i['item_price']}")
                        counter += 1
                    self.add_spacing()
                else:
                    self.manager_nothing_to_display()
        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError
    def del_Cat(self , cat_lst , deleted):
        try:
            if deleted:
                self.add_spacing()
                print("                Category deleted !!!")
                return

            elif len(cat_lst) > 0:
                self.display_lst(cat_lst)
                del_cat = int(input("Which category do you want to delete ? ")) -1
                '''check if the chosen category index exists if not it will throw an index error  '''
                cat_lst[del_cat]
                return cat_lst[del_cat]
            else:
                self.manager_nothing_to_display()
            return "no_cat_found"



        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError
    def del_item(self , cat_list ,item_list ,  deleted):
        try:
            if deleted:
                self.add_spacing()
                print("                Item Deleted!!!")
            elif item_list != None:
                if len(item_list) > 0:
                    counter = 1
                    self.display_lst(item_list)
                    del_item = int(input("Which item do you want to  delete ? ")) -1

                    item_list[del_item]
                    return item_list[del_item]
                else:
                    self.manager_nothing_to_display()

            elif len(cat_list) > 0:
                self.display_lst(cat_list)
                cat_name = int(input("From which category do you want to delete an item ? ")) -1
                return cat_list[cat_name]
            else:
                self.manager_nothing_to_display()
            return "no_cat_found"

        except ValueError:
            self.unknown_value_err_display()
            return ValueError
        except IndexError:
            self.unknown_value_err_display()
            return IndexError
    def replace_spacing(self , strinput):
        return strinput.replace(" " , "")
    def unknown_value_err_display(self):
        self.add_spacing()
        print("                Please enter a correct number from the given choice !!!                                                 ")
        self.add_spacing()

    def nothing_to_display(self):
        self.add_spacing()
        print("                Sorry but there is  nothing to display !!")
        self.add_spacing()
        return "nothing_found"
    def manager_nothing_to_display(self):
        self.add_spacing()
        print("                There's Nothing in the Inventory to Display !!! Please enter items ")
        self.add_spacing()
    def searchMessage(self):
        self.add_spacing()
        print("                Sorry nothing is found by the specified input  !!!")
        self.add_spacing()
    def display_lst(self , lst):
        counter = 1
        for i in lst:
            print(f"   {counter})   {i[0].upper() + i[1:]}")
            counter += 1

    def add_spacing(self):
        print(" ")
        print(" ")
        print(" ")




