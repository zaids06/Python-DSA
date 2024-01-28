from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

# write your code logic
class Human(Animal):
    def move(self):
        print('I can walk and run')

class Dog(Animal):
    def move(self):
        print('I can bark')

class Snake(Animal):
    def move(self):
        print('I can crawl')

class Lion(Animal):
    def move(self):
        print('I can roar')









R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
