

class Hello:
    greeting = "Hello, {}!"
    name = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.greeting.format(self.name)


class Goodbye(Hello):
    greeting = "Goodbye, {} :("
    pass

greeting = Goodbye("world")

print(greeting)