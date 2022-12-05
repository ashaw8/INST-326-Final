import re
import random
import sys



"""def categories(textline):
    expression = r'''(?P<name>^[A-Z]{1}\w+,\s[A-Z]{1}\w+)\s(?P<kids>\d+)
    \s(?P<transportation>[A-Z]{1}[a-z]+)
    \s(?P<pet>[a-z]+)\s(?P<place>[A-Z][a-z]+)'''
    for i in textline:
        print(i)
        search_regex = re.search(expression, i)"""
    
    
def separate(textline):
    kids = list(filter(lambda k: re.match('\d+', k), textline))
    transportation = list(filter(lambda t: re.match('[A-Z][a-z]+'), textline))
    pet = list(filter(lambda p: re.match('[a-z]+'), textline))
    place = list(filter(lambda e: re.match('[A-Z][a-z]+'), textline))
    
    
  
random_list = []  
with open("MASH.txt","r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        random_list.append(line)
#categories(random_list)
separate(random_list)


    