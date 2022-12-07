import re
import random
import sys
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser


class Storyline:
    def __init__(self,storyline):
        self.name, self.kids, self.car, self.pet, self.location = storyline[0], storyline[1], storyline[2], storyline[3], storyline[4]
         
    def __repr__(self):
        return 'Your partner is ' +self.name+' You will have ' +self.kids+ ' kid(s).' ' You will get around by '+ self.car+'. Your pet will be a '+ self.pet + ' and you will live in ' + self.location
    
        

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

def pass_regex(textfile):
    stored = open_file(textfile)
    list1 = []  #last name first name
    list2 = []  # # of kids 
    list3 = []  # Type of car
    list4 = []  # pet
    list5 = []  # location of life 
    for line in stored:
        list1.append(categories(line, 1))
        list2.append(categories(line, 2))
        list3.append(categories(line, 3))
        list4.append(categories(line, 4))
        list5.append(categories(line, 5))
        
    return [random.choice(list1),random.choice(list2),random.choice(list3),random.choice(list4),random.choice(list5)]

       
def salaries():
    
    
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    df= pd.DataFrame(money_made, columns= ['Job', 'Salary'])
    career = random.choice(money_made)
    job,salary = career[0],career[1]
    salary_filter= df['Salary'] >= salary
    df[salary_filter]
    #print(df[salary_filter])
    #print(f'You are a {job} and you make {salary} you make less then those above')
    return job

def createplot(job, desired_salary = 100000):
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    jobs_list = []
    salary_list = []
    for list in money_made:
        jobs_list.append(list[0])
        salary_list.append(list[1])
    ds = plt.plot(desired_salary)
    jobsal = plt.bar(jobs_list, salary_list, color = "maroon", width = .75)
    plt.show()


def main(textfile):
    regex = pass_regex(textfile)
     
    life = Storyline(regex)
    salary = salaries()
    print(repr(life))
    createplot(salary)


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="A list containing aspects of the person's life.")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

