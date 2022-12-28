#A simple program to convert miles to kilometres and vice versa
#Currently you can only convert km to miles by doing miles to km first

mi = int(input("Input your distance in miles: "))
kilom = mi*1.609
print("Miles to KM:" , kilom)
print()
km = int(input("Input your distance in KM: "))
miles = km*0.609
print("KM to Miles:" , miles)