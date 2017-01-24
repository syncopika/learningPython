import sys
import char_translator
import crypto

fileInput = sys.argv[1]

#set up jumbled string to map to
stringToMap = char_translator.random_permute_chars()

#make char_translator object
ct = char_translator.CharTranslator(stringToMap)

#pass that object to a crypto object
crypt = crypto.Coder(ct)

#encode file
outputName = fileInput + "-encoded"
crypt.encode_file(fileInput, outputName)

#then decode
newName = fileInput + "-new"
crypt.decode_file(outputName, newName)


