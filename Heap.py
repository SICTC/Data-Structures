from math import floor, log2
from operator import lt, gt

class Heap(object):
    
    @staticmethod
    def heapsort(m):
        h = Heap(m)
        temp = []
        
        while not h.isEmpty():
            temp.append(h._h[1])
            h._swap(1, h._last)
            h._last -= 1
            h._bubbledown(1)
            
        return temp
    
    @staticmethod
    def introsort(m):
        #idea: use quicksort, heapsort, and insertion sort, based on
        #some conditions
        #start out with quicksort, always.
        #if quicksort doesn't run "well enough", switch to heapsort
        #use insertion sort if len <= 16
        #what does "well enough" mean?
        #measure recursion depth
        maxdepth = floor(log2(len(m)))*2
        return Heap._introsort(m, maxdepth)
    
    @staticmethod
    def _introsort(m, maxdepth):
        #base case: a list of length 1 is always sorted
        if len(m) <= 1:
            return m
        #insertion sort for lists of length <= 16
        elif len(m) <= 16:
            for k in range(1, len(m)):
                while 0 < k and m[k] < m[k-1]:
                    m[k], m[k-1] = m[k-1], m[k]
                    k -= 1
            return m
        #if we exceed max recursion depth, switch to heapsort
        elif maxdepth <= 0:
            return Heap.heapsort(m)
        #otherwise, just use quicksort in the normal case
        else:
            pivot = m[0]
            less = [x for x in m[1:] if x < pivot]
            more = [x for x in m[1:] if x > pivot]
            
            return Heap._introsort(less, maxdepth-1) + [pivot] \
                + Heap._introsort(more, maxdepth-1)
    
    def __init__(self, from_list=None, kind="min"):
        #heap data
        #nothing ever goes in index 0, so just put none there
        self._h = [None, ]

        #last index we used
        self._last = 0
        
        mins = ["min", "minimum"]
        maxes = ["max", "maximum"]
        
        if kind in mins:
            self._kind = "minimum"
            #use less than
            self._comp = lt
        elif kind in maxes:
            self._kind = "maximum"
            #use greater than
            self._comp = gt
        else:
            raise ValueError("No such Heap kind {0}",
                "expected one of {1}".format(repr(kind), mins + maxes))
        
        if from_list:
            self._h += from_list
            self._last = len(from_list)
            self._heapify()
        
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
        if i == 1 or self._comp(self._h[self._parent(i)], self._h[i]):
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
            #is less than left child (min heap)
            #is greater than left child (max heap)
            if self._comp(self._h[rc], self._h[lc]):
                toSwap = rc
                
        #check heap property
        if self._comp(self._h[i], self._h[toSwap]):
            return
        
        #otherwise, repair heap
        self._swap(i, toSwap)
        self._bubbledown(toSwap)
    
    #O(n)
    def _heapify(self):
        #from parent(last) downto 1, bubbledown
        for i in range(self._parent(self.last), 0, -1):
            self._bubbledown(i)
    
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
    
    def merge(self, other):
        self._h += other
        self._last += len(other)
        self._heapify()
    
    def isEmpty(self):
        return self._last <= 0
        
    def isFull(self):
        return False
    
    def getKind(self):
        return self._kind
        