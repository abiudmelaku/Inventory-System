from csv import writer, DictWriter, reader, DictReader
import ReadWrite
import os

class HashMap:
    def __init__(self, size ):
        self.size = size;
        self.cat_hash_table = self.create_buckets(self.size)
        self.__cat_lst = []

    '''                                          Storing , Reading , Searching , and Editing  values functions                                                 '''

    def create_buckets(self, num):
            return [[] for _ in range(num)]

    def create_catagory(self, cat_key , del_cat_func_calling):
        cat_found = False
        cat_index = self.find_index(cat_key, "cat")
        for index, i in enumerate(self.cat_hash_table[cat_index]):
            record_key, record_value = i
            if (record_key == cat_key):
                cat_found = True;
                break;
        if cat_found:
            if del_cat_func_calling:
                return  (cat_index,index);
            return "cat_exists"
        else:
            self.cat_hash_table[cat_index].append((cat_key, self.create_buckets(80)))
            self.__cat_lst.append(cat_key)
            sorted(self.__cat_lst)

    def edit_catagory(self , cat_name,cat_index_in_lst , new_cat_name):
        old_cat_found = False
        old_cat_index = self.find_index(cat_name, "cat")
        new_cat_index  = self.find_index(new_cat_name,"cat")
        for index , i in enumerate(self.cat_hash_table[new_cat_index]): # check to see if the category already exists
            record_key,record_value = i
            if record_key == cat_name:
                return "cat_found"

        for index_2, i in enumerate(self.cat_hash_table[old_cat_index]): # find the index of the tuple
            record_key, record_value = i
            if (record_key == cat_name):
                old_cat_found = True
                break;
        if old_cat_found:
            edited_name = list(self.cat_hash_table[old_cat_index][index_2]) # This is the tuple converted to a list .
            edited_name[0] = new_cat_name # change the name of the old category to the new one
            self.cat_hash_table[new_cat_index].append(tuple(edited_name)) #append the tuple to the new index
            self.cat_hash_table[old_cat_index].pop(index_2) # delete the tuple found in the old category
            self.__cat_lst[cat_index_in_lst] = new_cat_name # update the list
            sorted(self.__cat_lst)
        return "category_edited"

    def fetch_items(self ,cat_name,customer_calling):
        item_lst = []
        cat_found = False
        cat_index = self.find_index(cat_name, "cat")
        for index ,i in enumerate (self.cat_hash_table[cat_index]):
            record_key , record_value = i ;
            if record_key == cat_name:
                cat_found = True
                break;
        if cat_found:
            if customer_calling:
                for i in self.cat_hash_table[cat_index][index][1]:
                    if len(i) > 0:
                        for j in i:
                            item_lst.append([j[1]["item_name"],j[1]["item_quantity"] , j[1]["item_price"] ])
            else:
                for i in self.cat_hash_table[cat_index][index][1]:
                    if len(i) > 0:
                        for j in i:
                            item_lst.append(j[1]["item_name"])

        return item_lst
    def item_set_val(self,key , item_details):
        item_found = False
        cat_index = self.find_index(key , "cat")
        item_name_index = self.find_index(item_details["item_name"], None)

        '''The following checking is needed because there might be 2 or more  tupels in  the hash_map list and find's the index of the desired value'''
        for index, i in enumerate(self.cat_hash_table[cat_index]):
            record_key, record_value = i
            if (record_key == key ):
                break;
        for item_index, i in enumerate(self.cat_hash_table[cat_index][index][1][item_name_index]):
            item_name, value = i
            if item_name == item_details["item_name"]:
                item_found = True
                break;
        if item_found:
            self.cat_hash_table[cat_index][index][1][item_name_index][item_index] = item_details["item_name"], item_details

            return "item_updated"
        else:
            self.cat_hash_table[cat_index][index][1][item_name_index].append((item_details["item_name"] , item_details))

            return "item_added"
    def edit_item(self , cat_name , old_item_name , new_item_details):
        new_item_found = False
        insert_edited_item = self.search_cat(cat_name, old_item_name, True) # gets   all the necessary index's needed to  delete the old  item
        cat_index = insert_edited_item[0]
        old_item_index = insert_edited_item[3]

        '''The following checking is needed because there might be 2 or more  tupels in  the hash_map list and find's the index of the desired value'''
        for  index , i in enumerate(self.cat_hash_table[cat_index]):
            key,value = i
            if key == cat_name:
                break;

        '''check if the new item already exists '''
        for i in self.cat_hash_table[cat_index][index][1][old_item_index]:
            key, value = i
            if value["item_name"] == new_item_details["item_name"]:
                new_item_found = True
                break
        if new_item_found:
            return "Item_already_exists"
        else:
            self.item_set_val(cat_name , new_item_details) # set's the new value tuple
            self.del_item(cat_name , old_item_name) # Delete's the old value tuple

            return "item_edited"

    def search_cat(self, cat_name, item_name , edit_or_delete_item_func_calling):

        cat_found = False
        item_found = False
        searched_cat_index = self.find_index(cat_name, "cat")
        searched_item_index = self.find_index(item_name, None)

        '''The following checking is needed because there might be 2 or more  tupels in  the hash_map list and find's the index of the desired value'''
        for index, i in enumerate(self.cat_hash_table[searched_cat_index]):
            searched_key, searched_value = i
            if searched_key == cat_name:
                cat_found = True
                break;
        if cat_found:
            for item_index, i in enumerate(self.cat_hash_table[searched_cat_index][index][1][searched_item_index]):
                searched_key, searched_value  = i
                if searched_key == item_name:
                    item_found = True;
                    break;
            if item_found:
                if edit_or_delete_item_func_calling:
                    return (searched_cat_index,index,1,searched_item_index,item_index)
                return ( self.cat_hash_table[searched_cat_index][index][1][searched_item_index][item_index][1])
            else:
                return False

        return "sorry but there is no name like that in the Inventory  "
    def search_cat_only(self, cat_name):
        cat_found = False
        searched_cat_index = self.find_index(cat_name, "cat");
        for  i in (self.cat_hash_table[searched_cat_index]):
            searched_key, searched_value = i
            if searched_key == cat_name:
                cat_found = True
                break

        return cat_found
    def get_items_in_cat(self , cat_name):
        items = []
        cat_found = False
        cat_index = self.find_index(cat_name, "cat")
        for index, i in enumerate(self.cat_hash_table[cat_index]):
            searched_key, searched_value = i
            if searched_key == cat_name:
                cat_found = True
                break;
        if cat_found:
            for index_2, i in enumerate(self.cat_hash_table[cat_index][index][1]):
                if len(i) > 0:
                    for j in i:
                       items.append(j[1])
            return items




    def get_cat_lst(self):
        return self.__cat_lst

    def del_cat(self , cat_name):
         del_cat_index = self.create_catagory(cat_name , True)
         cat_index = del_cat_index[0]
         cat_tuple_index = del_cat_index[1]
         self.cat_hash_table[cat_index].pop(cat_tuple_index)
         self.__cat_lst.pop(self.__cat_lst.index(cat_name))
         return True
    def del_item(self, cat_name , item_name):
        item = self.search_cat(cat_name , item_name , True)

        self.cat_hash_table[item[0]][item[1]][item[2]][item[3]].pop(item[4])
        return True


    def find_index(self, key, cat_or_item):
        if cat_or_item == "cat":
            return abs(hash(key)) % self.size
        return abs(hash(key)) % 80

    def write_to_csv(self, cat_name, item_name, item_amount, item_pirce):
        with open("uspw.csv", "a+") as file:
            header = ["Cat_name", "item_name", "item_amount", "item_pirce"]
            dw = DictWriter(file, fieldnames=header)
            dw.writeheader()
            dw.writerow({
                header[0]: cat_name,
                header[1]: item_name,
                header[2]: item_amount,
                header[2]: item_pirce
            })


    def __str__(self):
        return ''.join(str(_) + "\n" for _ in self.cat_hash_table)







