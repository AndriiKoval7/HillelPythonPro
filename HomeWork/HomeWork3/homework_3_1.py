def gcd(num,den):
    """function to reduce a fraction to the greatest common divisor"""
    if den == 0:
        print("Oops!  You can't divide by zero!")
        return
    while (num % den != 0):
        old_num = num
        old_den = den
        num = old_den
        den = old_num % old_den
    return den


class Fraction:
    """the Fraction class (fractional numbers),
    which has methods for adding, subtracting,
    multiplying, and dividing two objects of this class"""
    def __init__(self, num,den):
        if den == 0:
            print("Value Error! The denominator can not be zero")
            return
        self.num=num
        self.den=den

    def __repr__(self):
        if (self.num == self.den):
            return "1"
        elif (self.num > self.den):
            fractional_part = self.num // self.den
            new_fraction = Fraction(self.num % self.den, self.den)
            return "{0}/{1}, або {2} цілих і {3}".format(self.num, self.den, fractional_part, new_fraction)
        else:
            return "{0}/{1}".format(self.num, self.den)

    def __add__(self, next_fraction):
        new_num = self.num * next_fraction.den + self.den * next_fraction.num
        new_den = self.den * next_fraction.den
        gcomd = gcd(new_num,new_den)
        return Fraction(new_num // gcomd, new_den // gcomd)

    def __sub__(self, next_fraction):
        new_num = self.num * next_fraction.den - self.den * next_fraction.num
        new_den = self.den * next_fraction.den
        gcomd = gcd(new_num, new_den)
        return Fraction(new_num // gcomd, new_den // gcomd)

    def __mul__(self, next_fraction):
        try:
            new_num = self.num * next_fraction.num
            new_den = self.den * next_fraction.den
            gcomd = gcd(new_num, new_den)
            return Fraction(new_num // gcomd, new_den // gcomd)
        except ValueError:
            print("Oops!  It is not possible to multiply fractions.")

    def __truediv__(self, next_fraction):
        if next_fraction.num == 0:
            raise ValueError('The denominator of the fraction becomes zero during division, which is impossible!')
        try:
            reversed_fraction = Fraction(next_fraction.den, next_fraction.num)
            return self * reversed_fraction
        except ValueError:
            print("Oops!  It is not possible to divide fractions.")


fr1 = Fraction(1, 2)
fr2 = Fraction(1, 3)
fr3 = fr1 + fr2
print(fr3)
fr4 = fr1 - fr2
print(fr4)
fr5 = fr1 * fr2
print(fr5)
fr6 = fr1 / fr2
print(fr6)
# fr7 = Fraction(1, 0)
fr9 = Fraction(0, 3)
fr8 = fr1 / fr9
print(fr8)
