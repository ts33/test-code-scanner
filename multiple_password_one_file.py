"""
    The purpose of this file is to generate multiple findings in code scanner with the same signature.
    Bandit will generate several findings, 1 for each hardcoded password. 
    As the author, filename and reponame are the same, the signature will be the same.
"""
def login(username, password):
    pass


def func1():
    login(username='timothy', password='password123')


def func2():
    login(username='timothy', password='password123')


def func3():
    login(username='timothy', password='password123')


def func4():
    login(username='timothy', password='password123')
