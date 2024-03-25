#Functions

# def hello_func(greeting, name = 'You'):
#     return '{}, {} Function'.format(greeting, name)

# print(hello_func("hi", "Rashmi"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Math', 'Art')
info = {'name': 'Sam', 'age': 27}
student_info(*courses, **info)