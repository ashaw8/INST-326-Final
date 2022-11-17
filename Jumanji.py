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
        game_board (list): list of characters to be played as our game board
        cards (list): List of game cards
    """ 
    def __init__(self, name, character, listofcards, turnnumber,type ):
        self.cards = listofcards
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
        
    def roll_dye(self):
        """Ability to roll different types of dye, numeric or character based

            Returns: The number from a dye 1-8 and a character from a second dye
        """
        pass

class GameRules(GameSetUp):
    """Define the game rules for each type of game board tile
    """
    def blank_space(self):
        """Jungle Danger threaten you. To be saved, players must roll the hourglass
        or symbol you drew on your card
        
        Side Effects: roll dice method, interacts with doomsday grid method
        
        Returns: String indicating whos turn is next or add's a card to the doomsday grid
        """
        pass
    def wait_for_space(self):
        """Players must roll a 5 or 8 to save you. Each unsuccesful roll of a 
        5 or 8 requires the player who drew the card to move back a space
        
        Side Effects: Players will move back if Players were unsuccesful to free them if 5 or 8 was not rolled. 
        Interacts with players turn method/class for each trial to free character
        
        Players can keep moving back if they are unsuccesful
        
        Returns: New player position and stats
        
        """
        pass
    def jungle_space(self):
        """All players are trapped in the jungle, everyone must roll to save
        eachother
        
        Side Effects: No one can move until all players have rolled
        
        Returns: None
        """
        pass
    def rhino_space(self):
        """If player lands on a rhino space, player may block any other player
        with the Rhino piece, that player can not move until someone moves the
        rhino, or the roll an even number
        
        Side effects: Player with Rhino in front of them has limited movement
        
        Returns: New player position with Rhino infront of them
        
        
        """
        pass
        
    def doomsday_grid(self):
        """Keep track of doomsday grid count, if reaches 8/8 cards, game ends and all
        players lose
        
        Side Effects: If reaches 8/8 game indicates that player lost and interacts with game stats class
        
        Returns: Game is over if True if False game continues
        """
        pass


class GameMovement(GameSetUp):
    def __init__(self) -> None:
        """Initialize our gameboard that will be played on 
        """
        pass

    def move_player(self):
        """Move player across game board 
            
            Returns: The position the player has moved to on the game board
        """
        pass
    def players_turn(self):
        """Keeps track of whos turn it is
        
            Side effects: Indicates whos turn it is to other methods
        """
        pass
    
class GameStats:
    def number_of():
        """Reutrn the number of rolls for each player
        
        Returns: Stats on spaces moved, number of rolls, cards used, turns taken
        """
        pass
    def check_winner():
        """Check if a player has reached Jumanji tile
        
            Side effects: Ends game and indicates winner
            
            Returns: String indicating the winner of the game, if any
        """
        pass


def main(filepath):
    """Run the main code of the game, open and read doc with the game cards
    Each card will be different
    
    Attribute:
        filepath(str): string to a file path of Jumanji game cards
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