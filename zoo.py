zoo = ('monkey', 'dog', 'cat')

print(zoo.index('monkey'))

if 'monkey' in zoo:
	print('There is a monkey in the zoo')

(george, bob, fav) = zoo
print(fav)

zoo_list = list(zoo)
zoo_list.extend(['bird', 'octopus'])
print(zoo_list)
zoo = tuple(zoo_list)
print(zoo)
