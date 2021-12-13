class Student:
    count=0;
    def getdata(self,roll,name,course):
        self.roll=roll;
        self.name=name;
        self.course=course;
        Student.count=Student.count+1;
    def displaycount():
        print("no of students=",Student.count);
    def display(self):
        print("roll no=",self.roll);
        print("name=",self.name);
        print("course=",self.course);
s1=Student();
s2=Student();
s1.getdata(101,"anu","mca");
s2.getdata(102,"abhi","mca");
s1.display();
s2.display();
Student.displaycount();
        
        
