#--------------------------------------------------------------------------------------------------
# Purpose            : Code to handle morse code translations
# Date Created       : 06Apr2023
# Author             : A.S.Harrison
# Amendment History  : Date         Author          Description
#                      06Apr2023    A.S.Harrison    Created
#--------------------------------------------------------------------------------------------------

#NOTE: Tested against https://www.morsetranslator.com/

# Declare a dictionary containing all the English letters and their Morse equivalent (should add punctuation to this)
MorseDict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "   "
}


strTest = "The quick brown fox jumps over the lazy dog".lower()         #This is the message to convert to Morse code

lstWork = list(strTest)                                                 #Make a LIST copy of the test string (so we can easily iterate through the letters)

strResult = ""                                                          #Initialise the results string
                                                                        #Loop through each character and generate the equivalen Morse code 
for i in range(0, len(lstWork)):                                        #For each character in the message
    strResult += MorseDict[lstWork[i]]                                  #Append the appropriate Morse code to the end of the result
    if lstWork[i] != " ":                                               #If we are NOT on a space character
        if i < len(lstWork)-1: strResult += "  "                        #And we HAVEN'T reached the end of the message - add 2 spaces (to represent the timing between letters)

print(strResult)                                                        #Display the result


#Now do the reverse - convert it back into English
#    Create a list of words by splitting at 5 spaces
#    Create a list of letters by splitting each word at 2 spaces
#    Convert the morse letter back to english letter
#    Add a space at the end of each word

strEnglish = ""                                                         #Initialise the English string

lstWords = strResult.split("     ")                                     #Get all the individual Morse words into a list (by splitting where there are 5 spaces)

for i in range(0, len(lstWords)):                                       #For each Morse word
    lstLetters = lstWords[i].split("  ")                                #Get a list of Morse letters (by splitting where there are 2 spaces)
    for j in range(0, len(lstLetters)):                                 #For each Morse letter
        strEnglish += list(MorseDict.keys())[list(MorseDict.values()).index(lstLetters[j])] #Find the English letter
    if i < len(lstWords)-1: strEnglish += " "                           #As long as we aren't on the last word - add a space

print(strEnglish)                                                       #Output the English text
