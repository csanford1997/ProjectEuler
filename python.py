#TestDrive
#def problem():
    #return sum(x for x in xrange(1,1000) if x%3 == 0 or x& 5 == 0)
"""
sum = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        sum += i
print sum
"""
count = 1
#while (count < 101):
limit = int (input("Give me an upper limit"))
for i in range(limit):
    if (count % 5) == 0 and (count % 3) == 0:
        print "fizzbuzz"
        count = count +1
    elif (count % 3) == 0:
        print "fizz"
        count = count + 1
    elif (count % 5) == 0:
        print "buzz"
        count = count +1
    else:
        print count
        count = count + 1

