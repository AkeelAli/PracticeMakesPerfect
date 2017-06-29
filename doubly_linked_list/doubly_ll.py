class Node():
    def __init__(self, data, p=None, n=None):
        self.data = data
        self.prev = p
        self.next = n

class DoublyLinkedList():
    def __init__(self):
        self.size = 0 # explore replacing with __len__ property?
        self.head = self.tail = None
        self.hash = {} # key: data, value: Node

    def add_to_head(self, data):
        if not data:
            raise Exception('Data cannot be None')
        if data in self.hash:
            raise Exception('Duplicate data add attempted')

        n = Node(data)
        if self.size == 0:
            self.head = self.tail = n
        else:
            self.head.prev = n
            n.prev, n.next = None, self.head
            self.head = n

        self.size += 1 
        self.hash[data] = n

    def delete_node(self, n):
        if not n:
            raise Exception("Node cannot be None")
        if self.head == self.tail == n:
            self.head = self.tail = None
        elif self.head == n:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        elif self.tail == n:
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            n.prev.next = n.next
            n.next.prev = n.prev.next

        del n
        self.size -= 1

    def delete(self, data):
        ''' Deletes occurence of data
        '''
        if self.hash[data]:
            self.delete_node(self.hash[data]) 

    def __repr__(self):
        s = ''
        n = self.head
        while n:
            s += str(n.data) + ('<->' if n.next else '')
            n = n.next
        return s

if __name__ == '__main__':
    d = DoublyLinkedList()
    try:
        d.add(None)
        assert False, "adding None to List did not raise an exception"
    except:
        pass
        

    d.add_to_head(1)
    assert (repr(d) == '1')
    d.add_to_head(2)
    assert (repr(d) == '2<->1')
    d.add_to_head(-10)
    assert (repr(d) == '-10<->2<->1')
    d.delete(2)
    assert (repr(d) == '-10<->1')
    d.delete(-10)
    assert (repr(d) == '1')
