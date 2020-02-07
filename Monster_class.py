# Do monster class

class Monster():

    # create characteristics
    def __init__(self, name, strength, scary_skills):
        self.name = name
        self.strength = strength
        self.scary_skills = scary_skills


    #do behaviours (Methods)
    def eat(self, food = ''):
        return "I'm hungrrrryyy can i eat" + food

    def sleep(self):
        return  "tiredness kills"

    def pay_taxes(self):
        return 'my taxes go towards the NHS for better equipment for monsters!'

    def shout_strength(self):
        return 'My shout strength is AAAAAAAAAAAMMMMM...'
