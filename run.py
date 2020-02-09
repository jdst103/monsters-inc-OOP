#Import the Parent class Monster  from python file monster_class

from Monster_class import Monster

#import baby class Student from python file student_class
from Student_class import Student

# print(help(Monster)) <-- gives help on class Monster
# print(help(Student)) <-- gives help on class Student


#creating a instance of the class Monster
mr_sly = Monster('Mr Sly', 9, 45000, ['slyness'])
ms_Boat = Monster('Ms Boat', 4, 60000, '[power]')

#calling monster instances
print(ms_Boat.pay_taxes())
print(mr_sly.list_scary_skill())
print(ms_Boat.sleep())

#creating an instance of the class Student
sully = Student('Sully', 'strong', 1010, ['Element of surprise', 'Biology of Humans'])
mike = Student('Mike', 'weak', 1011, ['Power Of Scream', 'Avoiding Human Contact'])

#calling student instances
mike.add_scary_subject('science')
print(mike.list_scary_subjects())

mike.remove_scary_subject('maths')
print(mike.list_scary_subjects())