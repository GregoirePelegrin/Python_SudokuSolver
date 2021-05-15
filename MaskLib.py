class Mask:
    def __init__(self, _s, _v=""):
        self.size = _s
        self.value = _v
        if self.value == "":
            for i in range(self.size):
                self.value += "0"
            self.exposed = 0
            self.maxed = False
        else:
            self.exposed = 0
            for bit in self.value:
                if bit == "1": self.exposed += 1
            if "0" in self.value: self.maxed = False
            else: self.maxed = True
    def __add__(self, o):
        if type(o) == int:
            for i in range(o):
                self.increment()
        return self
    def __sub__(self, o):
        if type(o) == int:
            for i in range(o):
                self.increment()
        return self
    def __str__(self):
        return self.value
    
    def increment(self):
        i = self.size-1
        temp = ""
        while i >= 0 and self.value[i] == "1":
            temp += "0"
            i -= 1
        if not i < 0: 
            temp += "1"
            i -= 1
            while i >= 0:
                temp += self.value[i]
                i -= 1
            result = ""
            for i in range(self.size):
                result += temp[self.size-1-i]
            self.value = result
            if "0" not in self.value: self.maxed = True
        self.exposed = 0
        for bit in self.value:
            if bit == "1": self.exposed += 1
    def decrement(self):
        i = self.size-1
        temp = ""
        while i >= 0 and self.value[i] == "0":
            i -= 1
        if not i < 0:
            for l in range(i):
                temp += self.value[l]
            temp += "0"
            for l in range(i+1, self.size):
                temp += "1"
            self.value = temp
        self.exposed = 0
        for bit in self.value:
            if bit == "1": self.exposed += 1
