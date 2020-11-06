class Str:
    MAX_LENGTH = 10;

    def middle(self, str):
        length = len(str)
        if (length > Str.MAX_LENGTH):
            return "too long"
        if (length % 2 == 0):
            return str[length/2-1:length/2+1]
        else:
            return str[length/2:length/2+1]


str = Str()
print(str.middle("abcd"))
print(str.middle("abcde"))
