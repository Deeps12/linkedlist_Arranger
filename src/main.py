from model.linked_list import LinkedList
import logging
from logging.handlers import RotatingFileHandler
import os

class Logger(object):
    def create_logger(self, folder_name = None):
        msgfmt = "%(asctime)s %(levelname)5s %(module)s(%(lineno)s): %(message)s"
        myfmtr = logging.Formatter(fmt=msgfmt)
        logging.basicConfig(level=logging.INFO)
        if folder_name:
            log_path = os.path.join(os.path.abspath(
                                            os.path. os.chdir(".")),
                                            folder_name,
                                            "linked_list.log")
        else:
            log_path = os.path.join(os.path.abspath(
                                            os.path. os.chdir("..")),
                                            "log",
                                            "linked_list.log")
        handler = RotatingFileHandler(log_path,
                                          maxBytes=1024*1024,
                                          backupCount=5)
        handler.setFormatter(myfmtr)
        logger = logging.getLogger("LinkedList")
        logger.addHandler(handler)
        return logger
        
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
    
    logger = Logger().create_logger()
    output_file_name = "output_array.json"
    obj_linked_list = LinkedList(input_list[0])
    for each_ele in input_list[1:]:
        obj_linked_list.insert(each_ele)
    logger.info("processing linked list for rearranging")
    
    (list1, list2, data) = obj_linked_list.rearrange_list(output_file_name)
    logger.info(str(data))