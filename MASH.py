import re
import random
import sys



def categories(textline):
    expression = r'''(?P<name>^[A-Z]{1}\w+,\s[A-Z]{1}\w+)\s(?P<kids>\d+)\s(?P<transportation>[A-Z]{1}[a-z]+)\s(?P<pet>[a-z]+)\s(?P<place>[A-Z][a-z]+)'''
    
    search_regex = re.search(expression,textline)
    return search_regex.group(3)
    
    
def separate(textline):
        name = list(filter(lambda v: re.match('[A-Z][a-z]+,\s[A-Z][a-z]+',v)))
        kids = list(filter())
  
random_list = []  
with open("MASH.txt","r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        random_list.append(categories(line))
print(random_list)
    
    