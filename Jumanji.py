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


class GameSetUp:
    """Create names and attributes for the 4 players in our Jumanji game
    Attributes:
        name (str): The name of one of the four players to play
        character (str): the game piece the user wants to play as
    
    """ 
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.game_board = ['S','-','-','-','-','-','>',    #14 014
                            'O','O','O','O','O','O','>',  
                            '+','-','-','-','-','-','>',    
                            '+','O','O','O','O','O','O',   
                            '+','-','-','-','-','-','>',    
                            'O','O','O','O','O','O','>',  
                            '+','-','-','-','-','-','>', 
                            '+','-','-','-','-','-','J']  

class GameRules:
    """Define the game rules for each type of game board tile
    Each method will need to use the GameMovement Class, may switch around to have
    GameRules inherent from GaveMovement Class
    """
    def __init__(self) -> None:
        pass
    def blank_space(self):
        """Jungle Danger threaten you. To be saved, players must roll the hourglass
        or symbol you drew on your card
        """
        pass
    def wait_for_space(self):
        """Players must roll a 5 or 8 to save you. Each unsuccesful roll of a 
        5 or 8 requires the player who drew the card to move back a space
        """
        pass
    def jungle_space(self):
        """All players are trapped in the jungle, everyone must roll to save
        eachother
        """
        pass
    def rhino_space(self):
        """If player lands on a rhino space, player may block any other player
        with the Rhino piece, that player can not move until someone moves the
        rhino, or the roll an even number
        """
        pass

class GameMovement:
    def __init__(self) -> None:
        """Initialize our gameboard that will be played on 
        """
        pass
    def roll_dye(self):
        """Ability to roll different types of dye, numeric or character based
        """
        pass
    def move_player(self):
        """Move player across game board 
        """
        pass
    
class GameStats:
    def number_of():
        """Summarize the number of rolls
        """
        pass
    def check_winner():
        pass
    
    
def doomsday_grid():
    """Keep track of doomsday grid count, if reaches 8/8 cards, game ends and all
    players lose
    """
    return

    return


def main():
    """Run the main code of the game, open and read doc with the game cards
    Each card will be different
    """
    return








#print(f"{' '.join(quad_one[0:7])}"
      #f"\n{' '.join(quad_one[7:14])}"
      #f"\n{' '.join(quad_one[14:21])}"
      #f"\n{' '.join(quad_one[21:28])}"
      #f"\n{' '.join(quad_one[28:35])}"
      #f"\n{' '.join(quad_one[35:42])}"
      #f"\n{' '.join(quad_one[42:49])}"
      #f"\n{' '.join(quad_one[49:56])}"
 #     )