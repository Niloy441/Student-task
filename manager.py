
import json,random
from task import Task

class Manager:

    def __init__(self,fn="time.json"):
        self.fn=fn
        self.data=[]
        self.load()

    def load(self):
        try:
            with open(self.fn,"r") as f:
                self.data=json.load(f)
        except:
            self.data=[]
            self.save()

    def save(self):
        with open(self.fn,"w") as f:
            json.dump(self.data,f,indent=3)

    def add(self,title,des):
        try:
            i=random.randint(100,999)
            t=Task(i,title,des)
            self.data.append(t.dic())
            self.save()
            return True
        except:
            return False

    def show(self):
        if len(self.data)==0:
            print("\nNo Task Found\n")
        else:
            for a,b in enumerate(self.data):
                print(f"{a+1}. {b['title']} - {b['desc']} ({b['created']})")

    def update(self,index,newt,newd):
        try:
            self.data[index]["title"]=newt
            self.data[index]["desc"]=newd
            self.save()
            return True
        except:
            print("titel real value")
            return False

    def delete(self,i):
        try:
            self.data.pop(i)
            self.save()
            return True
        except:
            print("vul task number ")
            return False
