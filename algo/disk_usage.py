import os


def disk_usage(path):
    total = os.path.getsize(path) 
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
            
    print '{0:<7}'.format(total), path
    return total
                

path = raw_input("Enter a directory to start: ")
total = disk_usage(path)
print 'total directory size {}'.format(total)
