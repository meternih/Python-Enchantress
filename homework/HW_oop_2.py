class Laptop():
    """composition"""

    def __init__(self):
        os_windows = OS('tekst 1')
        os_linuks = OS('tekst 2')
        self.os = [os_windows, os_linuks]

    def print_os(self):
        print(self.os)
        for os in self.os:
            print(os.content)

class OS:
    def __init__(self, content):
        self.content = content


laptop = Laptop()
laptop.print_os()



class Guitare:
    """aggregation"""

    def __init__(self, string):
        self.string = string

    def issue(self):
        print(f'Issue {self.string.string_type} string...')


class String:
    def __init__(self, string_type):
        self.string_type = string_type

string = String('havy metal')
guitare = Guitare(string)
guitare.issue()

string_type = string.string_type
print((string_type))
