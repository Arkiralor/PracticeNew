class A:
    a:int = None

    def __init__(self, a:int):
        self.a = a

    def __repr__(self):
        return f"A(a={self.a})"


class B(A):
    b:int = None

    def __init__(self, b:int):
        self.b = b
    
    def __repr__(self):
        return f"B(b={self.b})"
    

class C(B):
    c:int = None

    def __init__(self, c:int):
        self.c = c
    
    def __repr__(self):
        return f"C(c={self.c})"

if __name__=="__main__":
    a = A(1)
    b = B(2)
    c = C(3)
    print(a)
    print(b)
    print(c)
    print(A.__subclasses__())
    print(B.__subclasses__())
    print(C.__subclasses__())