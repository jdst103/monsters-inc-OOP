#Import the Parent class Monster  from python file monster_classd
from Monster_class import Monster

#import baby class Student from python file student_class
from Student_class import Student

#creating a instance of the class Monster
mr_sly = Monster('Mr Sly', 'average strength', 'slyness')
ms_Boat = Monster('Ms Boat', 'strong', 'power')

#creating an instance of the class Student
mike = Student(11, 'Element Of Surprise')
sully = Student(12, 'Power Of Scream')

#calling monster instances
print(ms_Boat.strength)
print(mr_sly.scary_skills)

#calling student instances
print(mike.learn())
print(sully.scary_subjects)

print(mike.eat())