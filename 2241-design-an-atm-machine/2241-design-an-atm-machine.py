class ATM:
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0]
        self.note = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.arr[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        k = 4
        res = [0, 0, 0, 0, 0]
        while k >= 0 and amount > 0:
            curNote = self.note[k]
            if amount >= curNote and self.arr[k]:
                quant = amount//curNote
                num = min(self.arr[k], quant)
                res[k] = num
                amount -= (curNote*num)
            k -= 1
        if amount:
            return [-1]
        else:
            for i in range(5):
                self.arr[i] -= res[i]
            return res
        
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)