from functools import reduce


def dict_problem_one():
    courses = [{'coursenum': 'CS121', 'desc': 'Intro to Problem Solving with Computers', 'cred': 4},
               {'coursenum': 'CS145', 'desc': 'Storing, and Retrieving Information', 'cred': 3},
               {'coursenum': 'CS145', 'desc': 'Programming with Data Structures', 'cred': 4}]

    for course in courses:
        print(course['cred'])


def problem_three():
    mylist = [1, 2, 3, 4, 5]
    print(max(mylist))
    print(reduce(lambda x, y: x if x > y else y, mylist))


def problem_six():
    mylist = [1, 2, 3, 4, 5]
    for v in map(lambda x: x * 2, mylist):
        print(str(v))


class AbstractClass:
    def __init__(self, handle):
        self.handle = handle

    def abstract_method(self):
        pass


class ImplementsAbstract(AbstractClass):
    def abstract_method(self):
        print(self.handle)


if __name__ == '__main__':
    ImplementsAbstract("Handle").abstract_method()
