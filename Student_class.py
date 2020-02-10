# I need to inherit from Monster class
from Monster_class import Monster

# Do student monster class
class Student(Monster):

    #create characteristics
    def __init__(self, name, strength, uni_id, scary_subjects=[]):
        super().__init__(name, strength, pay=0) #scary method most useful
        self.uni_id = uni_id
        self.tiny_debt = 0
        self.__debt = 0         #'__' <-- double underscore makes this private and python doesnt allow this to run, ora '_' makes it less visible
        self.__scary_subjects = scary_subjects

    #create behaviours (methods)

    def setter_debt_attribute(self, amount): #internal methods, have access to the ecapsulation
        self.__debt = amount

    def get_debt_value (self):
        # # security check
        input('what is your login')
        input('what is your password')
        return self.__debt

    def eat(self):
        #allows you to run parent class methods or attributes
        #super().eat() # this will ran both statments.
        return 'They say I am a student eating'

    def pay_taxes(self):
        return 'I earn less then $10000 per annum so i pay no taxes!!'

    def learn(self):
         return 'is scaring a person actually the best way to harness energy from a human?..'

    def party(self):
         return "WAIT....Am i the only monster who came uni just to party?"

    def uni_shopping(self):
         return 'I got the best price match for a loaf bread between Tesco and Asda'

    def setter_scary_subject(self, scary_sbj):
        self.__scary_subjects = scary_sbj

    def add_scary_subject(self, scary_sub):
        if scary_sub not in self.__scary_subjects:
            self.__scary_subjects.append(scary_sub)

    def remove_scary_subject(self, scary_sub):
        if scary_sub in self.__scary_subjects:
            self.__scary_subjects.remove(scary_sub)

    def list_scary_subjects(self):
        #return self.__scary_subjects
        for scary_sub in self.__scary_subjects:
            return 'scary subjects:  ', scary_sub    #if used print, a none statement will

    def list_first_scary_subject(self):
        return self.__scary_subjects[0]
    # for scary_sub in self.__scary_subjects:
    #     return 'scary subjects:  ', scary_sub     #if used print, a none statement will



mike = Student('Mike', 'weak', 1011, ['Power Of Scream', 'Avoiding Human Contact'])
print(mike.list_scary_subjects())

#mike.add_scary_subject('science')
#print(mike.list_scary_subjects())

#print(mike.list_first_scary_subject())