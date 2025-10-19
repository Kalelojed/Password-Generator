import random

class Generator:
    def __init__(self):
        self.lowerAlph='abcdefghijklmnopqrstuvwxyz'
        self.upperAlph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nums='0123456789'
        self.symbols="""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""

    def GeneratePass(self, Length:int, includeUpper:bool, includeLower:bool, includeNums:bool, includeSymbols:bool) -> str:
        password = ''
        while len(password) < Length:
            charType = random.randint(1, 4)
            match charType:
                case 1:
                    if includeLower == True:
                        password += random.choice(self.lowerAlph)
                case 2:
                    if includeUpper == True:
                        password += random.choice(self.upperAlph)
                case 3:
                    if includeNums == True:
                        password += random.choice(self.nums)
                case 4:
                    if includeSymbols == True:
                        password += random.choice(self.symbols)
        return password