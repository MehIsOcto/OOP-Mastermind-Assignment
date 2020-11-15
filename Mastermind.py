""" Imports random, to be used in generating the code for saingle player mastermind """
import random

""" Menu prints off the menu, has no inputs, hence no init"""
class Menu:
    print('')

    print('Welcome to Mastermind!')
    print('Developed by Ethan Weight')
    print('COMP 1046 Object-Oriented Programming')

    print('')


""" Game mode selector allows to player to choose between single player mastermind, duo player mastermind and mastermind 44 """
class Game_Mode_Selector:

    """ Inits 'mode', the variable for game mode """
    def __init__(self):
        self.mode = ""

    """ Prints the options for the game modes """
    def select(self):

        
        print('Select which game you want to play:')
        print('     (A) Original Mastermind for 2 Players')
        print('     (B) Original Mastermind for 1 Player')
        print('     (C) Mastermind44 for 4 Players')
        print('*Enter A, B, or C to continue*')

        """ Assigns the game mode to local variable mode """
        self.mode = input('')

        """ Mode is then checked to see if it matches the options via if statement. If not, then repeats this function of the class """
        if self.mode == 'A':
            pass
        elif self.mode == 'B':
            pass
        elif self.mode == 'B':
            pass
        elif self.mode == 'C':
            pass
        elif self.mode == 'a':
            pass
        elif self.mode == 'b':
            pass
        elif self.mode == 'c':
            pass
        else:
            print('Invalid Entry')
            print('')
            modeSelect.select()

    """ Function to call the inputted game mode """
    def get_select_value(self):
        return self.mode


""" PlayOrQuit is similar to game mode selector, however instead determines if the player wishes to leave the game. """
class PlayOrQuit:

    """ Initialises the local play variable """
    def __init__(self):
        self.play = ""

    """ Acts as the menu, allowing user to press p for play or q for quit """
    def playquit(self):
        print('')
        print('What would you like to do?')
        print('(p)lay the game')
        print('(q)uit')
        self.play = input('')

        """ Makes user enter either p or q via if statement """
        if self.play == 'p':
            pass
        elif self.play == 'q':
            pass
        else:
            print('Invalid Entry')
            print('')
            playSelect.playquit()

    """ Returns boolean depending if user selects 1 for play or 0 for quit """
    def get_play_value(self):
        if self.play == 'q':
            return ('0')
        elif self.play == 'p':
            return ('1')


""" PlayerNames allows user to input either both player names for single player, or two player names for duo player games """
class PlayerNames:

    """ Init player1 and player2 variables """
    def __init__(self):
        self.p1 = ""
        self.p2 = ""

    """ Input player 1 name """
    def player1(self):
        print('Player 1: What is your name?')
        self.p1 = input ('')

        print('')

    """ Input player 2 name """
    def player2(self):
        print('Player 2: What is your name?')
        self.p2 = input ('')

        print('')

    """ Makes player 2 name 'Supermind' (Called in single player) """
    def player2robot(self):
        self.p2 = 'Supermind'

    """ Allows p1 name to be called """
    def get_player1_value(self):
        return self.p1

    """ Allows p2 name to be called """
    def get_player2_value(self):
        return self.p2


""" Inherits from playernames to print the introduction, depending on which game type """
class MastermindIntro(PlayerNames):
    def __init__(self):
        self.p1 = ""
        self.p2 = ""

    """ Intro for single player mastermind """
    def intro(self, p1, p2):
        print('Welcome ' + p1 + ', you need to create a code that consists of four pegs. Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack. Specify the code by specifying four characters where each character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice. No character is shown on the screen so ' + p2 + ' cannot see it.')

    """ Intro for duo player mastermind """
    def duointro(self, p1, p2):
        print('Welcome ' + p1 + '. ' + p2 + ' has created a code consisting of four pegs. Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack.')
        
""" Generates code for mastermind """
class CodeCreation:
    def __init__(self):
        self.code = ""

    """ Allows user to create code, when called in single player loop """
    def createcode(self):
        print('Enter the code now:')
        code1 = input('')

        print('Enter the same code again:')
        code2 = input('')

        if code1 == code2:
            self.code = code1
        else:
            print('')
            print('Entries do not match!')
            print('')
            codeSelect.createcode()
    
    """ Auto-generates a four letter code, utilizing the previously imported random...Utilzied in the single player mastermind """
    def createcoderobot(self):
        for i in range(4):
            new_num = random.randint(0,5)
            if new_num == 0:
                self.code = self.code + 'R'
            elif new_num == 1:
                self.code = self.code + 'L'
            elif new_num == 2:
                self.code = self.code + 'G'
            elif new_num == 3:
                self.code = self.code + 'Y'
            elif new_num == 4:
                self.code = self.code + 'W'
            elif new_num == 5:
                self.code = self.code + 'B'
        print (self.code)

    """ Returns the code, regardless if player or computer generatored """    
    def get_code_list(self):
        return self.code


""" Allows the user to guess the code, utilized in both single and duo player mastermind...Inherits from both playerNames and CodeCreation, needing p2 name and code to crack """
class GuessCode(CodeCreation, PlayerNames):
    def __init__(self):
        self.guessed = ""
        self.code = ""
        self.p2 = ""

    """ Called to allow user to guess code """
    def guessing(self, code, p2):

        """ converts string code into list """
        convertcode = []
        convertcode[:0] = code

        print(convertcode)
        print('')

        """ Introduces how to guess code """
        print('Welcome ' + p2 +', you can now start to play by guessing the code.')
        print('Enter a guess by providing four characters and press Enter.')
        print('')

        """ Sets variables...guessed counts if the code is cracked, and tries counts the ammount of attempts """
        self.guessed = 0
        tries = 0

        """ Eg. While code hasn't been guessed... """
        while self.guessed == 0:

            """ Add one counter to tries, show attempt no and allow guess input attempt """
            tries = tries + 1
            print('Attempt #' + str(tries))
            guess = input('')

            """ If the guess matches the code they won the game, and loop is ended via updating guessed """
            if guess == code:
                print('Congratulations! You broke the code in ' + str(tries) + ' attempt/s.')
                self.guessed = 1
            elif guess != code:

            
                """ Create several variables - two empty lists for the code and guess - a guess and code index to maintain which letters have been cross checked """
                """ - And lastly an empty string to add either B or W for the feedback """
                convertcode = []
                c_index = 0
                convertedguess = []
                g_index = 0
                feedback = ""

                """ creates the lists for code and guess """
                for entry in code:
                    convertcode += entry
                for entry in guess:
                    convertedguess += entry
                
                """ While the guess index is below 4..."""
                while g_index < 4:
                    """ Cross check the guess list position of guess index with the converted codes. This is done using the indexies, and runs several times changing """
                    """ indexies each time. as the colour matches the same position, B is added to feedback. A a matching colour occurs in different spots, W is appended"""

                    if convertedguess[g_index] == convertcode[c_index] and g_index == c_index:
                        convertedguess[g_index] = ''
                        g_index += 1
                        feedback += 'B '
                        convertcode[c_index] = ''
                        c_index = 0

                    elif convertedguess[g_index] == convertcode[c_index] and g_index != c_index:
                        if convertedguess[g_index] == convertcode[g_index]:
                            convertedguess[g_index] = ''
                            g_index += 1
                            feedback += 'B '
                            convertcode[c_index] = ''
                            c_index = 0

                        elif convertedguess[c_index] != convertcode[c_index]:
                            convertedguess[g_index] = ''
                            g_index += 1
                            feedback += 'W '
                            convertcode[c_index] = '*'
                            c_index = 0

                    else:
                        c_index += 1

                    if c_index >= 4:
                        g_index += 1
                        c_index = 0

            """ Prints the feedback on each attempt """  
            print('Feedback on Attempt #' + str(tries) + ': ' + feedback)
            print('')
            
            """ If tries max-es out, game ends """
            if tries > 9:
                print ('You ran out of tries!')
                self.guessed = 1


        




"""Class Initalisations, initalising the '__init__' statement in each of the classes"""
modeSelect = Game_Mode_Selector()
playSelect = PlayOrQuit()
player1Select = PlayerNames()
player2Select = PlayerNames()
codeSelect = CodeCreation()
guessedSelect = GuessCode()

"""Loop Inits"""
#play = '1'
#cont = ''

"""Acts as the Game Loop, calling each class using the already existing objects used while initialising the classes previously. """
Menu()
modeSelect.select()

""" These print 'Option =' lines are not a part of the game, but rather exist as a way of helping me debug the game and follow classes...They will be removed before submittion"""
print('Option =',modeSelect.get_select_value())

playSelect.playquit()
print('Option =',playSelect.get_play_value())


""" This large loop allows for me to direct the player to the loop corresponding to the slected game mode in Game_Mode_Selector...This calls the get_select_value, which only returns the relevant variable. """
""" This utilisation of calling functions allowed me to not use globals, which would create issues later in development """

if modeSelect.get_select_value() == 'A' or modeSelect.get_select_value() == 'a':
    player1Select.player1()
    player2Select.player2()
    print('P1 =',player1Select.get_player1_value())
    print('P2 =',player2Select.get_player2_value())

    MastermindIntro.intro(PlayerNames, player1Select.get_player1_value(),player2Select.get_player2_value())

    codeSelect.createcode()
    print('Code =',codeSelect.get_code_list())

    guessedSelect = GuessCode.guessing(CodeCreation, codeSelect.get_code_list(), player2Select.get_player2_value())

elif modeSelect.get_select_value() == 'B' or modeSelect.get_select_value() == 'b':
    player1Select.player1()
    player2Select.player2robot()
    print('P1 =',player1Select.get_player1_value())
    print('P2 =',player2Select.get_player2_value())

    MastermindIntro.duointro(PlayerNames, player1Select.get_player1_value(),player2Select.get_player2_value())

    codeSelect.createcoderobot()
    print('Code =',codeSelect.get_code_list())

    guessedSelect = GuessCode.guessing(CodeCreation, codeSelect.get_code_list(), player2Select.get_player2_value())
else:
    print('Not A or B')

""" When game ends, prints goodbye, signifying end, also acting as a tool to help design game loop """
print('Goodbye!')