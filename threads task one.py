"""
Synchronisation_in_threads
"""
from threading import Event, Thread


def write_even(string: str, event: Event):
    """
    Print the even chars of a given string correspondingly to the event

    :param string: A given string to be printed.
    :param event: The Event used to synchronize between threads.
    """
    for char in string[1::2]:
        event.wait()
        print(char)
        event.clear()


def main():
    """
    Print the odd chars of a string correspondingly to the event
    """
    event = Event()
    str1 = "synchronization"
    even_printer = Thread(target=write_even, args=[str1, event])
    even_printer.start()
    i = 0

    while i <= len(str1):
        if not event.is_set():
            print(str1[i])
            i += 2
            event.set()


if __name__ == '__main__':
    main()
