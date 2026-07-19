class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cap = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    def addFront(self, node):
        curHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = curHead
        curHead.prev = node

    def get(self, key: int) -> int: 
        getNode = self.hashmap.get(key, None)
        if not getNode:
            return -1
        else:
            self.removeNode(getNode)
            self.addFront(getNode)
            return getNode.val
        
    def put(self, key: int, value: int) -> None:
        curNode = self.hashmap.get(key, None) 
        if curNode: #key is already in list; just put to front
            curNode.val = value
            self.removeNode(curNode)
            self.addFront(curNode)
        else:
            #key not in; put in
            newNode = Node(key, value)
            self.addFront(newNode)
            self.hashmap[key] = newNode
            if len(self.hashmap) > self.cap:
                nodeToRemove = self.tail.prev
                self.removeNode(nodeToRemove) #remove from list 
                del self.hashmap[nodeToRemove.key] #remove from hashmap
                
            
            
