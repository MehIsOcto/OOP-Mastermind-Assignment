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

