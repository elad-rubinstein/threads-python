"""
putting_and_getting_from queues_using_threads
"""
import queue
import threading
file = open("lol.txt", "w")


def put_queue(queue1: queue.Queue):
    """
    The method get inputs and put it in a queue in an infinite loop

    :param queue1: The queue to put an input in.
    """
    flag = True
    while flag:
        inp = input("please input: ")
        queue1.put(inp)
        if inp == "":
            flag = False


def get_queue(queue1: queue.Queue):
    """
    The function try to get a massage from a queue and write it to a file
    in an infinite loop

    :param queue1: The queue to get a massage from.
    """

    while True:
        if not queue1.empty():
            massage = queue1.get()
            file.write(massage)


def main():
    """
    The function run the put_queue and get_queue methods
    """
    queue1 = queue.Queue()
    t1 = threading.Thread(target=put_queue, args=[queue1])
    t2 = threading.Thread(target=get_queue, args=[queue1])
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
