"""
Synchronisation in threads
"""
from threading import Thread, Event

event = Event()


def write_even(s: str):
    """
    Print the even chars of a given string correspondingly to the event

    :param s: A given string to be printed.
    """

    for char in s[1::2]:
        event.wait()
        print(char)
        event.clear()


def main():
    """
    Create a thread and print the odd chars of a string correspondingly
     to the event
    """
    s = "synchronization"
    even_printer = Thread(target=write_even, args=[s])
    even_printer.start()
    i = 0

    while i <= len(s):
        if not event.is_set():
            print(s[i])
            i += 2
            event.set()


if __name__ == '__main__':
    main()
