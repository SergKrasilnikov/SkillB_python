class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)

mydict = MyDict()

print(mydict.get('1'))