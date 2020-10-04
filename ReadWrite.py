import os
import ast
from csv import reader,writer

class read_Write:
    def __init__(self , path):
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) # get's the current full path of the directory where this python file is found .
        self.dir_message = None
        self.load_data_to_memory = None
        if path != None:
            path_valid = self.validate_file_path(path) # examines the specified path by the user
            if path_valid == "no_dir" or path_valid == "not_csv" or path_valid == "failed":
                self.dir_message = path_valid
            else:
                self.inventory_file_path = path
        else:
            self.inventory_file_path = self.dir_path+"\\inventory.csv"
            if not os.path.isfile(self.inventory_file_path ):  # check if the csv file exists
                self.create_inventory_file(self.inventory_file_path)
    def validate_file_path(self, path):
        try:
            dir = self.find_dir(path)  # returns the dir path and file name as a tuple or returns failed
            if dir != "failed":
                dir_path, file_name = dir[0] , dir[1]
                if os.path.exists(dir_path): # check if the directory exists
                    if file_name.lower().endswith(".csv"):#check if the file extention ends with .csv
                        if os.path.isfile(path): # check if the csv file exists
                            read_data = self.read(path)
                            if len(read_data) > 0:
                                '''load data to memory '''
                                loading_data = []
                                for i in read_data:
                                    category = i[0]
                                    item_details = ast.literal_eval(i[1])  #Safely evaluate an expression node or a string containing a Python  expression.
                                    # (i.e in this case changes the string dict format to a dict type  )
                                    loading_data.append((category,item_details))
                                    self.load_data_to_memory = loading_data
                            return
                        else:
                            self.create_inventory_file(path)
                            return
                    else:return "not_csv"
                else:return "no_dir"
            return "failed"
        except Exception:
            '''The following happens usually when file name  is not correct '''
            return "failed"

    def find_dir(self, path):
        try:
            reversed_path = path[::-1]
            for index, i in enumerate(reversed_path):
                if i == "\\":
                    break;
            csvFile_name = reversed_path[:index]
            new_idx = index + 1
            dir_reversed = reversed_path[new_idx:]
            return (dir_reversed[::-1], csvFile_name[::-1])
        except Exception:
            '''The following happens usually when the path format is not correct '''
            return "failed"
    def create_inventory_file(self , path):
        with open(path, "a",newline=''
                  ) as file:  # checks if the file name is valid by creating the file
            w = writer(file,lineterminator = '\n')
            w.writerow(["Category,item_details"])

    def read(self , file_path ):
        with open(file_path) as file:  # checks if the file name is valid by creating the file
            f = reader(file)
            next(f)
            lst_data =  list(f)
        return lst_data
    def write_new_item(self ,   data ): # the data param contains the cat_name and item details
        with(open(self.inventory_file_path , 'a' , newline='')) as file:
            w = writer(file)
            w.writerow(data)
    def update_old_item(self ,  data):
        read_data = self.read(self.inventory_file_path)
        for index, i in enumerate(read_data):
            category = i[0]
            item_detail = ast.literal_eval(i[1])
            if category == data[0] and item_detail['item_name'] == data[1]['item_name']:
                break;
        read_data.pop(index)
        read_data.append(data)
        self.write_data(read_data)

    def edit_cat(self , old_cat_name , new_cat_name):
        read_data = self.read(self.inventory_file_path)
        new_data = []
        for index , i  in enumerate(read_data):
            category = i[0]
            item_details = i[1]
            if category == old_cat_name:
                new_data.append([new_cat_name ,item_details])
            else:
                new_data.append(i)
            self.write_data(new_data)

    def edit_item(self , cat_name , old_item_name , data):
        read_data = self.read(self.inventory_file_path)
        for index , i in enumerate(read_data):
            category = i [0]
            item_details = ast.literal_eval(i[1])
            if cat_name == category and old_item_name == item_details["item_name"]:
                break;
        read_data.pop(index)
        read_data.append([cat_name,data])
        self.write_data(read_data)
    def del_cat(self , cat_name):
        read_data = self.read(self.inventory_file_path)
        new_data = []
        for i in read_data:
            category = i[0]
            if cat_name != category:
                new_data.append(i)
        self.write_data(new_data)
    def del_item(self , cat_name , item_name):
        read_data = self.read(self.inventory_file_path)
        new_data = []
        for i in read_data:
            category = i[0]
            item_detail = ast.literal_eval(i[1])
            if cat_name == category and item_detail['item_name'] == item_name: pass;
            else:new_data.append(i)
        self.write_data(new_data)



    def write_data(self , data):
        with open(self.inventory_file_path, 'w', newline='') as file:
            w = writer(file, lineterminator='\n')
            w.writerow(["Category,item_details"])
            for i in data:
                w.writerow(i)

    def search_any_user(self, username , password , who_is_calling):
        user_found = False
        with open(self.dir_path + '\\uspw.csv' , "r") as file:
            us_pw = reader(file)
            if who_is_calling == "manager":
                for i in us_pw:
                    if i[0] == username.lower() and i[1] == password and i[2] == "manager":
                        user_found = True
                        break
            else:
                for i in us_pw:
                    if i[0] == username.lower() and i[1] == password and i[2] == "customer":
                        user_found = True
                        break
        if user_found: return True
        return False