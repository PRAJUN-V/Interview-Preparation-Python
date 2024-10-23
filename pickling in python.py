import pickle

d = {'name': 'Praju', 'age': 23}

# Pickling
with open('data.txt', 'wb') as f:
    pickle.dump(d, f)

# Unpickle
with open('data.txt', 'rb') as f:
    print(pickle.load(f))
