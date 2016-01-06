class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    def insertAfter(frob1, frob2):
        '''
        assert before and after frob1 are all not None
        then put frob2 after frob1
        '''
        frob2.setAfter(frob1.getAfter())
        frob1.getAfter().setBefore(frob2)
        frob2.setBefore(frob1)
        frob1.setAfter(frob2)
        
    def insertBefore(frob1, frob2):
        '''
        assert before and after frob1 are all not None
        then put frob2 before frob1
        '''
        frob2.setBefore(frob1.getBefore())
        frob1.getBefore().setAfter(frob2)
        frob2.setAfter(frob1)
        frob1.setBefore(frob2)
    if atMe.getBefore() == None and atMe.getAfter() == None:
        l = [atMe.myName(), newFrob.myName()]
        l.sort()
        if l[0] == newFrob.myName():
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
    elif atMe.getBefore() == None and atMe.getAfter() != None:
        l = [atMe.myName(), newFrob.myName(), atMe.getAfter().myName()]
        l.sort()
        if l[0] == newFrob.myName():
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif l[1] == newFrob.myName():
            insertAfter(atMe, newFrob)
        else:
            insert(atMe.getAfter(), newFrob)
    elif atMe.getBefore() != None and atMe.getAfter() == None:
        l = [atMe.getBefore().myName(), atMe.myName(), newFrob.myName()]
        l.sort()
        if l[2] == newFrob.myName():
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif l[1] == newFrob.myName():
            insertBefore(atMe, newFrob)
        else:
            insert(atMe.getBefore(), newFrob)
    else:
        l = [atMe.myName(), atMe.getBefore().myName(), newFrob.myName(),atMe.getAfter().myName()]
        l.sort()
        if newFrob.myName() == l[1]:
            insertBefore(atMe, newFrob)
        elif newFrob.myName() == l[2]:
            insertAfter(atMe, newFrob)
        elif newFrob.myName() == l[0]:
            insert(atMe.getBefore(), newFrob)
        else:
            insert(atMe.getAfter(), newFrob)

def findFront(start):
    if start.getBefore() == None:
        return start.myName()
    else:
        return findFront(start.getBefore())

test_list = Frob('allison')
insert(test_list, Frob("lyla"))
insert(test_list, Frob("christina"))
insert(test_list, Frob("ben"))
