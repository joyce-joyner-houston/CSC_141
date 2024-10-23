names = ['Jayla', 'Isaac', 'Messiah', 'Kyle']
message = f"Hello, {names[0].title()}"
print(message)

message = f"Hello, {names[1].title()}"
print(message)

message = f"Hello, {names[2].title()}"
print(message)

message = f"Hello, {names[3].title()}"
print(message)


def greet(name):
    print(f"Hello, {name}")

import greetings
greetings.greet('Jayla')

from greetings import greet
greet('Isaac')

from greetings import greet as fn
fn('Messiah')

import greetings as mn
mn.greet('Kyle')

from greetings import *
greet('Joyce')