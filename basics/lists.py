#Lists, Tuples, Sets

courses = ['Art', 'History', 'Math', 'Comp Sci']
# print(len(courses))
# print(courses[-1]) #Accessing from end of the list

# print(courses[:2])

courses.append('Geography')
courses.insert(1, 'Physics')

courses_2 = ['Biology', 'Chemistry']
courses.extend(courses_2)
# print(courses)

courses.remove('Math')
popped = courses.pop()
# print(popped)

courses.reverse()
courses.sort(reverse=True) #Alters the list in place

nums = [1,8,3,7,5]
nums.sort()
# print(courses)
# print(nums)

sorted_courses = sorted(courses)
# print(sorted_courses)

#Min, Max, Sum is available

# print(sorted_courses.index('History'))
# print('Art' in courses)

# for item in enumerate(courses, start=11):
#     print(item)


# course_str = '-'.join(courses)
# print(course_str)

# new_list = course_str.split('-')
# print(new_list)


#Tuples and Sets

#Tuples are immutable, Lists are mutable

tuple_1 = ('Art', 'History', 'Math', 'Comp Sci')
tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Physics' #Gives an error

# print(tuple_1)
# print(tuple_2)

#Sets are unordered and non duplicate

set_1 = {'Physics', 'History', 'Math', 'CompSci'}
set_2 = {'Art', 'History', 'Math', 'Design'}

# print(set_1.union(set_2))
# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))


#Empty objects

empty_list = [] #or list()
empty_tuple = () #or tuple()
empty_set = set()

#{} will create empty dictionary
