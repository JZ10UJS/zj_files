s = 'tjurilli'
count = 1
bigcount = 1
lct = 0
for i in range(len(s)-1):
    if(i != len(s)-2):
        if s[i] <= s[i+1]:
            count += 1
            #print '1:',count
        else:
            st = count
            count = 1
            if bigcount < st:
                bigcount = st
                lct = i
                #print'bigcount is:',bigcount
    else:
        if s[i] <= s[i+1]:
            count += 1
            #print '2:',count
            st = count
            count = 1
            if bigcount < st:
                bigcount = st
                lct = i+1
                #print'bigcount is:',bigcount
        else:
            #print'3:',count
            st = count
            count = 1
            if bigcount < st:
                bigcount = st
                lct = i
                #print'bigcount is:',bigcount
print s[lct-bigcount+1:lct+1]
