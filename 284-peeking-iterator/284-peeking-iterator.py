class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.temp = None
        if self.it.hasNext():
            self.temp = self.it.next()

    def peek(self):
        return self.temp

    def next(self):
        curr = self.temp
        if self.it.hasNext():
            self.temp = self.it.next()
        else:
            self.temp = None
        return curr

    def hasNext(self):
        return self.temp is not None