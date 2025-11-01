class PublicNumberList:
    def __init__(self):
        self.data = []

    def insert_number(self, num):
        self.data.append(num)

    def find_number(self, x):
        for i in range(len(self.data)):
            if self.data[i] == x:
                return i + 1
        return -1