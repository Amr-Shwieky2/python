class Product:
    def __init__(self, ItemCode, departmentName,
                 itemQuantity, minimumItem, price):
        
        self.ItemCode = ItemCode
        self.departmentName = departmentName
        self.itemQuantity = itemQuantity
        self.minimumItem = minimumItem
        self.price = price
        
    def get_ItemCode(self):  
        return self.ItemCode 
    
    def get_departmentName(self):
        return self.departmentName
     
    def get_itemQuantity(self): 
        return self.itemQuantity
    
    def get_minimumItem(self): 
        return self.minimumItem 
     
    def get_price(self):
        return self.price   

class Products_list:
    def __init__(self):
        self.lstProducts = []
    
    def add(self, product):
        self.lstProducts.append(product)
        self.lstProducts.sort(key =lambda x: x.get_price())
    
    def check_inventory(self):
            for salary in range(len(self.lstProducts)):
                if self.lstProducts[salary].get_itemQuantity() < self.lstProducts[salary].get_minimumItem():
                    print(self.lstProducts[salary].get_ItemCode(),
                          self.lstProducts[salary].get_minimumItem() - self.lstProducts[salary].get_itemQuantity())
    
    def print_category(self, name):
        print(name)
        for salary in self.lstProducts:
            if name == salary.get_departmentName():
                print(salary.get_ItemCode(), salary.get_price())
                
    def price_of(self, code):
        for salary in self.lstProducts:
            if code == salary.get_ItemCode():
                return salary.get_ItemCode(), salary.get_price()
                   
                
                        
                
          
p1 = Product(1,"milk", 567, 500, 3.45)
p2 = Product(2,"milk", 456, 500, 11.12)
p3 = Product(3,"milk", 245, 300, 7.99)
p4 = Product(4,"meat", 38, 30, 23.45)
p5 = Product(5,"meat", 48, 50, 31.45)
pl = Products_list()
pl.add(p1)
pl.add(p2)
pl.add(p3)
pl.add(p4)
pl.add(p5)
pl.check_inventory()
pl.print_category("milk")          
print(pl.price_of(2))