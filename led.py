import RPi.GPIO  as IO
import time
IO.setwarnings(False)
led1=40
led2=31
led3=33

d=0.6
d1=0.3
d2=0.5
IO.setmode(IO.BOARD)
IO.setup(led1,IO.OUT)
IO.setup(led2,IO.OUT)
IO.setup(led3,IO.OUT)

while(1):
    print(0)
    IO.output(led1,1)
    time.sleep(d)
    IO.output(led2,1)
    time.sleep(d1)
    IO.output(led3,1)
    time.sleep(d2)
    IO.output(led1,0)
    time.sleep(d1)
    IO.output(led2,0)
    time.sleep(d1)
    IO.output(led3,0)
    time.sleep(d1)
IO.cleanup()
