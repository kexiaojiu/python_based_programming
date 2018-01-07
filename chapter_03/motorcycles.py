motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'abc')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_mptorcycle = motorcycles.pop()
print(motorcycles)
print(popped_mptorcycle)

motorcycles.remove('ducati')
print(motorcycles)
