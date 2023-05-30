class MyHashTable:
    def __init__(self):
        self.__table = [None] * 1000

    # Public methods
    def add(self, name, score):
        name = self._myHash(name)
        try:
            self.__table[name]
        except:
            self._extend(name)
        finally:
            if self.__table[name] is None:
                self._singleAdd(name, score)
            else:
                self._multiAdd(name, score)

    def getScore(self, name):
        name = self._myHash(name)
        if name > len(self.__table) or self.__table[name] is None:
            return 'Name not found'
        return self.__table[name]

    # Protected methods

    def _myHash(self, name : str) -> int:
        sum = 0
        for i in range(len(name)):
            sum += ord(name[i])
        return sum
    
    
    def _singleAdd(self, name, score):
            self.__table[name] = score

    def _multiAdd(self, name, score):
        try:
            self.__table[name].append(score)
        except:
            tmp = [self.__table[name]]
            self.__table[name] = tmp
            self.__table[name].append(score)
    
    def _extend(self, name):
        for _ in range((name + 1) - len(self.__table)):
            self.__table.append(None)


def start():
    st = MyHashTable()
    while True:
        data = input('Enter the name of the student and their score separated by space or press Enter to quit ')
        if data == '':
            print('Done with this shit')
            break
        data = data.split()
        st.add(data[0], int(data[1]))
    
    while True:
        name = input('Enter the name of the student whose score u wanna know or press Enter to quit: ')
        if name == '':
            print('Bye')
            break
        print(st.getScore(name))

if __name__ == '__main__':
    start()
