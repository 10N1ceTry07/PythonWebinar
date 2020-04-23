from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother(AbstractParent):
    def hello_friend(self):
        pass

    def init(self, age=0):
        self.age = age
        print('Mother constructor!')

    def do_work(self):
        print("I'm working")

    def do_work_in_kitchen(self):
        print("I'm cooking cake")

    def do_house_work(self):
        print("Listening music")


class Father(AbstractParent):
    def hello_friend(self):
        pass

    def init(self):
        print('Father constructor!')

    def play_guitar(self):
        print('play guitar')

    def do_house_work(self):
        print("sitting on the sofa and drink beer")


class Daughter(Mother, Father):

    def init(self, age=0):
        Mother.init(self, age=age)
        Father.init(self)

    def do_work(self):
        print("I'm working like a horse!")

    def hello_friend(self):
        pass


class Friend:
    pass


def greet_mother(mother: Mother):
    print("Hello mother!!!")
    mother.do_work()


def greet_father(father: Father):
    print('time to beer!')
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    # mother.do_work()

    # change object class :)
    # daughter.class = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    for x in [daughter]:
        x.do_house_work()

    # list
    povtorka_list = ["mathan_2", "superprice"]

    # tuple
    vasian = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 10, "call"}
    print(my_set)

    # frozen set
    another_set = frozenset(["di_", "mi", "do"])

    # dictionary
    my_dict = {1: "first", "2": 123, (1,2,3): "tuple_as_a_key"}