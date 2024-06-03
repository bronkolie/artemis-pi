import time

button1 = False
button2 = False

def one():
    time.sleep(5) #long action
def two():
    time.sleep(5) #long action

while True:
    if button1:
        one()
    if button2:
        two()

