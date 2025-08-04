import math
#create a pagination system
#step 1
class Pagination:
    def __init__(self, items=[], page_size=10 ):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

#implement method
    def get_visible_items(self):
        first = self.current_idx * self.page_size
        last = first + self.page_size
        return self.items[first:last] 
    
#implement navi methods
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("No dice!")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current.idx = 0
        return self
    
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        items = self.get_visible_items()
        return "\n".join(str(item) for item in items)

    

#this is a test
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
print(str(p))
p.next_page()
p.next_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
p.go_to_page(7)
print(p.current_idx + 1)
p.go_to_page(0)