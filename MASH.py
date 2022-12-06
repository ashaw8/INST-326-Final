import re
import random
import sys



def categories(textline, option):
    expression = r'''(?P<name>^[A-Z]{1}\w+,\s[A-Z]{1}\w+)\s(?P<kids>\d+)\s(?P<transportation>[A-Z]{1}[a-z]+)\s(?P<pet>[a-z]+)\s(?P<place>[A-Z][a-z]+)'''
    search_regex = re.search(expression,textline)
    return search_regex.group(2)
    
    

def open_file(textfile):  
    random_list = []  
    with open(textfile,"r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            random_list.append(line)
    return random_list

def pass_regex():
    stored = open_file("MASH.txt")
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for line in stored:
        list1.append(categories(line, 1))
        list2.append(categories(line, 2))
        list3.append(categories(line, 3))
        list4.append(categories(line, 4))
        list5.append(categories(line, 5))
        
    return [random.choice(list1),random.choice(list2),random.choice(list3),random.choice(list4),random.choice(list5),]

print(pass_regex())
