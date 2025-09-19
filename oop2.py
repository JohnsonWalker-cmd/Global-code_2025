class Person:
    def __init__(self , name:str , gender:str , status:str , dob : str , age:int):
        self.name = name
        self.gender = gender
        self.status = status
        self.dob = dob
        self.age = age
        
        
    def speak(self):
        print(f"Hello my name is {self.name}")
        
        
    def walk():
        print("walking away")
        
        
    def get_name(self):
        return self.name 
    
    def get_age(self):
        return self.age
    
    
    
    
class Student(Person):
    def __init__(self, name , gender, status ,dob, age , courses=[]):
        super().__init__(name , gender, status ,dob, age)
        
        self.courses = courses
        
        
    def get_courses(self):
        return self.courses
    
    def speak():
        print("I'm so tired")
        
        
        
        
        
student1 = Student("JOhnson" , "M" , "Single", "23-06-2003" , 23 , ["Maths, Science"])

print(student1.get_courses())
print(student1.name)
