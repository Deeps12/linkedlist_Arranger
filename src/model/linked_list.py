import os
import json


class Node(object):
    '''
    This is basic Node class following
    singly linked list structure
    '''

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        try:
            self.next_node
        except:
            return None

    def set_next(self, new_next):
        self.next_node = new_next
        
    def __str__(self):
        pass
    

class LinkedList(object):
    '''
    Linked List class where each ele comprises
    of each Unit object Node
    
    To create LinkedList object 
    call it using either of ways 
    =>LinkedList(8)
    =>LinkedList(Node(8))
    '''
    def __init__(self, ele=None):
        if isinstance(ele, Node):
            self.head = ele
        elif not(ele is None): 
            head = Node(ele)
            self.head = head
        else:
            self.head = None
        self.size = None
        
    def insert(self, data):
        '''
        This will insert node in 
        created linked list
        :param data: Node object
        :type data: object

        '''
        if self.head:
            temp = Node(data)
            temp.set_next(self.head)
            self.head = temp
        else:
            self.head = Node(data)
    
    def print_elems(self):
        '''
        This method will print each ele in linked list
        '''
        if self.head:
            print(self.head.data)
            current_node = self.head.next_node
            while not(current_node == None):
                print(current_node.data)
                current_node = current_node.next_node
    
    def get_size(self):
        '''
        This will return size of linked list
        '''
        if self.head:
            #print(self.head.data)
            current_node = self.head.next_node
            size = 1 
            while not(current_node == None):
                #print(current_node.data)
                current_node = current_node.next_node
                size = size + 1
            return size
        return 0

    def swap_node_data(self, cur_node, next_node):
        '''
        This methode will sort data of two 
        elements in linked list
        '''
        temp = cur_node.data
        cur_node.data = next_node.data 
        next_node.data = temp

    
    def __sort(self):
        '''
        private method to sort element in linked list
        currntly using bubble sort for sorting
        '''
        if self.head:
            cur_node = self.head
            next_node = cur_node.next_node
            #print("+##>" + str(cur_node.data))
            while not(cur_node == None):
                while not(next_node == None):
                    if cur_node.data > next_node.data:
                        self.swap_node_data(cur_node, next_node)
                    #print("++>" + str(next_node.data))
                    next_node = next_node.next_node
                cur_node = cur_node.next_node
                if cur_node:
                    #print("+##>" + str(cur_node.data))
                    next_node = cur_node.next_node

    def __split_list(self):
        '''
        This is used for spliting list in  two 
        list where list2 size is greater than list one size if total 
        number of elements are odd
        
        :return: tuple of (LinkedList1, LinkedList2)
        :rtype: tuplle
        '''
        if self.size:
            split_size = int(self.size/2)
        else:
            self.size = self.get_size()
        cur_node = self.head
        if self.head:
            while (split_size > 0):
                prev_node = cur_node
                cur_node = cur_node.next_node
                split_size -= 1
            prev_node.next_node = None   
        return(LinkedList(self.head), LinkedList(cur_node))
    
    def rearrange_list(self, output_file_name=None):
        '''
        This will rearrange list and save it to json file 
        in output folder
        '''
        self.__sort()
        self.size = self.get_size()
        if self.size > 2:
            (list1, list2) = self.__split_list()
        #list1.print_elems()
        #list2.print_elems()
        if output_file_name:
            path = os.path.join(os.path.abspath(
                                        os.path. os.chdir("..")),
                                        "output",
                                        output_file_name)
        else:
            path = os.path.join(os.path.abspath(
                                        os.chdir(".")),
                                        "output",
                                        "output_array.json")
    
        data = []
        ele_2 = list2.head
        ele_1 = list1.head
        while not(ele_1 == None):
            data.append(ele_2.data)
            data.append(ele_1.data)
            ele_2 = ele_2.next_node
            ele_1 = ele_1.next_node
        if (self.size - int(self.size/2)*2) == 1:
            data.append(ele_2.data)
       
        with open(path, 'w') as fw:
            json.dump(data, fw)
        
        return (list1, list2)
        
