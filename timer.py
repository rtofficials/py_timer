import os, time, keyboard, sys
s=50;
m=59;
h=0;
while(True):
  if keyboard.is_pressed("s"):
    sys.exit(0);
  else :
    os.system('clear')
    print('%d : %d  : %d' %(h, m, s))
    time.sleep(0.1)
    s += 1;
    if s==60:
      s=0;
      m+=1
    if m==60:
      m=0
      h =+ 1;
