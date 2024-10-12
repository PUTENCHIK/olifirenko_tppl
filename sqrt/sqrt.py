class R:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
    
    def simple(self):
        self.num = self.num // self.den
        self.den = 1

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __int__(self):
        return int(self.num / self.den)

def f(num: int):
    x = R(num, 2)
    y = R(num*x.den*x.den + x.num*x.num, x.num*x.den*2)
    y.simple()
    s = R(x.num*y.den - y.num*x.den, x.den*y.den)
    while (s.num >= s.den):
        x = y
        y = R(num*x.den*x.den + x.num*x.num, x.num*x.den*2)
        y.simple()
        s = R(x.num*y.den - y.num*x.den, x.den*y.den)
    return y


def square(num):
    x = num / 2
    y = (x + (num / x)) // 2
    while(x - y >= 1):
        x = y
        y = (x + (num / x)) // 2
    return y

if __name__ == "__main__":
    i = 30
    print(f"\t{i}\t{f(i)}")

