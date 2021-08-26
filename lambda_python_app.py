import json

def nameToList(name):
    list_words = []
    for word in name:
        list_words.append(word.lower())
    return list_words

def sortedName(name):
    list_2 = nameToList(name)
    sorted_list = []
    while list_2:
        sorted_list.append(min(list_2))
        list_2.remove(min(list_2))
    return sorted_list

def lambda_handler(event, context):
    name = event['name']
    if len(name) < 20:
        list_words = nameToList(name)
        sorted_list = sortedName(list_words)
        return {
            'statusCode': 200,
            'body': {
                'name': name,
                'name_list': list_words,
                'name_sorted': sorted_list
            }
        }
    else:
        return "Strings longer than 20 charcters are not allowed"
