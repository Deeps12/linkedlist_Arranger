from model.linked_list import LinkedList
import unittest
from main import Logger

class testLinkedList(unittest.TestCase):
    def setUp(self):
        self.logger = Logger().create_logger("log")
        

    def test_empty_linked_list_creation(self):
        '''
        This wil test empty linked test can be created
        '''
        obj_linked_list = LinkedList()
        self.assertIsInstance(obj_linked_list, LinkedList)
    
    def test_linkedlist_functionality(self):
        input_list = [1,0,3,6,5,10]
        obj_linked_list = LinkedList(input_list[0])
        for each_ele in input_list[1:]:
            obj_linked_list.insert(each_ele)
        self.logger.info("processing linked list for rearranging")
        (list1, list2, data) = obj_linked_list.rearrange_list()
        self.assertEqual([5, 0, 6, 1, 10, 3],data)
    
        

if __name__ == "__main__":
    unittest.main()
