class bird:
    def __init__(self):
        print("Bird is Ready")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("swim faster")
class emu(bird):
    def __init__(self):
        super().__init__()
    def whoisthis(self):
        print("emu")
    def run(self):
        print("run faster")
em=emu()
em.whoisthis()
em.swim()
em.run()