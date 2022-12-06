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
    
    
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    df= pd.DataFrame(money_made, columns= ['Job', 'Salary'])
    career = random.choice(money_made)
    job,salary = career[0],career[1]
    salary_filter= df['Salary'] >= salary
    df[salary_filter]
    print(df[salary_filter])
    print(f'You are a {job} and you make {salary} you make less then those above')
    return money_made

def createplot(job, desired_salary = 100000):
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    jobs_list = []
    salary_list = []
    for list in money_made:
        jobs_list.append(list[0])
        salary_list.append(list[1])
    plt.plot(job, desired_salary)
    plt.bar(jobs_list, salary_list, color = "maroon", width = 1)
    plt.show()
createplot("Doctor")


main()
 
