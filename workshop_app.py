print('Hello World!')

flag = True

while flag:

	name_s = input('What is your name?: ')

	print('Hello ' +  name_s)

	list_words = []
	for w in name_s:
		list_words.append(w)
	print("Your name in a list " + str(list_words))

	list_name = []
	while name_s:
		name_s = name_s.lower()
		list_name.append(min(name_s))
		name_s = name_s.replace(min(name_s), '')
	print("Your name sorted alphabetically " + str(list_name))
	
	answer = input('Do you want to try it again?(y/n)')
	if answer == 'y':
		flag = True
	else:
		flag = False
		print('Bye!!!')