class mammal:
    def walk(self):
        print("walk")

class dog(mammal):
   def bark(self):
       print("bark")

class cat(mammal):
    def annoy(self):
        print("annoy")


cat1=cat()
cat1.annoy()
mam=mammal()
mam.walk()
