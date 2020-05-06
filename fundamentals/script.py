import sys

print(sys.version)
print(sys.executable)

def greet(whomeToGreet): 
    greeting = 'Hello, {}'.format(whomeToGreet)
    return greeting

print(greet('World'))