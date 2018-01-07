places = ['shanghai', 'beijing', 'wuhan', 'shenzhen', 'changsha']

print("Here is original list:")
print(places)

print("\nHere is sorted list:")
print(sorted(places))

print("\nHere is original list: ")
print(places)

sorted_places = sorted(places)
sorted_places.reverse()
print("\nHere is sorted list in reverse:")
print(sorted_places)

print("\nHere is original list:")
print(places)

places.reverse()
print("\nHere is original list in reverse:")
print(places)

places.reverse()
print("\nHere is original list:")
print(places)

places.sort()
print("\nHere is sorted list forever:")
print(places)

places.sort(reverse=True)
print("\nHere is sorted list forever in reverse:")
print(places)
