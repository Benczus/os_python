import sys
import os

pid=os.fork()

if pid!=0:
    print("Parent process")
else:
    print("Child Process")
