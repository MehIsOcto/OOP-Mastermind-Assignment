import random


class Menu:
    print('')

    print('Welcome to Mastermind!')
    print('Developed by Ethan Weight')
    print('COMP 1046 Object-Oriented Programming')

    print('')



class Game_Mode_Selector:

    def __init__(self):
        self.mode = ""

    def select(self):
        print('Select which game you want to play:')
        print('     (A) Original Mastermind for 2 Players')
        print('     (B) Original Mastermind for 1 Player')
        print('     (C) Mastermind44 for 4 Players')
        print('*Enter A, B, or C to continue*')
        self.mode = input('')
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

    def get_select_value(self):
        return self.mode



class PlayOrQuit:
    def __init__(self):
        self.play = ""
    
    def playquit(self):
        print('')
        print('What would you like to do?')
        print('(p)lay the game')
        print('(q)uit')
        self.play = input('')

    def get_play_value(self):
        if self.play == 'q':
            return ('0')
        elif self.play == 'p':
            return ('1')



class PlayerNames:
    def __init__(self):
        self.p1 = ""
        self.p2 = ""

    def player1(self):
        print('Player 1: What is your name?')
        self.p1 = input ('')

        print('')

    def player2(self):
        print('Player 2: What is your name?')
        self.p2 = input ('')

        print('')

    def player2robot(self):
        self.p2 = 'Supermind'

    def get_player1_value(self):
        return self.p1
    
    def get_player2_value(self):
        return self.p2



class MastermindIntro(PlayerNames):
    def __init__(self):
        self.p1 = ""
        self.p2 = ""
    
    def intro(self, p1, p2):
        print('Welcome ' + p1 + ', you need to create a code that consists of four pegs. Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack. Specify the code by specifying four characters where each character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice. No character is shown on the screen so ' + p2 + ' cannot see it.')

    def duointro(self, p1, p2):
        print('Welcome ' + p1 + '. ' + p2 + ' has created a code consisting of four pegs. Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack.')
        
    
class CodeCreation:
    def __init__(self):
        self.code = ""

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



        
    
    def get_code_list(self):
        return self.code



class GuessCode(CodeCreation, PlayerNames):
    def __init__(self):
        self.guessed = ""
        self.code = ""
        self.p2 = ""

    def guessing(self, code, p2):

        convertcode = []
        convertcode[:0] = code

        print(convertcode)
        print('')

        print('Welcome ' + p2 +', you can now start to play by guessing the code.')
        print('Enter a guess by providing four characters and press Enter.')
        print('')

        self.guessed = 0
        tries = 0

        while self.guessed == 0:

            tries = tries + 1
            print('Attempt #' + str(tries))
            guess = input('')

            if guess == code:
                print('Congratulations! You broke the code in ' + str(tries) + ' attempt/s.')
                self.guessed = 1

            elif guess != code:
                convertcode = []
                c_index = 0
                g_list = []
                g_index = 0
                feedback = ""

                for entry in code:
                    convertcode += entry
                for entry in guess:
                    g_list += entry
                


                while g_index < 4:
                    if g_list[g_index] == convertcode[c_index] and g_index == c_index:
                        feedback += 'B '
                        g_list[g_index] = ''
                        g_index += 1
                        convertcode[c_index] = ''
                        c_index = 0
                    elif g_list[g_index] == convertcode[c_index] and g_index != c_index:
                        if g_list[g_index] == convertcode[g_index]:
                            feedback += 'B '
                            g_list[g_index] = ''
                            g_index += 1
                            convertcode[c_index] = ''
                            c_index = 0
                        elif g_list[c_index] != convertcode[c_index]:
                            feedback += 'W '
                            g_list[g_index] = ''
                            g_index += 1
                            convertcode[c_index] = '*'
                            c_index = 0
                    else:
                        c_index += 1
                    if c_index >= 4:
                        g_index += 1
                        c_index = 0
                        
            print('Feedback on Attempt #' + str(tries) + ': ' + feedback)
            print('')
                
            if tries > 9:
                print ('You ran out of tries!')
                self.guessed = 1


        




"""Class Initalisations"""
modeSelect = Game_Mode_Selector()
playSelect = PlayOrQuit()
player1Select = PlayerNames()
player2Select = PlayerNames()
codeSelect = CodeCreation()
guessedSelect = GuessCode()

"""Loop Inits"""
#play = '1'
#cont = ''

"""Game Loop"""
Menu()
modeSelect.select()
print('Option =',modeSelect.get_select_value())

playSelect.playquit()
print('Option =',playSelect.get_play_value())

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


print('Goodbye!')