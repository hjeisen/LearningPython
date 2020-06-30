#
# Example file for working with classes
#
class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("My class method2 "+someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherclass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("THis is a string")
    c22 = anotherClass()
    c22.method1()
    c22.method2("string test")

  
if __name__ == "__main__":
  main()
