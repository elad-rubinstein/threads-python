"""
Threads competition
"""
import time
import threading

lst_names = []
lst_score = []
event = threading.Event()


def get_score(threads_name: str):
    """
    According to the event, the threads accessing this method try
    to take a score from a global list and put it in another global list

    :param threads_name: The name of the thread accessing this method.
    """
    event.wait()
    if lst_score:
        lst_score.pop(0)
        lst_names.append(threads_name)
        event.clear()
        event.wait()


def calculate_score():
    """
    Calculate which thread in a global list has the highest score and print it
    """
    max_wins = 0
    max_name = ""
    for thread_name in lst_names:
        if lst_names.count(thread_name) > max_wins \
                and lst_names.count(thread_name) > 1:
            max_wins = lst_names.count(thread_name)
            max_name = thread_name

    print(f"winner is {max_name}")


def main():
    """
    In a five-rounds loop the method create 10 threads to compete against
    each other using the get_score method
    """
    round_thread = 1
    while round_thread <= 5:
        lst_score.append(int(input("input a score: ")))

        for i in range(10):
            thread_name = "thread " + str(i + 1)
            x = threading.Thread(target=get_score, args=[thread_name])
            x.start()

        event.set()
        time.sleep(0.5)
        print("list of winners every round: ")
        print(lst_names)
        round_thread += 1

    calculate_score()


if __name__ == '__main__':
    main()
