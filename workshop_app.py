print("Hello World!")

answer = True

while answer:
    name = input("What is your name?")
    if name == 'Emmanuel':
        print("Hello " + name + "!")
    else:
        print("Hello stranger!")
    list_words = []
    for word in name:
        list_words.append(word.lower())
    print("Your name in a list " + str(list_words))
    sorted_list = []
    while list_words:
        sorted_list.append(min(list_words))
        list_words.remove(min(list_words))
    print("Your name sorted alphabetically " + str(sorted_list))
    answer = input('Do you want to try it again?(y/n)')
    if answer.lower() != 'y':
        print('Bye!!!')
        break