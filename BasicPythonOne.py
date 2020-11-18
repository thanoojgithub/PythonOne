import datetime
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fileiowrite():
    try:
        f = open("demofile.txt", "wt")
        f.writelines(["ram","sita","bharat","lakshman","hanuma"])
    except IOError:
        print("Issue while fileiowrite")
    finally:
        f.close()

def fileioapend():
    try:
        f = open("demofile.txt", "at")
        f.writelines(["ram","sita","bharat","lakshman","hanuma"])
    except IOError:
        print("Issue while fileiowrite")
    finally:
        f.close()

def fileioread():
    try:
        f = open("demofile.txt", "rt")
        print(f.readline())
    except IOError:
        print("Issue while fileiowrite")
    finally:
        f.close()
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exist")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getnameage(self):
        try:
            if not type(self.age) is int:
                raise TypeError("Only integers are allowed")
            x = datetime.datetime.now()
            print(x)
            print("Hello my name is ", self.name, ", age ", self.age)
        except NameError:
            print("An NameError exception occurred")
        except TypeError:
            print("An TypeError exception occurred")
        except IOError:
            print("An IOError exception occurred")
        finally:
            print("final block code")

    def getname(self):
        print("Hello me", self.name)
        return self.name


class User(Person):
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    username = input("Enter username:")
    age = int(input("Enter age:"))
    p1 = User(username, age)
    p1.getnameage()
    print(p1.getname())
    fileiowrite()
    fileioapend()
    fileioread()
