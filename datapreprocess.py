#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:01:36 2018

@author: vaishnavimalhotra
"""

import sys
import json, re

# Function to drop unneessary entry
def keep_info(data):
    for entry in data:
        entry.pop('url', None)
        entry.pop('partition', None)
        entry.pop('instructions', None)
        
    return data

# Function to clean ingredients, remove measurements
def getIngredients(data):
    ingredients = []
    # measurement words
    mwords = ('cup ','tablespoon ','tsp ','tbsp. ','c. ','grams ','ounces ','tablespoons ','can ', 'ounce ', 
              'cups ', 'teaspoon ','teaspoons ','graham ', 'lb ','lb. ','lbs ', 'ml ', 'cc. ', 'cc ')
    for key in data:
        # Remove brackets and its contents from ingredient strings
        text = re.sub(r" ?\([^)]+\)", "", key['text'])
        for word in mwords:
             if word in text:
                 # since measurements appear in beginning, second half od text is retained
                 text = text.split(word)[1]
        # Remove digits from ingredients to avoid cases like '1 cabbage'
        ingredients.append(''.join([i for i in text if not i.isdigit()]))
    #print(ingredients)
    #print('-------------------')
    return ingredients
               
def main():
    
    keywords = ('dessert', 'main-course', 'snack', 'beverage', 'soup', 'bread', 'salad', 'appetizer', 'side-dish','corn')
    keep_json=[]
    
    with open('data/dummylayer.json', "r") as read_file:
        data = json.load(read_file)
    
    for i in range(len(data)):
        category = 'others'
        
        # remove measurements from ingredients
        data[i]['ingredients'] = getIngredients(data[i]['ingredients'])
        
        # Identify category of food
        for word in keywords:
            if word in str(data[i]).lower():
                  category = word
        #add category field in json
        data[i]['category'] = category
    
    # Remove fields from json
    keep_json = keep_info(data)
    #print(keep_json)
    
    # Write in a new json file (Contents are over-written if file already created)
    with open('output/out1.json', 'w') as outfile:
       json.dump(keep_json, outfile, sort_keys=True, indent=4)
        

       

if __name__ == '__main__':
    #input = sys.argv[1]
    main()
