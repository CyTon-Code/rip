#!/bin/python
from random import random
print(random())
#  import random
rips = []

def save():
    save = ""
    for links in rips:
        for link in links:
            save += link +  " "
        if [] != links:
            #  print(['1','1','1','1','1','1'].strip('as'))
            print('1'.strip('as'))
            save += "\n"
    with open("list", "w") as f:
        f.write(save)

def load():
    global rips
    with open("list") as f:
        rips = [i.split() for i in f.read().split("\n")]
    pass

def rip(link, to_link=""):
    if not to_link:
        to_link = str(__import__("random").random())
    if __import__("os").system("mv " + link + " rip/" + to_link)//256:
        raise Exception()
    pass

def back():
    pass

def get(original_link):
    for i in rips:
        pass
    pass

def echo():
    print(rips)
echo()
load()
echo()
save()
rip("test")
