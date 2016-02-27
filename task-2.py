import resource, pdb, logging

logging.basicConfig(filename='log/log.log',level=logging.DEBUG)

"""
This is assuming that the maximum age is 150.
"""

sorted_age = open("files/ages-8-billion-sort.txt","w")
for index in range(1,151):
    with open('files/ages-8-billion.txt') as f:
        logging.debug('resource used index %s :: %s' % (index, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        for line in f:
            age = int(line.replace('\n',''))
            if age is index:
                sorted_age.write(str(age) + '\n')
                logging.debug('resource used age %s :: %s' % (age, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
logging.debug('resource used finish %s' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
sorted_age.close()