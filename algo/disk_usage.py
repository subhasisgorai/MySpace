from __future__ import absolute_import
from __future__ import print_function
import os
def disk_usage(path):
    total = os.path.getsize(path) 
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
            
    print('{0:<7}'.format(total), path)
    return total
                

path = input("Enter a directory to start: ")
total = disk_usage(path)
print('total directory size {}'.format(total))
