#------------------------#
#---Alexander Shevtsov---#
#--github: alexdrk14-----#
#------------------------#
#simple example of library usage

import random
import time
from timeEst import estimateTime

def function_main():
  x = random.randrange(10,20)
  for i in range(1,x):
    #call function of library in each execution cycle start
    #is important to identify accurate time of execution cycle
    estimateTime(x)

    #after library call perform any calculation that 
    #should be executed by your programm
    print("Round:{}".format(i))
    time.sleep(random.randrange(1,8))


function_main()
