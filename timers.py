import threading
 
import signal
TIMEOUT = 5 # number of seconds your want for timeout

def interrupted(signum, frame):
    "called when read times out"
    print 'interrupted!'
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
            print 'You have 5 seconds to type in your stuff...'
            foo = raw_input()
            return foo
    except:
            # timeout
            return

# set alarm
signal.alarm(TIMEOUT)
s = input()
# disable the alarm after success
signal.alarm(0)
print 'You typed', s

def gfg(): 
    print("Time's up\n") 
  
timer = threading.Timer(1.0, gfg) 
timer.start() 
print("Exit\n") 