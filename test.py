import os

class GithubTest():
    def __init__(self, clear: bool):
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')
        print("GithubTest has run!")