#
#   AP1
#   authors: Jacob Sheets and Jake Allinson
#   version: 1.2
#

import sys
import string
from collections import defaultdict
from collections import deque
import monoalfa_decryptgui
from PyQt5 import QtGui, QtCore, QtWidgets

#############################################################################################
# brownFoxWindow #
# Class of gui events & decrpyt functions #
#############################################################################################

class brownFoxWindow(QtWidgets.QMainWindow, monoalfa_decryptgui.Ui_BrownFox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Buttons
        self.Clear_Button.clicked.connect(self.clearClick)
        self.Restart_Button.clicked.connect(self.restartClick)
        self.Decrypt_Button.clicked.connect(self.decryptClick)

        #Menu Buttons
        self.actionQuit.triggered.connect(self.close)

    def clearClick(self):
        #clears input 
        self.statusbar.showMessage('Clear...')
        self.Input_Text_Box.clear()

    def restartClick(self):
        #clears every input and output box
        self.statusbar.showMessage('Reset...')
        self.Input_Text_Box.clear()
        self.Output_Text_Box.clear()
        self.freq_Text_Box.setPlainText('etaoinsrhdlucmfywgpbvkxqjz')

    def decryptClick(self):
        #runs decrypt and prints to output screen
        inputMessage = self.Input_Text_Box.toPlainText()
        Word_Freq = self.freq_Text_Box.toPlainText()

        outputMessage = self.decrypt(inputMessage, Word_Freq)

        self.Output_Text_Box.setPlainText(outputMessage)
        self.statusbar.showMessage('Decrypt...')

    #Decrypts Message
    def decrypt(self, inputMessage, Word_Freq): 
        #find freq of input Message
        inputFreq = self.freqparse(inputMessage) 
        #Makes string lowercase
        inputMessage = inputMessage.lower()      
        outputString = ""
        for char in inputMessage:
            if char == ' ':
                outputString = outputString + ' '
            for char2 in inputFreq:
                #try:
                    if char == char2:
                        outputString = outputString + str(Word_Freq[inputFreq.index(char2)])
                #except:

        return outputString


#############################################################################################
# parse function #
# returns freq string #
#############################################################################################

    def freqparse(self, stringx):
        
        #declare list of lowercase letters
        letterStats = dict.fromkeys(string.ascii_lowercase, 0)
        inputString = stringx.lower()

        #walks through input and adds a score to each letter.
        for char in inputString:
            if char in letterStats.keys():
                letterStats[char] += 1
        
        # Check letterStats
        if len(letterStats) != 26:
            raise ValueError('Incorrect number of letters in c_letterStats')

        return self.clean_string(letterStats)

#############################################################################################
# string maker and cleaner function #
# returns cleaned string #
#############################################################################################

    def clean_string(self, listx):
        # sort letterStats

        #Turns list to a string.
        inverse = defaultdict(list)
        for k, v in listx.items():
            inverse[v].append(k)
        listx = list()
        for k in sorted(inverse):
            listx.insert(k, inverse[k])

        #reverses list to be highest to lowest freq.
        listx.reverse()

        #cleans out all list elements from the converted string.
        cleanString = ''.join([str(elem) for elem in listx])
        cleanString = cleanString.replace('/', '')
        cleanString = cleanString.replace('[', '')
        cleanString = cleanString.replace(']', '')
        cleanString = cleanString.replace(',', '')
        cleanString = cleanString.replace(' ', '')
        cleanString = cleanString.replace("'", '')

        return cleanString


#############################################################################################
# main #
#############################################################################################

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = brownFoxWindow()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()















