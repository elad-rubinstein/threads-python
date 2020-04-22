"""
Usage of queues
"""
import queue
import threading

queue = queue.Queue()


def put_queue():
    """
    The method get inputs and put it in a queue in an infinite loop
    """
    while True:
        inp = input("please input: ")
        queue.put(inp)
        if inp == "":
            break


def get_queue():
    """
    The function try to get a massage from a queue and write it to a file
    in an infinite loop
    """
    open("task_three_file.txt", "w+")
    f = open("task_three_file.txt", "a")
    while True:
        if not queue.empty():
            massage = queue.get()
            f.write(massage)


def main():
    """
    The function create two threads to be responsible on two different methods
    """
    t1 = threading.Thread(target=put_queue)
    t2 = threading.Thread(target=get_queue)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
