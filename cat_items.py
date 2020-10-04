class cat_Items:
    def __init__(self , cat_name):
        self.cat_name = cat_name
        self.item_lst = []
    def add_item(self , item_name):
        self.item_lst.append(item_name)
