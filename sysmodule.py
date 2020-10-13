import sys

print(sys.maxsize)
print(sys.maxunicode)
print(sys.path[0])
curr_dir=sys.path[0]
print(sys.version[:1])
if sys.version[:1]=="2":
    print("python2")
elif sys.version[:1]=="3":
    print("python3")
sys.exit(1)