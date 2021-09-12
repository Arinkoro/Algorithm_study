class Human():
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

class Student(Human):
    def __init__(self, name="", age=0):
        super().__init__(name, age)
        self.academic_ability = {}
    
    def study(self, subject):
        self.academic_ability.setdefault(subject, 0)
        self.academic_ability[subject] += 5
    
    def get_academic_ability(self):
        return self.academic_ability
    pass

def main():
    manA = Human("Taro", 32)
    # manA.set_name("Taro")
    name = manA.get_name()
    print(name)
    # manA.set_age(20)
    age = manA.get_age()
    print(age)
    studentA = Student("Taro", 32)
    for num in range(5):
        studentA.study("Japanese")
    for num in range(10):
        studentA.study("English")
    print(studentA.get_academic_ability())
    

if __name__ == '__main__':
    main()