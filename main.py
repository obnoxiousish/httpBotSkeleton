"""
Author: obnoxious
About: This is a simple script that assists in creating an HTTP bot
"""
import httpx
import trio
import queue

# our files
from settings import Settings
from account import Accounts
from proxy import Proxies

# this where we import the user edited part
from bot import Work

class main:
    def __init__(self):
        self.Q = queue.Queue()
        self.settings = Settings()
        self.accounts = Accounts()
    
    # "thread" starter
    async def startThreads(self):
        async with trio.open_nursery() as nursery:
            for _ in range(self.settings.threads):
                nursery.start_soon(self.threadLoop)    
            
            return True

    # this is the main loop for the "threads"
    async def threadLoop(self):
        while not self.Q.empty():
            newTask = self.Q.get()
            completedTask = await self.threadWork(newTask)
            self.Q.task_done()
            
        return True
            
    # this is the actual work code, but it calls bot.py's work() function to create an easy location to insert the meat of the code
    async def threadWork(self, task):
        async with httpx.AsyncClient(verify=False, proxy=Proxies.getRandom()) as session:
            self.session = session
            self.setupSession()
            
            userCode = Work(session)
            userCodeResults = await userCode.start()
            print(userCodeResults)
            return userCodeResults

    def setupSession(self):
        self.session.headers.update(
            {
                #'authority': 'facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            }
        )

if __name__ == "__main__":
    mn = main()
    trio.run(main.startThreads, mn)