class Stack(object):
    
    def __init__(self):
        self.make_empty()
        
    def make_empty(self):
        self._elements = []
    
    def push(self, item):
        self._elements.append(item)
    
    def pop(self):
        try:
            return self._elements.pop()
        except IndexError:
            return None
    
    def peek(self):
        try:
            return self._elements[-1]
        except IndexError:
            return None

    def is_empty(self):
        return len(self._elements) == 0
    
    def is_full(self):
        return False
    
    def __len__(self):
        return len(self._elements)






    