# list to string
li = [('a','b'),('c','d'),('e','f'),('g','h')]
si = []
for i in li:
	string='='.join(i)
	si.append(string)
word=';'.join(si)
print('String:" {}"'.format(word))

# list to dictionary

li = [('a','b'),('c','d'),('e','f'),('g','h')]
my_dict= {}
for i in li:
	my_dict[i[0]]=i[1]
print('Dictionary:' ,my_dict)
