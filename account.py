from codecs import open
from random import shuffle
from queue import Queue

class Accounts:
    def __init__(self, combosFileName='accounts.txt', delimiter=':'):
        self.combosFileName = combosFileName
        self.delimiter = delimiter
        self.Q = Queue()
        self.accountSet = set() # no duplicates
        
        line = line.strip().rstrip()
        
        if '@' in line:
            self.email, self.password = line.split(delimiter)
        else:
            self.username, self.password = line.split(delimiter)
            
    def loadAccounts(self, returnSet=False):
        self.accountList = open(self.combosFileName, 'r', 'utf-8', errors='ignore').readlines()
   
        for acc in self.accountList:
            self.accountSet.add(acc.strip().strip())
            
        if returnSet: # if we want to return a set instead of a list
            return self.accountSet
        
        self.accountList = list(self.accountSet) # convert to a list for more functionality
            
        return self.accountList
    
    def putAccountsInQueue(self):
        for acc in self.accountList:
            self.Q.put(acc)
            
        return True
    
    def shuffleAccounts(self):
        shuffle(self.accountList)
        return self.accountList