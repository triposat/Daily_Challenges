# # 1st Approach: Not good for the same URL passing several times
class Codec:

    def __init__(self):
        self.urlS = []

    def encode(self, longUrl):
        self.urlS.append(longUrl)
        return "http://tinyurl.com/"+str(len(self.urlS)-1)

    def decode(self, shortUrl):
        return self.urlS[int(shortUrl.split("/")[-1])]

# 2nd Approach - Best Approach
import string
import random
class Codec:

    def __init__(self):
        self.deco = {}
        self.enco = {}
        self.alphanum = string.ascii_letters+"0123456789"

    def encode(self, longUrl):
        while longUrl not in self.enco:
            tinyCode = "".join(random.choice(self.alphanum) for _ in range(6))
            if tinyCode not in self.deco:
                self.deco[tinyCode] = longUrl
                self.enco[longUrl] = tinyCode
        return "http://tinyurl.com/"+self.enco[longUrl]

    def decode(self, shortUrl):
        return self.deco[shortUrl[-6:]]
