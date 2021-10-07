import stack


string = "nole si yrev taerg"

reversed_string = ""

s = stack.Stack()

# your solution here

for char in string:
    s.push(char)


while not s.is_empty():
    reversed_string += s.pop()

# while not s.is_empty():
#     reversed_string += s.pop()

    

# split in character
# pop
# append to reversed_string

print(s)
print(reversed_string)