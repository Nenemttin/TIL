from darksky import forecast

multicampus = forecast('c8f5585bd3f5ef841ee41709e398bd33', 37.501579, 127.039713)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])