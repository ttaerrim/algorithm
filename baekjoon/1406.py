import sys

class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0
    
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True
    
    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow: Index Error")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target
    
    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1
            
    
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1
    
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_next = tmp.next
                newNode = Node(value, tmp, tmp_next)
                tmp_next.prev = newNode
                tmp.next = newNode
        self.size += 1
        
    def delete(self, idx):
        if self.is_empty():
            print("Underflow Error")
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del(tmp)
            self.size -= 1
    
    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, end='')
            else:
                print(target.data)
            target = target.next


w = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

linked_list = LinkedList()
for s in w:
    linked_list.append(s)


cursor = len(w) - 1
for _ in range(n):
    c = sys.stdin.readline().strip().split()
    if (c[0] == 'P'):
        linked_list.insert(c[1], cursor)
        cursor += 1
    elif (c[0] == 'L'):
        if (cursor >= 0): 
            cursor -= 1
    elif (c[0] == 'D'):
        if (cursor < linked_list.listSize() - 1 and linked_list.selectNode(cursor) != linked_list.tail):
            cursor += 1
    elif (c[0] == 'B'):
        if (cursor >= 0):
            linked_list.delete(cursor)
            cursor -= 1
            
linked_list.printlist()
