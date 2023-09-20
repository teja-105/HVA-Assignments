from datetime import datetime

def python(teja):
    time = datetime(teja.year, i, j)
    remain = time - teja

    print(remain, "left for your birthday")
def java(teja):
    time = datetime(teja.year+1, i, j)
    remain = time - teja

    print(remain, "left for your birthday")


teja = datetime.today()

l = input("enter your birthday (YYYY-MM-DD) : ").split('-')
i = int(l[1])
j = int(l[2])


today = datetime.now()
if today.month > i:
    a = java(teja)
else:
    a = python(teja)