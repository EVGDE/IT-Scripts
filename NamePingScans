import os, pathlib

f = open('Test.txt', 'w')

for i in os.listdir():
    filename = pathlib.Path(i)
    filename = filename.stem
    print(filename)
    response = os.system("ping -c 1 -w 1 " + filename + " >/dev/null")
    if response == 0:
        print(filename + " is up")
        f.write(filename + " is up \n")
    else:
        print(filename + " is down")
        f.write(filename + " is down \n")
f.close()
