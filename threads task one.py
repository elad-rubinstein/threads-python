"""
Synchronisation_in_threads
"""
import constant
from threading import Event, Thread


def write_even(event: Event):
    """
    Print the even chars of a given string correspondingly to the event

    :param event: The Event used to synchronize between threads.
    """
    for char in constant.str1[1::2]:
        event.wait()
        print(char)
        event.clear()


def main():
    """
    Print the odd chars of a string correspondingly to the event
    """
    event = Event()
    even_printer = Thread(target=write_even, args=[event])
    even_printer.start()
    while constant.index_str <= len(constant.str1):
        if not event.is_set():
            print(constant.str1[constant.index_str])
            constant.index_str += 2
            event.set()


if __name__ == '__main__':
    main()
