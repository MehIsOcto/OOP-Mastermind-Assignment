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

"""Class Initalisations"""
modeSelect = Game_Mode_Selector()
playSelect = PlayOrQuit()


"""Game Loop"""
Menu()
modeSelect.select()
print('Option =',modeSelect.get_select_value())

playSelect.playquit()
print('Option =',playSelect.get_play_value())

player1Select.player1()
player2Select.player2()
print('P1 =',player1Select.get_player1_value())
print('P2 =',player2Select.get_player2_value())

codeSelect.createcode()
print('Code =',codeSelect.get_code_list())