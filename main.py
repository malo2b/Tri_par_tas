import random


class TriParTas:
    def __init__(self, list_length):
        self.list_to_tri = []
        self.list_tri = []
        self.list_length = list_length
        self.born_inf = 0
        self.born_sup = 1000

    def generate_list(self):
        self.list_to_tri = [random.randint(self.born_inf, self.born_sup) for _ in range(self.list_length)]
        self.list_tri = self.list_to_tri.copy()

    def entasser(self):
        for i in range(1, len(self.list_tri)):
            ind = i
            while ind > 0 and self.list_tri[ind] < self.list_tri[(ind - 1) // 2]:
                self.list_tri[ind], self.list_tri[(ind - 1) // 2] = self.list_tri[(ind - 1) // 2], self.list_tri[ind]
                ind = (ind - 1) // 2
        print(self.list_tri)

    def depiler(self, d):
        ind = 0
        while ind *2 +1 <= d:
            pp = ind *2 +1
            if (ind+1)*2 <= d and self.list_tri[pp] > self.list_tri[(ind+1)*2]:
                pp = (ind+1)*2
            self.list_tri[ind], self.list_tri[pp] = self.list_tri[pp], self.list_tri[ind]
            ind = pp

    def tri(self):
        self.entasser()
        for i in range(len(self.list_tri)-1, 0, -1):
            self.list_tri[i], self.list_tri[0] = self.list_tri[0], self.list_tri[i]
            self.depiler(i-1)
        self.list_tri.reverse()

    def __str__(self):
        return f"Liste à trier : {self.list_to_tri}\nListe triée : {self.list_tri}"


if __name__ == '__main__':
    tri = TriParTas(100)
    tri.generate_list()
    tri.tri()
    print(tri)
