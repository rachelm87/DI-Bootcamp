import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__)) 
#convert a dict to a json file
my_family = {
    'parents':['Beth', 'Jerry'],
    'children':['Summer', 'Morty']
}

#with open(f'{dir_path}/family.json', 'w', encoding='utf-8') as f:
#    json.dump(my_family, f)
#convert a dict to a json string
json_my_family_string = json.dumps(my_family)
print(json_my_family_string)

#convert from a json file to a dict
with open(f'{dir_path}/family.json', 'r', encoding='utf-8') as f:
    my_family2 = json.load(f)
print(type(my_family2))

#convert from a json string to a dict
parsed_famiy =json.loads(json_my_family_string)
print(type(parsed_famiy))
