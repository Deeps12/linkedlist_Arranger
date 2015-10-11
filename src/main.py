from model.linked_list import LinkedList

if __name__ == "__main__":
    """
    This is Executor and 
    to execute navigate to 
    "..\linked_list_arranger\src" and type 
    'python main.py'
    press enter
    """
    #input_list = [0,5,2,8,1,100,101,78,40,25,12]
    input_list = [1,0,3,6,5,10]
    output_file_name = "output_array.json"
    obj_linked_list = LinkedList(input_list[0])
    for each_ele in input_list[1:]:
        obj_linked_list.insert(each_ele)
    (list1, list2) = obj_linked_list.rearrange_list(output_file_name)