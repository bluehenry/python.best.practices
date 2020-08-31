import numpy as np

results = {}
results['A'] = np.zeros((7, 48))
results['B'] = np.zeros((7, 48))
results['C'] = np.zeros((7, 48))

longitude = 119.800631

print(str(longitude))

list_mapping = {
    "119.931418": 'A',
    "119.800631": 'B',
    "119.796352": 'C',
}


print(list_mapping.get(str(longitude)))



results[list_mapping.get(str(longitude))][0][0] += 1
print(results['B'][0][0])

for carpark in results:
    print(carpark)
    print(results[carpark])