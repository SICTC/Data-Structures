
class Heap(object):
    
    def __init__(self):
        #heap data
        #nothing ever goes in index 0, so just put none there
        self._h = [None, ]
        
        #last index we used
        self._last = 0
        
    #we don't need h[0], so return the slice starting at 1
    def __str__(self):
        return str(self._h[1:])
    
    def __len__(self):
        return self._last
    
    def _parent(self, i):
        return i//2
    
    def _left(self, i):
        lc = 2*i
        #make sure lc is in the range of our data
        return lc if lc <= self._last else None
    
    def _right(self, i):
        rc = 2*i + 1
        return rc if rc <= self._last else None
    
    #exchange data at indices i and j
    def _swap(self, i, j):
        self._h[i], self._h[j] = self._h[j], self._h[i]
        
    #O(log n)
    def _bubbleup(self, i):
        #root (i=1) doesn't have a parent,
        #or heap condition is satisfied,
        #we're done
        if i == 1 or self._h[self._parent(i)] < self._h[i]:
            return
    
        self._swap(i, self._parent(i))
        self._bubbleup(self._parent(i))
    
    #O(log n)
    def _bubbledown(self, i):
        lc = toSwap = self._left(i)
        rc = self._right(i)
        
        #no left child
        if not lc:
            return
        
        #if right child exists and..
        if rc:
            #is less than left child
            if self._h[rc] < self._h[lc]:
                toSwap = rc
                
        #check heap property
        if self._h[i] < self._h[toSwap]:
            return
        
        #otherwise, repair heap
        self._swap(i, toSwap)
        self._bubbledown(toSwap)
    
    #O(1) + O(1) + O(log n)
    #total=O(log n)
    def insert(self, item):
        self._last += 1
        self._h.append(item)
        self._bubbleup(self._last)
    
    #O(1) + O(1) + O(1) + O(1) + O(log n)
    #total=O(log n)
    def remove(self):
        if self.isEmpty():
            return None
        
        toReturn = self._h[1]
        #pull up data in last position to root
        self._h[1] = self._h[self._last]
        self._last -= 1
        #remove old last
        self._h.pop()
        #repair heap
        self._bubbledown(1)
        
        return toReturn
    
    #complexity: O(1)
    def peek(self):
        return None if self.isEmpty() else self._h[1]
    
    def isEmpty(self):
        return self._last <= 0
        
    def isFull(self):
        return False
        