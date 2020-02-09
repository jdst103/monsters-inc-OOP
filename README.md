# MONSTER INC

In this task, we worked on using inheritance  in classes. the example given in this project has relationd to Monster inc.
Monsters being the parent class and students being the baby class.

Learning Objectives:
- Pushing project on GitHub and Git
- Created Markdown file
- How to implement inheritance class
- How to call an instance from these classes
- Using seperation of concerns
- using super(). to reduce repeating code

To create a inheritance class, 

````
class Inheritance_class(Parent_Class):
````
In this example its: 
````
class Student(Monster):
````

To define its characteristics where we use a constructor method:
```
    def __init__(self, arg1, arg2)
        self.arg1 = arg1
        self. arg2 = arg2
```
In monster terms!!:
```
    def __init__(self, name, strength, pay, scary_skills=None):
        self.name = name
        self.strength = strength
        self.pay = pay
        if scary_skills is None:
            scary_skills = []
        else:
            self.scary_skills = scary_skills
````
we have access to the instance of the class via the self. self is the instance/occurance of the class.

scary_skills is equal to **none** as its prefered not to make the parameters mutable. the scary list is equal to a lis
so we can add and remove items per monster. 

the following method was used to add skills to this list:
````
    def add_scary_skill(self, scary_sk):
        if scary_sk not in self.scary_skills:
            self.scary_skills.append(scary_sk)
````

Another method called list_scary_skills listed these items in convetional way.


instances for the class was defined like below for the student class.
````
sully = Student('Sully', 'strong', 1010, ['Element of surprise', 'Biology of Humans'])
````

These instances was called using print(). 