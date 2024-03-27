import sys

sys.path.append("")#Path you have any module

import modules as m

courses = ['Art', 'History', 'Math', 'Chemistry']

index = m.find_index(courses, 'Math')
print(index)

print(sys.path)