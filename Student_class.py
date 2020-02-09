# I need to inherit from Monster class
from Monster_class import Monster

# Do student monster class
class Student(Monster):

    #create characteristics
    def __init__(self, name, strength, uni_id, scary_subjects=None):
        super().__init__(name, strength, pay=0)
        self.uni_id = uni_id
        if scary_subjects is None:
            scary_subjects = []
        else:
            self.scary_subjects = scary_subjects

    #create behaviours (methods)
    def learn(self):
         return 'is scaring a person actually the best way to harness energy from a human?..'

    def party(self):
         return "WAIT....Am i the only monster who came uni just to party?"

    def uni_shopping(self):
         return 'I got the best price match for a loaf bread between Tesco and Asda'

    def add_scary_subject(self, scary_sub):
        if scary_sub not in self.scary_subjects:
            self.scary_subjects.append(scary_sub)

    def remove_scary_subject(self, scary_sub):
        if scary_sub in self.scary_subjects:
            self.scary_subjects.remove(scary_sub)

    def list_scary_subjects(self):
        for scary_sub in self.scary_subjects:
            print('scary subjects:  ', scary_sub)


