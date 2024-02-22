class Frac:
    
    def __init__(self, num, den):
        
        """Parameters:
            num: int
            den: int
        
            Returns: Creates instance of Frac"""
        
        self.num = num
        self.den = den
        return
    
    def gcd(a, b):
        
        """Parameters:
            a: int
            b: int
        
            Returns: Greatest Common Denominator"""
        
        while b:
            a, b = b, a % b
        return a
    
    def simplify(self):
        
        """Simplifies fraction of self"""
        
        common_divisor = Frac.gcd(self.num, self.den)
        simplified_num = self.num // common_divisor
        simplified_den = self.den // common_divisor
        self.num = simplified_num
        self.den = simplified_den
        return
    
    def __add__(self, other):
        
        """Parameters:
            other: Frac
            
            Returns: Result of + operation"""
            
        final_denominator = self.den * other.den
        final_numerator = self.den * other.num + self.num * other.den
        
        result = Frac(final_numerator, final_denominator)
        
        result.simplify()
        
        return result
    
    def __sub__(self, other):
        
        """Parameters:
            other: Frac
            
            Returns: Result of - operation"""
            
        final_denominator = self.den * other.den
        final_numerator = other.den * self.num - self.den * other.num
        
        result = Frac(final_numerator, final_denominator)
        
        result.simplify()
        
        return result
    
    def __mul__(self, other):
        
        """Parameters:
            other: Frac
            
            Returns: Result of * operation"""
            
        final_numerator = self.num * other.num
        final_denominator = self.den * other.den
            
        result = Frac(final_numerator, final_denominator)
        
        result.simplify()
        
        return result
    
    def __truediv__(self, other):
        
        """Parameters:
            other: Frac
            
            Returns: Result of / operation"""
        
        swapped_frac = Frac(other.den, other.num)
        
        return self * swapped_frac
    
    def __gt__(self, other):
        
        """Parameters:
            other: Frac
            
            Returns: Result of > operation"""
        
        self_num = self.num * other.den
        other_num = other.num * self.den
        return self_num > other_num
    
    def __str__(self):
        
        """"
        Returns: User friendly representation"""
        
        return str(self.num) + "/" + str(self.den)

    
    
        
            
            