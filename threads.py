import threading

def calculate():
    return 15**3

thing = threading.Thread(target=calculate)
thing.start()
thing.join()