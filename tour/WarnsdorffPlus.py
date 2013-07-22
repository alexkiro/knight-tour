from Warnsdorff import Warnsdorff
class WarnsdorffPlus(Warnsdorff):
    def get_plus_factor(self, p):
        """Get the plus factor, in order to select from equally valuable position.
        Measure how far is the point from the center of the table.
        Return a number in the range [0.0,1.0) so it doesn't interfere with
        Warnsdorff's rule. The higher it is the closer to center of the board
        """
        i,j = p / self.m, p % self.m
        f = (abs(i - self.n / 2) + abs(j - self.m / 2)) / float(self.n / 2 + self.m / 2)
        return 1.0 - (f if f != 0.0 else 10 ** (-self.n))
    def calculate(self, p):
        return Warnsdorff.calculate(self, p) + self.get_plus_factor(p)