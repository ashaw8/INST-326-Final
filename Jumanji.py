import sys
import argparse
import random

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
        
    def roll_dice(self,required_dice):
        """Ability to roll different types of dye, numeric or character based

            Returns (int): The number from a dye 1-8 and a character from a second dye
        """
        
        character_dice = ['axe', 'die', 'opendoor', 'racquet', 'raft','rope', 'score', 'hourglass']
        if required_dice == "number":
            return random.randint(1,8)
        else:
            return random.choice(character_dice)
        
        
        
        
        
        pass

class GameRules(GameSetUp):
    """Define the game rules for each type of game board tile
    """
    def blank_space(self):
        """Jungle Danger threaten you, which basically means the character whose roll it is
        is in trouble. To be saved, other players get a turn and must roll the hourglass
        or symbol you drew on your card
        
        Side Effects: roll dice method, interacts with doomsday grid method
        
        Returns(str): String indicating whos turn is next or add's a card to the doomsday grid
        """
        pass
    def wait_for_space(self):
        """Players must roll a 5 or 8 to save you. Each unsuccesful roll of a 
        5 or 8 requires the player who drew the card to move back a space
        
        Side Effects: Players will move back if Players were unsuccesful to free them if 5 or 8 was not rolled. 
        Interacts with players turn method/class for each trial to free character
        
        Players can keep moving back if they are unsuccesful
        
        Returns(str): Updated player position and stats respective to the players
        
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
        rhino, or they roll an even number
        
        Side effects: Player with Rhino in front of them has limited movement
        
        Returns(str): New player position with Rhino infront of them
        
        
        """
        pass
        
    def doomsday_grid(self):
        """Keep track of doomsday grid count, if reaches 8/8 cards, game ends and all
        players end up losing the game
        
        Side Effects: If reaches 8/8 game indicates that player lost and interacts with game stats class
        
        Returns(Boolean): Game is over if True if False game continues
        """
        pass


class GameMovement(GameSetUp):
    """This class will determine how a player will move and will track which
    players turn it is, through inheriting the GameSetUp class
    
        
        """
    def __init__(self) -> None:
        """Initialize our gameboard to be played and moved on.
        """
        pass

    def move_player(self):
        """Move player across game board.
            
            Returns(str): The board game position the player has moved to on the game boards
            
            Side effect: Interacts with the roll_dye method to be able to 
                determine how many spaces the player will move.
        """
        pass
    def players_turn(self):
        """Keeps track of whos turn it is
        
            Side effects: Indicates whos turn it is to the other methods so that the 
            other methods can adopt and become active for the current player.
        """
        pass
    
class GameStats:
    """Here it will count the overall statistics of the game played for each of
    players in the game. It will deliver the total number of rolls, cards, and
    turns that each of the players had taken.
    
        Attributes:
            """
    def number_of():
        """Counts the number of rolls for each player, the cards that each of 
        them used, and the number of turns taken for each of the players.
        
        Returns(ints and str): Stats on spaces moved, number of rolls, cards used, turns taken
        """
        pass
    def check_winner():
        """Check if a player has reached Jumanji tile by rolling the exact number needed on the dice
        
            Side effects: Ends game and indicates winner
            
            Returns(str): String indicating the winner of the game or it will 
            have to return the fact that no one won
        """
        pass


def main(filepath):
    """Run the main code of the game, open and read doc with the game cards
    Each card will be different
    
    Attribute:
        filepath(str): string to a file path of Jumanji game cards
    """
    return






if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

#print(f"{' '.join(quad_one[0:7])}"
      #f"\n{' '.join(quad_one[7:14])}"
      #f"\n{' '.join(quad_one[14:21])}"
      #f"\n{' '.join(quad_one[21:28])}"
      #f"\n{' '.join(quad_one[28:35])}"
      #f"\n{' '.join(quad_one[35:42])}"
      #f"\n{' '.join(quad_one[42:49])}"
      #f"\n{' '.join(quad_one[49:56])}"
 #     )