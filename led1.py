import RPi.GPIO as IO
import time
IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)
IO.output(40,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)
i=1
IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)
while(1):
    IO.output(40,1)
    time.sleep(1)
    IO.output(40,0)
    time.sleep(1)
    IO.setmode(IO.BOARD)
    IO.setup(40,IO.OUT)
    IO.output(40,1)
    time.sleep(1)
    IO.cleanup()
    time.sleep(1)
