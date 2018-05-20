class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None
    def mergekList(self, lists):
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
L = Node('a', Node('b', Node('c', Node('d'))))
print(L.next.next.value)
lists = [Node('1', Node('4',Node('5'))), Node('1', Node('3', Node('4'))), Node('2', Node('6'))]
k = Node()
print(k.mergekList(lists))

