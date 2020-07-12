import threading 
def gfg(): 
    print("Time's up\n") 
  
timer = threading.Timer(1.0, gfg) 
timer.start() 
print("Exit\n") 