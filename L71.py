#RosemaryHoffman and Emily Nixon
#A
message=str(input("What is the message you are trying to send?\n"))
def too_long(message):
    if len(message)>140:
        print("string is too long")
    else:
        return None
too_long(message)

import unicodedata
unicodedata.lookup("snake")
unicodedata.lookup("cat")
