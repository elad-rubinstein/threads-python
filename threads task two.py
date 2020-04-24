"""
Threads_competition
"""
from queue import Queue
import threading
import time

lst_names = []


def get_score(threads_name: str, event: threading.Event, queue: Queue):
    """
    According to the event, the func take a score from a global list and put
     a name in another global list

    :param threads_name: The name of the thread accessing this method.
    :param event: The Event used to synchronize between threads.
    :param queue: A queue to store scores.
    """
    event.wait()
    queue.get()
    lst_names.append(threads_name)
    event.clear()


def calculate_score():
    """
    Calculate which thread in a global list has the highest score and print it
    """
    max_wins = 0
    max_name = ""
    for thread_name in lst_names:
        name_count = lst_names.count(thread_name)
        if name_count > max_wins and name_count > 1:
            max_wins = name_count
            max_name = thread_name

    if max_name:
        print(f"Winner is {max_name}")
    else:
        print("There isn't one winner!")


def main():
    """
    The method runs a a five-round-competition between threads
    using the get_score method
    """
    event = threading.Event()
    queue = Queue()
    round_thread = 1
    LAST_ROUND = 5
    while round_thread <= LAST_ROUND:
        queue.put(int(input("input a score: ")))

        for i in range(10):
            name = "thread " + str(i + 1)
            x = threading.Thread(target=get_score, args=[name, event, queue])
            x.start()

        event.set()
        time.sleep(0.5)
        print("list of winners every round: ")
        print(lst_names)
        round_thread += 1

    calculate_score()


if __name__ == '__main__':
    main()
