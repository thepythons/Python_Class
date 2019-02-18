words="a=b;c=d;e=f;g=h"
split_list=words.split(";")
new_list=[]
for i in split_list:
	t=tuple(i.split("="))
	new_list.append(t)
print(new_list)
