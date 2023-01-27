import os
import functools
from datetime import datetime as dt


def wrapper_with_log_action(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path,'a')) as f:
                f.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%d/%m/%Y %H:%M:%S")))
                 
            return func(path)
        
        return the_real_wrapper
    
    return wrapper_with_log_to_known_file

@wrapper_with_log_action('FILE_CREATE','C:................')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
 
@wrapper_with_log_action('FILE_DELETE','C:\\.......')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


 
 
create_file(r'C:.....')
delete_file(r'C:.....')
create_file(r'C:.....')
delete_file(r'C:.....')
