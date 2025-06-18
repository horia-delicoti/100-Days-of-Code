from collections import namedtuple

user = ('bob', 'coder')

print(type(user))

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')

print(user.name)

print(f'{user.name} is a {user.role}') 