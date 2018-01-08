class Heap(object):
    
    def __init__(self):
        #array to store heap data
        self._h = [None, ]
        #the last index we used
        self._last = 0
    
    def __str__(self):
        return str(self._h[1:])
    
    def __len__(self):
        return self._last
    
    def _parent(self, i):
        return i//2
    
    def _left(self, i):
        #check and make sure left child is actually in heap
        lc = 2*i
        return lc if lc <= self._last else None
    
    def _right(self, i):
        #same as left
        rc = 2*i + 1
        return rc if rc <= self._last else None
    
    def _swap(self, i, j):
        #exchange data at i and j
        self._h[i], self._h[j] = self._h[j], self._h[i]
        
    def _bubbleup(self, i):
        #if we're at the root or the heap property is satisfied,
        #then we're done
        if i == 1 or self._h[self._parent(i)] < self._h[i]:
            return
        
        #otherwise, swap i and its parent, then bubbleup from parent
        self._swap(i, self._parent(i))
        self._bubbleup(self._parent(i))
        
    def insert(self, item):
        self._last += 1
        self._h.append(item)
        self._bubbleup(self._last)
