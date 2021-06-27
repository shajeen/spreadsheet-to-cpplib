from pyfiglet import Figlet

def printText(text):
    textFont = Figlet(font='digital')
    print(textFont.renderText(text))