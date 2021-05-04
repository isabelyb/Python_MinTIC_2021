# Develop a function

def short_greeting(name):
    return "Hello, {}!".format(name)

# get user name

name = input("Ingrese su nombre: ")

sentence = short_greeting(name) 

print(sentence)


def long_greeting(name):
    return "Hello, {}! How are you today?".format(name)

# get user name

name = input("Ingrese su nombre: ")

sentence = long_greeting(name) 

print(sentence)



