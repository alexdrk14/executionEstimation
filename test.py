#------------------------#
#---Alexander Shevtsov---#
#--github: alexdrk14-----#
#------------------------#
import random
import time
from timeEst import estimateTime

def function_main():
  x = random.randrange(10,20)
  for i in range(1,x):
    estimateTime(x)
    print("Round:{}".format(i))
    time.sleep(random.randrange(1,8))


function_main()
