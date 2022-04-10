class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.hmap = dict()
        self.keyss = keys
        self.dict = dictionary
        for i in range(len(keys)):
            self.hmap[keys[i]] = values[i]

    def encrypt(self, word1: str) -> str:
        ans = ""
        for i in word1:
            if i in self.keyss:
                ans += self.hmap[i]
            else:
                ans = ""
        return ans
    # O(100*100) = 10^4
    def decrypt(self, word2: str) -> int:
        ans = 0
        for w in self.dict:
            if self.encrypt(w) == word2:
                ans += 1
        return ans

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)