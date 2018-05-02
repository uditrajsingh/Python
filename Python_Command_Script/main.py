from lib import *


def initiate():
    print "Python command line [version v2.7.14:84471935ed]"
    print "last open on " + getCurrentDateTime() + "\n"
    storeCurrentDateTime()
    

def storeCurrentDateTime():
    file = open("db.txt", "w")
    file.write(str(datetime.datetime.now()))
    file.close()

def getCurrentDateTime():
    file = open("db.txt", "r")
    l = str(file.read())
    file.close()
    return l
