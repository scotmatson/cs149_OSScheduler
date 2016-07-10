import logging
import datetime
import sys
import random
import memory
from queue import PriorityQueue
from process import Process

def create_job_queue(number, name, size, execution, runtime):
    '''
    Generates random processes and places them into a priority queue
    '''
    # Initialize the processes
    # TODO Enforce unique naming
    # TODO Enforce even distribution
    pq = PriorityQueue(maxsize=0) # If maxsize is 0, queue size is infinite
    for i in range(number):
        priority = random.choice(range(execution))
        process = Process(
            random.choice(name),
            random.choice(size),
            priority,
            random.choice(runtime))
        pq.put((priority, process))
    return pq

def main():
    logging.info('Inside main()')

    # Simulation Variables 
    EXECUTION_TIME  = 600

    # Memory Variables
    MAIN_MEMORY     = 100             # Units as MB 
    TOTAL_PAGES      = 100
    PAGE_SIZE       = 1               # Size as MB

    # Process Variables
    NUMBER_OF_PROCESSES = 150
    PROCESS_NAME_SIZE    = range(11)
    PROCESS_SIZE    = [5, 11, 17, 31] # Randomly chosen, Size as MB
    PROCESS_RUNTIME = [1, 2, 3, 4, 5] # Randomly chosen, Time as seconds

    book_keeping = list()
    workload = create_job_queue(
        NUMBER_OF_PROCESSES,
        PROCESS_NAME_SIZE,
        PROCESS_SIZE,
        EXECUTION_TIME,
        PROCESS_RUNTIME)

    # Initialize page_list
    page_table = memory.pagetable.PageTable(TOTAL_PAGES, PAGE_SIZE)

    test_counter = 0
    while not workload.empty() and test_counter < 3: # Prevent infinite loops during tests
        test_counter += 1
        if page_table.available_pages() > 3:             # there are at least 4 free pages
            pass
            #process = workload.get()
            #free_pages = [page_table.get_free_pages(4)]  # get the free pages 
            #print(free_pages)
            #print(process)
            # Get a process, Get Pages, Couple, Update PageTable

    # TODO Generate an appropriate record whenever starting or completing a job
    #      <time stamp, process name, enter/exit, size, duration, memory-map>


################################################################################
if __name__ == '__main__':
    # Logging Init
    current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d.%H%M%S')
    logging_file = 'logs/simulator_' + current_time + '.log'
    logging_format = '%(asctime)s %(message)s'
    logging.basicConfig(filename=logging_file, format=logging_format, level=logging.DEBUG)

    # Application entry point
    logging.info('Calling procedure main(), initiating paging simulation')
    main();
    # Application controlled termination
    logging.info('Application execution terminated successfully')
    sys.exit()



