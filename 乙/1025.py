class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Lian(object):
    def __init__(self):
        self.root = None
    def addNode(self,data):
        if self.root==None:
            self.root = Node(data = data , next=None)
            return self.root
        else
            cursor = self.root
            while cursor.next!=None:
                cursor = cursor.next