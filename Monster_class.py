# monster class
class Monster():

    # strength range from 1-10 with 10 being the strongest.

    # create characteristics, using special method '__init__'. scary skill make to be a list.
    def __init__(self, name, strength, pay, scary_skills=None):
        self.name = name
        self.strength = strength
        self.pay = pay
        if scary_skills is None:
            scary_skills = []
        else:
            self.scary_skills = scary_skills

    #do behaviours (Methods defined here)
    def eat(self, food = ''):
        return "My favourite food is " + food

    def sleep(self):
        sleep_hours = int(self.strength * 0.6)
        return f'tiredness kills, i sleep {sleep_hours}hrs a day.'

    #how much tax paid relating to monster
    def pay_taxes(self):
        if self.pay > 50000:
            self.tax = 0.3
        elif 35000 >= self.pay >= 50000:
            self.tax = 0.2
        else:
            self.tax = 0.1
        tax_to_gov = int(self.pay * self.tax)
        return f'my taxes go towards the NHS for better equipment for monsters! I pay ${tax_to_gov}, to government.'

    def shout_strength(self):
        return self.strength * 1.1

    #adds scary skills to list
    def add_scary_skill(self, scary_sk):
        if scary_sk not in self.scary_skills:
            self.scary_skills.append(scary_sk)

    #removes scary skill to list
    def remove_scary_skill(self, scary_sk):
        if scary_sk not in self.scary_skills:
            self.scary_skills.remove(scary_sk)

    #prints scary list in conventional format
    def list_scary_skill(self):
        for scary_sk in self.scary_skills:
            return('scary skills:  ', scary_sk)




