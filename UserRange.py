class UserRange:

    def __init__(self,start, end=None , step=1):
        if end == None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration
        
if __name__ == "__main__":
    for i in UserRange(2,10,2):
        print(i)