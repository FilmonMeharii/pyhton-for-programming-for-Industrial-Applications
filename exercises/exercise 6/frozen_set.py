students = frozenset(['Ali', 'Bo', 'Carl', 'David', 'Emma', 'Frida'])
present = frozenset(['Carl', 'David'])
leave = frozenset(['Ali', 'Emma'])
sick = frozenset(['Frida'])

absent = students - present
AWOL = absent - (leave | sick)

print(f"Absent: {absent}")
print(f"AWOL: {AWOL}")