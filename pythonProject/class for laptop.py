class laptop:
    #tgp = "latech" tisalso works for the general self.tgp

    def __init__(self, processor, ssd, ram, rom, gup):
        self.prc = processor
        self.ss = ssd
        self.rm = ram
        self.ro = rom
        self.gp = gup
        self.tgp = "latech"

L1 = laptop(22,44,4,44,44)
L2 = laptop(22,22,11,3,45)
print(L2.rm)
print(L1.gp)
print(L1.rm)
print(L1.tgp)
a = input("what is your name:")