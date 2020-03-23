#------------------------#
#---Alexander Shevtsov---#
#--github: alexdrk14-----#
#------------------------#
#time estimation library that are should be called in every exectuion cycle
#in case when step of execution is different step should be passed in each function call

import time

global_nmb_iter = None
global_nmb_exec = None
global_time_start = None

def estimateTime(nmb_iter=None, step=None, debug=False):
  global global_nmb_iter
  global global_nmb_exec
  global global_time_start
 
  if debug: print("DEBUG at start: NMB_ITER:{} NMB_EXEC:{} TIME_START:{}".format(global_nmb_iter, global_nmb_exec, global_time_start))
  
  if global_time_start is None: global_time_start = time.time()
  if step is None: step = 1
  if nmb_iter is None and global_nmb_iter is None:
      return sys.exit(-1)
  elif global_nmb_iter is None: global_nmb_iter = nmb_iter
  
  if global_nmb_exec is not None:
    
    print("Completed: {:.1f}% Estimated Time Left: {:.2f}sec. Time Spend: {:.2f}sec.".format(((global_nmb_exec*100)/float(global_nmb_iter)), 
     (((time.time()-global_time_start) / float(global_nmb_exec))*(global_nmb_iter - global_nmb_exec)),
      (time.time()-global_time_start)))
    global_nmb_exec += step 
  else: global_nmb_exec = step
  if debug: print("DEBUG at end: NMB_ITER:{} NMB_EXEC:{} TIME_START:{}".format(global_nmb_iter, global_nmb_exec, global_time_start))
  
  return 0

