"""
putting_and_getting_from queues_using_threads
"""
import queue
import threading


def put_queue(queue1: queue.Queue):
    """
    The method get inputs and put it in a queue in an infinite loop

    :param queue1: The queue to put an input in.
    """
    inp = input("please input: ")
    while inp:
        queue1.put(inp)
        inp = input("please input: ")
    queue1.put(inp)


def get_queue(queue1: queue.Queue):
    """
    The function try to get a massage from a queue and write it to a file
    in an infinite loop

    :param queue1: The queue to get a massage from.
    """
    file = open("lol.txt", "a")
    flag = True
    while flag:
        message = queue1.get()
        file.write(message)
        if not message:
            flag = False
    file.close()


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
