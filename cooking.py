
#!/usr/bin/python3.6

"""
@Authors : Kiran, Vashnavi, Moeen

File preprocessing
Use following command on the layer1.json file
sed 's/,$//' layer1.json > file.nocomma (this will remove all comma from the end of each line)
awk '(NR>1 && NR<1029722) {print}' file.nocomma > file.nocomma1 (This will remove first and last line)
Then give this file.nocomma1 as an input
It would be  better if we can do it within python.

This simple script will search for any of the given key-words for 'course-category' which I think will 
be a good "target" value. This also delete url, partition and instruction entries.
"""


import sys
import json
#import numpy as np
#import matplotlib.pyplot as plt


# Function to drop unneessary entry
def keep_info(data):
    
    for entry in data:
        entry.pop('url', None)
        entry.pop('partition', None)
        entry.pop('instructions', None)
        
    return data


def main(input):
    
    #keywords = ('dessert', 'main-course', 'snack', 'beverage', 'soup', 'bread',
     #           'salad', 'appetizer', 'side-dish')
    
    keep_json=[]
    
    with open(input, "r") as read_file:
        for line in read_file:
            #parsed_json.append(json.loads(line))
            parsed_json = json.loads(line)
            # Convert to string for keyword search
            str1 = str(parsed_json)

            ## The follwoing command is very clean but I do not know how to extract 'key' value
            ## because that will be the VALUE for 'course-category' KEY

            #if any(key in str1 for key in keywords):
             #   keep_json.append(parsed_json)
            
            ## So I am using this repetitive approach!!!

            if ('appatizer') in str1:
                parsed_json['course_category'] = 'appatizer'
                keep_json.append(parsed_json)
            elif ('salad') in str1:
                parsed_json['course_category'] = 'salad'
                keep_json.append(parsed_json)
            elif ('side-dish') in str1:
                parsed_json['course_category'] = 'side-dish'
                keep_json.append(parsed_json)
            elif ('main-course') in str1:
                parsed_json['course_category'] = 'main-course'
                keep_json.append(parsed_json)
            elif ('snack') in str1:
                parsed_json['course_category'] = 'snack'
                keep_json.append(parsed_json)
            elif ('beverage') in str1:
                parsed_json['course_category'] = 'beverage'
                keep_json.append(parsed_json)
            elif ('soup') in str1:
                parsed_json['course_category'] = 'soup'
                keep_json.append(parsed_json)
            elif ('bread') in str1:
                parsed_json['course_category'] = 'bread'
                keep_json.append(parsed_json)
            elif ('dessert') in str1:
                parsed_json['course_category'] = 'dessert'
                keep_json.append(parsed_json)
            
        ## Drop entry 
        keep_json = keep_info(keep_json)
    

   # Write in a new json file
    with open('out1.json', 'w') as outfile:
       json.dump(keep_json, outfile, sort_keys=True, indent=4)
       
       

if __name__ == '__main__':
    input = sys.argv[1]
    main(input)