from codecs import open
from random import choice

class Proxies:
    def __init__(self, proxyFile='proxies.txt'):
        self.proxyList = open(proxyFile, 'r', 'utf-8', errors='ignore').readlines()
        self.proxySet = set()
        
        for proxy in self.proxyList:
            self.proxySet.add(proxy.strip())
            
        self.proxyList = list(self.proxySet)
            
    def getRandom(self):
        return choice(self.proxyList)
    
    def getFirst(self):
        return self.proxyList[0]
    
if __name__ == "__main__":
    print('This is a module.')