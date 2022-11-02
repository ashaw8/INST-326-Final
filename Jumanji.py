"""Jumanji Game Board
11/1/2022
Authors: Aidan Shawyer, Jeffrey Gomes, Josiah Arnold, Hannah Johnston, Peter Mensah

This is a starter doctsring saying who is exactly in our
group for this final project. In which we will be making
our own version of the Jumanji board game. It will consist
of different players and different types of actions which 
the board will play on the user or the player themselves
will play. But this is an example intro docstring.
"""
example_list= ()
#How do you make an octopus laugh...... give them ten-tickles
class Character: 
        def __init__(self, name, color):
            self.name = "david"


second_gb = ['-','-','-','-','+','O','O',    #14 0-14
             'O','O','O','O','|','O','O',  
             '+','-','+','O','|','O','O',   
             '|','O','+','-','+','O','O',   
             '|','O','O','O','O','O','O',   
             '+','-','-','-','-','-','+',  
             'O','O','O','O','O','O','O']  

print(f"{' '.join(second_gb[0:7])}\n{' '.join(second_gb[7:14])}"
      f"\n{' '.join(second_gb[14:21])}\n{' '.join(second_gb[21:28])}"
      f"\n{' '.join(second_gb[28:35])}\n{' '.join(second_gb[35:42])}"
      f"\n{' '.join(second_gb[42:49])}"
      )