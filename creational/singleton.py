'''
Singleton Pattern

Deliver a singleton Lone warrior object

Singleton Class : LoneWarrior
'''

class LoneWarrior:
    _warrior = None
    def getWarrior(self):
        if not LoneWarrior._warrior:
            LoneWarrior._warrior = LoneWarrior()
        return LoneWarrior._warrior

def Main():
     samurai = LoneWarrior()
     military = LoneWarrior()

     print(military.getWarrior())
     print(samurai.getWarrior())

if __name__ == '__main__':
    Main()


'''
<__main__.LoneWarrior instance at 0x027F1B98>
<__main__.LoneWarrior instance at 0x027F1B98>
'''