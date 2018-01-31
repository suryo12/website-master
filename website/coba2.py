from datetime import datetime
import datetime as dt

#for x in range(1, 30):
#    print "We're on time %d" % (x)

for i in xrange(1,5)
    date=datetime.datetime(2003,8,i,12,4,5)
    print date

now = datetime.now()
print(now)

delta = dt.timedelta(hours=5)
print(delta)

myGlobal = 5

def func1():
    myGlobal = 42

def func2():
    print myGlobal

func1()
func2()

foo = 1
def test():
    foo = 2 # new local foo
print (foo)

def blub():
    global foo
    print foo # changes the value of the global foo

print foo
