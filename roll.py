import random
import hashlib

ALPHABET="0123456789abcdefghijklmnopqrstuvwxyz"   # 36 symbols. throws from 1-1 to 6-6
    
def alphtothrow(alph):
    n=ALPHABET.index(alph)
    return [int(n/6)+1, n%6+1]

def throwtoalph(throw):
    (first, second) = throw
    first-=1
    second-=1
    return ALPHABET[first*6+second]

def randompermutation():
    x=[c for c in ALPHABET]
    res=""
    while (len(x)>0):
        i=random.randint(0,len(x)-1)
        c=x[i]
        res+=c
        x.remove(c)
        
    return res

def salt(n):
    res=''
    for i in xrange(n):
        res+=ALPHABET[random.randint(0,len(ALPHABET)-1)]
    return res

def hash(msg):
    return hashlib.sha256(msg).digest().encode('base64').strip()

class RollException(Exception):
    pass

class Roll():
    # roles: 'initiator' and participant
    # the initiator generates the commitment
    def __init__(self, role, commitment=None):
        if (role=='initiator'):
            self.role = role
            self.shuffle = randompermutation()
            self.shuffle+='['+salt(100)+']'
            self.commitment = hash(self.shuffle)
            self.chosenthrow = None

        if (role=='participant'):
            self.role = role
            self.commitment = commitment
            self.chosenthrow = random.randint(0,35)
            self.shuffle = None

    def check_shuffle(self):
        """checks if shuffle and commitment match
        checks if shuffle is complete"""

        #shuffle complete?
        for c in ALPHABET:
            if not (c in self.shuffle[0:36]):
                raise RollException("Shuffle doesn't contain all throws")
            if (hash(self.shuffle) != self.commitment):
                raise RollException("Shuffle doesn't match the commitment")

    def set_shuffle(self, shuffle):
        if (self.role != 'participant'):
            raise RollException("the shuffle cannot be set on the initiator")
        self.shuffle = shuffle

    def get_throw(self):
        if (self.shuffle == None):
            raise RollException("Not rolled yet")
        self.check_shuffle()
        return alphtothrow(self.shuffle[self.chosenthrow])

