class Parent1():
    def father(self , father):
        self.father=father

    def show_father(self):
        print("Father",self.father)

class Parent2():
    def mother(self, mother):
        self.mother = mother

    def show_mother(self):
        print("Mother", self.mother)

class Child(Parent1 , Parent2):
    def child(self, child):
        self.child= child
    def show_child(self):
        print("Child",self.child)

c1=Child()
c1.father("Velumani")
c1.mother("Maheshwari")
c1.child("Niveda")

c1.show_father()
c1.show_mother()
c1.show_child()
