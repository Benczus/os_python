import sys
import os

print(os.listdir(".."))
print(os.getlogin())
print(os.getpid())
os.pipe()
print(os.fork())

# if not os.path.exists("temp_dir"):
#     os.mkdir("temp_dir")
# os.chdir("./temp_dir")
# print(os.getcwd())
# os.chdir("..")
# os.rmdir("./temp_dir")
# sys.exit(1)

