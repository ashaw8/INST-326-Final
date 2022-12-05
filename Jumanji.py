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
    def __init__(self):
        self.cards = "listofcards"
        #Index for each players total sequence of movements
        self.player_spaces = {"Player1":[1,16, 31, 46, 61, 76, 91, 106, 121, 136
        ,151, 166, 181, 196, 211, 226, 241, 256, 271, 286, 301, 316, 331, 346,
        361, 376, 391, 406, 421, 436, 451, 466, 481, 496, 511, 526],
                              "Player2":[5,20, 35, 50, 65, 80, 95, 110, 125, 140
        ,155, 170, 185, 200, 215, 230, 245, 260, 275, 290, 305, 320, 335, 350, 
        365, 380, 395, 410, 425, 440, 455, 470, 485, 500, 515, 530],
                              "Player3":[9,24, 39, 54, 69, 84, 99, 114, 129, 144
        ,159, 174, 189, 204, 219, 234, 249, 264, 279, 294, 309, 324, 339, 354,
        369, 384, 399, 414, 429, 444, 459, 474, 489, 504, 519, 534], 
                              "Player4":[13, 28, 43, 58, 73, 88, 103, 118, 133, 
        148, 163, 178, 193, 208, 223, 238, 253, 268, 283, 298, 313, 328, 343, 
        358, 373,388, 403, 418, 433, 448, 463, 478, 493, 508, 523, 538]}
        
        self.playertotal1 = 0
        self.playertotal2 = 0
        self.playertotal3 = 0
        self.playertotal4 = 0
        
        self.game_board = ["|","S","|"," ","|","S","|"," ","|","S","|"," ","|","S","|", #0-15
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|","W","|"," ","|","R","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|","R","|"," ","|"," ","|"," ","|","U","|"," ","|"," ","|",
             "|"," ","|"," ","|","R","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","U","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|","W","|"," ","|","W","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","W","|",
             "|","W","|"," ","|"," ","|"," ","|","R","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","R","|"," ","|","R","|"," ","|","U","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|","W","|"," ","|","W","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","R","|"," ","|"," ","|"," ","|","R","|"," ","|","U","|",
             "|"," ","|"," ","|","W","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","U","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|","U","|"," ","|"," ","|",
             "|","W","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","R","|",
             "|"," ","|"," ","|","U","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","U","|",
             "|","W","|"," ","|"," ","|"," ","|","W","|"," ","|"," ","|",
             "|"," ","|"," ","|","R","|"," ","|"," ","|"," ","|","W","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|","J","|"," ","|","J","|"," ","|","J","|"," ","|","J","|",
             ]  
        print(self.cards)
        
    def move_player(self, playerturn, number):
        """Move player across game board.
            
            Returns(str): The board game position the player has moved to on the game boards
            
            Side effect: Interacts with the roll_dye method to be able to 
                determine how many spaces the player will move.
        """
        if playerturn == 1:
            self.playertotal1 += number
            player1 = self.player_spaces["Player1"]
            player1move = player1[self.playertotal1]
            self.game_board[player1move] = "1"
        if playerturn == 2:
            self.playertotal2 += number
            player2 = self.player_spaces["Player2"]
            player2move = player2[self.playertotal2]
            self.game_board[player2move] = "2"
        if playerturn == 3:
            self.playertotal3 += number
            player3 = self.player_spaces["Player3"]
            player3move = player3[self.playertotal3]
            self.game_board[player3move] = "3"
        if playerturn == 4:
            self.playertotal4 += number
            player4 = self.player_spaces["Player4"]
            player4move = player4[self.playertotal4]
            self.game_board[player4move] = "4"
        

    def players_turn(self):
        """Keeps track of whos turn it is
        
            Side effects: Indicates whos turn it is to the other methods so that the 
            other methods can adopt and become active for the current player.
        """
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

    
class GameStats(GameSetUp):
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

def roll_dice(required_dice):
        """Ability to roll different types of dye, numeric or character based

            Returns (int): The number from a dye 1-8 and a character from a second dye
        """
        
        character_dice = ['axe', 'die', 'opendoor', 'racquet', 'raft','rope', 'score', 'hourglass']
        if required_dice == "number":
            return random.randint(1,8)
        else:
            return random.choice(character_dice)

def main():
    """Run the main code of the game, open and read doc with the game cards
    Each card will be different
    
    Attribute:
        filepath(str): string to a file path of Jumanji game cards
    """
    
    #main game method, will be a while loop to run game 
    game = GameSetUp()
    game.move_player(1,3)
    #Temp flag until check_winner method is set-up



main()


#if __name__ == "__main__":
    #args = parse_args(sys.argv[1:])
    #main(args.file)
