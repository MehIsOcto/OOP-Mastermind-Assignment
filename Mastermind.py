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


"""Class Initalisations"""
modeSelect = Game_Mode_Selector()
playSelect = PlayOrQuit()


"""Game Loop"""
Menu()
modeSelect.select()
print('Option =',modeSelect.get_select_value())

playSelect.playquit()
print('Option =',playSelect.get_play_value())

