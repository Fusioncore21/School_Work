import Custom_Tools
import string
CHANGELOG = """
Morse Code Translation Program
[VERSION] 1.0
[LAST UPDATE] 12/11/2020
"""
# * Defining the morse code translator
MC_Translator = {
   ".-":"a",
   "-...":"b",
   "-.-.":"c",
   "-..":"d",
   ".":"e",
   "..-.":"f",
   "--.":"g",
   "....":"h",
   "..":"i",
   ".---":"j",
   "-.-":"k",
   ".-..":"l",
   "--":"m",
   "-.":"n",
   "---":"o",
   ".--.":"p",
   "--.-":"q",
   ".-.":"r",
   "...":"s",
   "-":"t",
   "..-":"u",
   "...-":"v",
   ".--":"w",
   "-..-":"x",
   "-.--":"y",
   "--..":"z",

   ".----":1,
   "..---":2,
   "...--":4,
   ".....":5,
   "-....":6,
   "--...":7,
   "---..":8,
   "----.":9,
   "-----":0
}

def UI():
    """Another awesome UI that is overcomplicated!"""
    def Morse_To_String():
        print("Enter morse code you'd like to translate. Please use the | key inbetween words. ")
        to_Parse = input("Enter morse code: ")
        to_Parse = to_Parse.lower() # Just to help check the string
        for letter in to_Parse:
            if letter in string.ascii_lowercase:
                print("[ERROR] Not valid morse code!\nRestarting...")
                UI()

        Translated_Morse = ""
        word2 = ""
        for word in to_Parse.split(sep="|"):
            for letter in word.split(sep=" "):
                for key in MC_Translator.keys():
                    if key == letter:
                        letter = letter.replace(key,MC_Translator[key])
                word2 += letter
            Translated_Morse+=(word2+" ")
            word2 = ""
        return Translated_Morse.title() # Makes it have a uppercase first letter

    def String_To_Morse(): # Now to go backwards. WEEEEEE
        print("Please enter the string which you'd like to translate. No symbols.")
        to_Parse = input("Enter string: ")
        to_Parse = to_Parse.lower()
        for letter in to_Parse:
            if letter in string.punctuation:
                print("[ERROR] No symbols please!")
                UI()
        Translated_String = ""
        for word in to_Parse.split(sep=" "):
            for item in MC_Translator.items():
                try:
                    if item[1] in word:
                        word = word.replace(item[1],item[0]+" ")
                except TypeError:
                    continue
                
            Translated_String+=(word+"|")

        return Translated_String


    Switch = {1:Morse_To_String,2:String_To_Morse}
    print(f"{CHANGELOG}\n1. Morse code to string\n2. String to morse code")
    print(Switch[Custom_Tools.Get_Int_Inputv2("Enter selection: ",2)]())

while __name__ == "__main__": # Only runs if started from this program
    UI()
