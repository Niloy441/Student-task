
from datetime import datetime

class Task:
    def __init__(self,id,title,desc):
        self.id=id
        self.title=title
        self.description=desc
        self.time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dic(self):
        return {
            "id":self.id,
            "title":self.title,
            "desc":self.description,
            "created":self.time
        }
