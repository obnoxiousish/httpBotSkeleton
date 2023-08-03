class Work:
    def __init__(self, session):
        self.session = session
    
    async def start(self):
        return await self.session.get('https://google.com')
        
if __name__ == "__main__":
    print('Start main.py, this is only for editing!')