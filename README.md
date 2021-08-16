# py_timer
I simple timer in python that starts with the usual command `sudo python timer.py` and stops as **s** is pressed.

**Dependencies**
==================
1. **`keyboard`**
Now in the above command `sudo` is used as I am using `keyboard` module that required system root permissions.
So, had to install `keyboard` at root level; i.e, `sudo pip3 install keyboard`.

2. **`sys`**
`sys` is usually present in most of the system default. So you need not install it separately, just import and use.
This sys module provides with a function `exit()` that I have used. This as per [Named Link](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/ "GFG title") is a good practice, and for me it really had difference between exit() and sys.exit().

3. `os`
So as to perform operating system operations. Herein, I used it to run system command using its `system()` passed with the command I wanted to run, `clear`.
This command may differ system to system, i.e, I used Manjaro with XFCE (bash) so it clear the screen the command is `clear`.
If you are a windows user, I `'clear'` command will be replaced with `cls` and similarly for OS and distros.

4. `time`
Since it's a timer, it has to act like a real timer. The `sleep()` of this module is used to take the gap of 1 sec before incrementing the seconds indicator.
