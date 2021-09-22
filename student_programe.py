import Student_class as sc

studentid=1001
name='john'

dob= '10/15/2001'
classification='junior'
John=sc.Student(studentid,name,dob,classification)
John.register()
print("student age is:",John.return_age())
print("Student can register between:",John.return_register())


