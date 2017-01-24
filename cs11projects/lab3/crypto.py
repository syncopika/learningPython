#crypto.py
#this file does the translating/untranslating

class Coder:

    #init - takes a CharTranslator object
    def __init__(self, ct):
        self.charTrans = ct

    #encode the file
    def encode_file(self, inputName, outputName):
        file = open(inputName, 'r')
        writeFile = open(outputName, 'w')
        for line in file:
            for c in line:
                writeFile.write(self.charTrans.translate_char(c))
        file.close()
        writeFile.close()
        return

    #decode the file
    def decode_file(self, inputName, outputName):
        file = open(inputName, 'r')
        writeFile = open(outputName, 'w')
        for line in file:
            for c in line:
                writeFile.write(self.charTrans.untranslate_char(c))
        file.close()
        writeFile.close()
        return
    
        
