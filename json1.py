import json


data = { "name": "Mayo Ebg",
        "age": 29,
        "city": "Renton, WA", 
        "interests": ["God", "Eat", "Help", "Kids"], 
        "is student": True 
        }

#write data to JSON file
with open('data.json', 'w') as json_file: # w for write
    json.dump(data, json_file, indent=4) #dump helps object to be written in JSON format with 4 indents
    print('Data written to data.json') #print this message once use.

#create function to read the data from the JSON file
with open('data.json', 'r') as json_file: # r for read/reading
    loaded_data = json.load(json_file) #create an object to load the indicated variable
    print('Data loaded from data.json:') #print this message
    print(loaded_data) #print the casteded variable

#call loaded data in the key value pair to edit
loaded_data['age'] = 29
#append into the interest array with the correct key
loaded_data['interests'].append("Congo is the Richest Country")

#use with statement to modify the code in the json file
with open('data.json', 'w') as json_file: # w for writing
    json.dump(loaded_data, json_file, indent=4) #dump helps object to be written in JSON format with 4 indents
    print('Modified data to data.json file') #print this message
