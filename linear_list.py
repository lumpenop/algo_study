class LL:
    def __init__(self):
        self.list = []


    def get_list(self):
        return self.list

    def add(self, data, index):
        if len(self.list) < index or index < 0:
            print('범위 초과')
            return

        self.list.append(None)

        for i in range(len(self.list) - 2, index, -1):
            self.list[i + 1] = self.list[i]
            self.list[i] = None

        self.list[index] = data

    def delete(self, index):
        if len(self.list) < index or index < 0:
            print('범위 초과')
            return

        self.list[index] = None

        for i in range(index, len(self.list) - 1):
            self.list[i] = self.list[i + 1]
            self.list[i + 1] = None

        del self.list[-1]


a = LL()

print(a.get_list())

a.add(1, 0)
a.add(1, 1)
a.add(1, 2)
a.delete(0)

print(a.get_list())

