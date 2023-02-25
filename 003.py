'''
Module to print the class name of an object.
'''

class HelloWorld:
    '''
    Test class.
    '''
    name:str=None

    def __init__(self, name:str=None):
        self.name = name
    def __repr__(self):
        rep = {
            "name":self.name
        }
        return rep
    def salutation(self):
        sal = f"Hello, {self.name} and welcome to Python."
        print(sal)

def main():
    name:str = "Bubba"
    hello_world = HelloWorld(name)
    class_name = type(hello_world).__name__
    print(class_name)

if __name__ == "__main__":
    main()

