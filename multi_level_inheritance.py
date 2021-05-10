class Parent():
    def parent(self,name):
        self.name= name

    def show_name(self):
        return self.name

class Child():
    def child(self,age):
        self.age=age

    def show_age(self,age):
        return self.age

class Grand():
    def grand(self,height):
        self.height=height

    def show_height(self):
        return self.height

c1=Grand()
c1.height(67)
c1.name("nnn")

c1.show_height()
c1.show_age()
c1.show_name()


