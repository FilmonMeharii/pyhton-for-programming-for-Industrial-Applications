

students = {'Ali', 'Bo', 'Carl', 'David', 'Emma', 'Frida'}
present = {'Carl', 'David'}
leave = {'Ali', 'Emma'}
sick = {'Frida'}
absent = students - present  
AwOL = absent -(leave | sick)
print("Absent:", absent)
print("AwOL:", AwOL)