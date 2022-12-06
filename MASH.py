import re
import random
import sys
import pandas as pd
import matlibplot.pyplot as plt



def categories(textline, option):
    expression = r'''(?P<name>^[A-Z]{1}\w+,\s[A-Z]{1}\w+)\s(?P<kids>\d+)\s(?P<transportation>[A-Z]{1}[a-z]+)\s(?P<pet>[a-z]+)\s(?P<place>[A-Z][a-z]+)'''
    search_regex = re.search(expression,textline)
    if option == 1:
        return search_regex.group(1)
    if option == 2:
        return search_regex.group(2)
    if option == 3:
        return search_regex.group(3)
    if option == 4:
        return search_regex.group(4)
    if option == 5:
        return search_regex.group(5)
    
    

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
        
    return [random.choice(list1),random.choice(list2),random.choice(list3),random.choice(list4),random.choice(list5)]


def main():
    regex = pass_regex()
    print(f'''Your partner is {regex[0]}\n
          and you will have {regex[1]} kids\n
          and you get around by {regex[2]}\n
          your pet is a {regex[3]}\n
          and you live in {regex[4]}''')
    salary = salaries()
       
def salaries():
    
    
    money_made = [["Doctor", 150000], ["Chef", 90000], ["Librarian", 30000], ["Swimmer", 60000],["Uber Driver",10000],["Salesperson",50000], ["Veterinarian", 120000],["Dropshipper",180000], ["Instagram Model", 7000],["UFC Fighter", 1000],["Dentist",190000], ["DMV Rapper", 500], ["Marvel Actor", 200000], ["Mickey Mouse Character", 250000], ["Lifeguard", 30000]]
    df= pd.DataFrame(money_made, columns= ['Job', 'Salary'])
    career = random.choice(money_made)
    job,salary = career[0],career[1]
    salary_filter= df['Salary'] >= salary
    df[salary_filter]
    print(df[salary_filter])
    print(f'You are a {job} and you make {salary} you make less then those above')
    return money_made

def createplot(job, desired_salary = 100000):
    jobs_list = []
    for list in money_made:
        jobs_list.append(list[0])
        return jobs_list
    salary_list = []
    for list in money_made:
        salary_list.append(list[1])
        return salary_list
    plt.plot(jobs_list, salary_list)


main()
 
