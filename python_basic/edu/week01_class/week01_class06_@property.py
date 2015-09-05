
class Silly:

    @property
    def silly(self):
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoa, you killed silly!")
        del self._silly

mySilly = Silly()

mySilly.silly = "I'm calling getter"
print(mySilly.silly)

