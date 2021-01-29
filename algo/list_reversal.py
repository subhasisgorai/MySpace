class ListNode:

    def __init__(self, data=0, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return str(self.data) if str(self.data) else 'None' 


class LinkedList:

    def __init__(self, head):
        self.head = head
        
    def search_in_list(self, key):
        iter_node = self.head
        while iter_node and iter_node.data != key:
            iter_node = iter_node.nxt
        
        return iter_node if iter_node and iter_node.data == key else None 
    
    def insert_after(self, node, new_node):
        if node and new_node:
            new_node.nxt = node.nxt
            node.nxt = new_node
        return
    
    def delete_after(self, node):
        if node and node.nxt and node.nxt.nxt:
            node.nxt = node.nxt.nxt
        return
    
    def reverse_list(self):
        first, second = None, self.head
        while second:
            third = second.nxt
            second.nxt = first
            if third:
                temp = third.nxt
                third.nxt = second
                first = third
                second = temp
            else:
                self.head = second
                second = None
                
    def reverse_list_recursive(self):
        self.__reverse_list_recursive(self.head).nxt = None
    
    def __reverse_list_recursive(self, node):
        if node:
            if node.nxt:
                self.__reverse_list_recursive(node.nxt).nxt = node
            else:
                self.head = node
        return node 
    
    def print_list(self):
        iter_node = self.head
        while iter_node:
            print iter_node.data,
            iter_node = iter_node.nxt
            print '->' if iter_node else '',
        print ''

    def print_list_reverse(self):
        stack = list()
        iter_node = self.head
        while iter_node:
            stack.append(iter_node.data)
            iter_node = iter_node.nxt
        
        while len(stack):
            print stack.pop(),
            
        print ''
    
    def print_list_reversed_recursive(self):
        self.__print_list_reversed_recursive(self.head) 
    
    def __print_list_reversed_recursive(self, node):
        if node:
            self.__print_list_reversed_recursive(node.nxt)
            print node.data,
        return


if __name__ == '__main__':
    node = ListNode(data=0)
    linked_list = LinkedList(node)
    for i in range(1, 9):
        new_node = ListNode(data=i)
        linked_list.insert_after(node, new_node)
        node = new_node

    linked_list.print_list()
    linked_list.print_list_reverse()
    linked_list.reverse_list()
    linked_list.print_list()
    linked_list.reverse_list_recursive()
    linked_list.print_list()
    linked_list.print_list_reversed_recursive()
