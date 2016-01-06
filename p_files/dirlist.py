filename = raw_input('input your filename:')
try:
    f = open(filename)
    print hello
except IOError,msg:
    print 'no such file,please check it out'
except NameError,msg:
    print 'no such file,fuck off'
finally:
    print 'ok'
print 'over'

f.close()
print "that's all"


