import re
import random
import sys
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser

# Topics covered: Magic methods outside innnit, regex, with on files, sequence unpacking,
#filtering a data frame, optional parameters, pyplot, conditionals, lamba functions, parse_args


class Storyline: 
    """
    A class used to represent a story for person's fictional life
        
        Attributes:
        
        name (str) celeb from txt file 
        kids (int) number of kids that they will have with celeb
        car (str) transportation use
        pet (str) animal that the user will own
        location (str) location of where user will live
        
    """
    def __init__(self,storyline):
        """Sequence unpacks the random list of elements that makes up the users MASH game experience.
        Each attribute is then assigned part of the sequence unpack to be used in the repr method

        Args:
            storyline (list): List of random elements that was created in the pass_regex function
        """
        self.name, self.kids, self.car, self.pet, self.location = storyline[0], storyline[1], storyline[2], storyline[3], storyline[4]
         
    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_

        Member: Peter Mensah, magic methods not innit 
        """
        return 'Your partner is ' +self.name+' You will have ' +self.kids+ ' kid(s).' ' You will get around by '+ self.car+'. Your pet will be a '+ self.pet + ' and you will live in ' + self.location
    
        

def categories(textline, option):
    """This function recieves a textfile and matches the lines in the file to
    groups using a regular expression. It then returns that group depending on the
    option that is being called from the parameter and pass_regex function
    Args:
        textline (str): _A line from the textfile, supposed to be a first name last name
        # of kids, pet, and locaiton
        option (int): An optional int that represents the group number
        we want to call
    Returns:
        str: A string from the group that was called based on the option parameter

    Member: Aidan Shawyer, used regular expressions. 
    """
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
    """Open our textfile, stip it of special characters and then append it to a list.
    Return that list to be used throughout the rest of the program

    Args:
        textfile (str): Str name to a text file specified by user

    Returns:
        _type_: A list containing each line from textfile as an entire element

    Member: Aidan Shawyer, Open files
    """
    random_list = []  
    with open(textfile,"r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            random_list.append(line)
    return random_list

def pass_regex(textfile):
    """Iterates through a textfile and assigns each part of the line to a group. The groups
    are determined by a regex expression in another function. The function then returns one random
    element from each group in order to give the user a randomized version of MASH
    Args:
        textfile (str): A str to the textfile that we want to open

    Returns:
        list: A randomized list where each element is from one of the other five different groups
        that contains different categories.

    Side effects:
        Creates a list by using the open file and categories functions. 
    
    Member: Josiah Arnold

    """
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
    """Create our lists of lists that will be used to give our user their job and the assoicated
    salary with that job. The function creates a pandas data frame to show what professions
    make more each year then the one you were assigned. 

    Returns:
        list: The random job and salary assigned to the user
    
    Side effects:
        Job and salary which get returned will be used by other functions to compare other aspects
        of the users assigned salary to other profession's salaries.
    
    Member: Jeffrey Gomes, sequence unpacking and filtering a data frame
    """
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    df= pd.DataFrame(money_made, columns= ['Job', 'Salary'])
    career = random.choice(money_made)
    job,salary = career[0],career[1]
    print(f'Your profession is {job} and you make ${salary} annually\nYou can compare your salary to other professions in the graph.')
    print("Remaining users in the data frame earn a HIGHER salary than you:")
    salary_filter= df['Salary'] >= salary
    print(df[salary_filter])
    #print(f'You are a {job} and you make {salary} you make less then those above')
    return [job, salary]

def user_entry(textfile):
    """Allows the user to add entries to the text file, the entries must be in a specific format:
    Last name, First name Number of kids Type of transportation Pet Location

    Args:
        textfile (_str): A str to the path of the textfile which contains all the entries to 
        be used in a game of MASH
    
    Side effects: 
        Appends new data entries to the existing text files
    
    Member: Hannah Johnston (With open again, but not to be used as our main function to cover the topic)
    """
    print("Would you like to add a new entry? Enter 'Y' or 'N'")
    yes_or_no = input()
    print(yes_or_no)
    if yes_or_no == "Y":
        with open(textfile, "a") as f:
            print("Input your desired entry following the format exactly: ")
            print("Lastname, Firstname Kids(numerical) Car Pet Location")
            added_entry= input()
            f.write("\n" + added_entry)
            f.close()
    elif yes_or_no == "N":
        pass
    
    

def createplot(test, desired_salary = 100000):
    """Plots all the different potential salaries to their respective professions. Displays a bar
    graph. 

    Args:
        desired_salary (int, optional): The desired salary by the user
        if they are not happy with the current salary they're receiving. Defaults to 100000.

    Returns:
       list: Lists of lists, containing the profession and their salary per each list
    
    Member: Hannah Johnston, optional parameters and pyplot
    """
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    jobs_list = []
    salary_list = []
    for list in money_made:
        jobs_list.append(list[0])
        salary_list.append(list[1])
    plt.plot(desired_salary)
    plt.bar(jobs_list, salary_list, color = "maroon", width = .75)
    plt.show()
    return money_made

    
def main(textfile):
    """Main driver of our MASH script. Runs a user display option for users to pick if the want to 
    add to the existing textfile or if they want to play a game of MASH

    Args:
        textfile (str): String containing the path to the textfile, entered in command line terminal

    Member: Peter Mensah, Condintionals 
    """
    print(f"Enter the corresponding digit to navigate: \n1 - Play MASH\n2 - Add entry to MASH game")
    user_options = input()
    if user_options == str(1):
        regex = pass_regex(textfile)
        life = Storyline(regex)
        print(repr(life))
        salary = salaries()
        compare_jobs(salary[0])
        createplot(salary)
    else:
        user_entry(textfile)
        
def compare_jobs(user_job):
    """Iterates between all jobs alongside the salaries in the dataframe.
     This function then creates a list comparing all salaires of the different jobs to each other.
    

    Args:
        user_job (str): A string that names the profession the user has been assigned.
    
    Members: Jeffrey Gomes, lambda expressions
    """
    money_made = [["Doctor", 150_000], ["Chef", 90_000], ["Librarian", 30_000], ["Swimmer", 60_000],["Nurse",10_000],["cop",50_000], ["Vet", 120_000],["Dropshipper",180_000], ["Model", 7_000],["counselor", 1_000],["Dentist",190_000], ["Rapper", 50_000], ["Actor", 200_000], ["Lawyer", 250_000], ["Lifeguard", 30_000]]
    jobs_ordered = []
    for job, salary in sorted(money_made, key = lambda g:g[1]):
        if user_job == job:
            job = job.upper()
            jobs_ordered.append(job)
        else:
            jobs_ordered.append(job)
    print("You're job is in all caps. These are the jobs in order from most made, to least made:")
    print(' '.join(jobs_ordered))
    
    

def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    
    Member: Josiah Arnold, parse args
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="A list containing aspects of the person's life.")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
