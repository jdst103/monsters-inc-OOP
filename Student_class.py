# i need to inherit from Monster class
from Monster_class import Monster

# Do student monster class
class Student(Monster):

    #create characteristics
    def __init__(self,uni_id, scary_subjects):
        self.uni_id = scary_subjects
        self.scary_subjects = scary_subjects


    # create behaviours (methods)
    def learn(self):
        return 'is scaring a person actually the best way to harness energy from a human?..'

    def party(self):
        return "WAIT....Am i the only monster who came uni just to party?"

    def uni_shopping(self):
        return 'I got the best price match for a loaf bread between Tesco and Asda'


