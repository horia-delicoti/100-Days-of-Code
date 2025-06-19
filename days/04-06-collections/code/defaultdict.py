from collections import defaultdict

users = {'bob': 'coder'}

print(users['bob'])
#print(users['alice'])  # Raises KeyError

users.get('bob')
users.get('julian') is None # Returns None

challenge_done = [('mike', 10), ('bob', 20), ('mike', 30), ('alice', 40), ('bob', 50), ('alice', 60)]

challenges = {}

# Raise KeyError if key does not exist
#for name, challenge in challenge_done:
#    challenges[name].append(challenge)

# Use defaultdict to avoid KeyError
challenges = defaultdict(list)
for name, challenge in challenge_done:
    challenges[name].append(challenge)

print(challenges)
