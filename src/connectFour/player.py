class Player():
    def __init__(self, number):
        self.number = number
        self.moveHistory = []

    def setNumber(self, number):
        self.number = number;

    def getNumber(self):
        return self.number

    def makeMove(self, column):
        self.moveHistory.append(column)

    def getMoveHistory(self):
        return self.moveHistory


def main():
    print("Player main.")

if __name__ == '__main__':
    main()