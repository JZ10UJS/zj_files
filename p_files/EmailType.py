import re

def check():
    usr_email =''
    sd_email = r'^\w+@.+(.com|.cn)$'
    list1 = re.findall(sd_email,usr_email)
    while len(list1) == 0:
        usr_email = raw_input('Please input your email:')
        list1 = re.findall(sd_email,usr_email)
    print "that's right!'\n"

def goon():
    ctn = raw_input('Press Y/N to continue/close:')
    if ctn == 'y' or ctn == 'Y':
        check()
        goon()
    elif ctn == 'N' or ctn == 'n':
        pass
    else:
        print 'Please input again!'
        goon()
check()
goon()
    
