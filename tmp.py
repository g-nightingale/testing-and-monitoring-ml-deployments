class Superman:
    def __init__(self):
        self.superpowers = ['flight']

    def print_superpowers(self):
        print(f"Superpowers {self.superpowers}")

sm = Superman()
sm.print_superpowers()


class Megaman(Superman):
    def __init__(self, megaman_powers=[]):
        super().__init__()
        self.superpowers.extend(megaman_powers)

mm = Megaman(megaman_powers=['x-ray vision', 'insane speed'])
mm.print_superpowers()