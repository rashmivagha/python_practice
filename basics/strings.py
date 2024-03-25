#Strings
message = "Hello World"
message2 = """Hello World
I am so happy to be here""" #triple quotes for multiline


print(message.lower()) #upper() also
print(message.count("l"))
print(message.find("l"))

message2 = message.replace("World", "there")
print(message2)

greeting = "Hello"
name = "Rashmi"

message = greeting + ", " + name + ". Welcome" 

print(message)

#Formatted string

message = f'{greeting}, {name}, Welcome!'
print(message)

print(dir(message))
print(help(str))