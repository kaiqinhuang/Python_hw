def julia(c, max = 100):
    """ Takes a complex parameter c and an optional positive integer max, and returns a function specified by the following:
        
        The function should take one complex parameter z as an input, and return a positive integer n.
        
        The returned integer n should count how many times the complex parameter z can be transformed
        as z = z**2 + c before the resulting magnitude |z| exceeds 2.
        
        If the number max is reached before the magnitude of z exceeds 2, the function should return the number 0.
        
        If the number z already has a magnitude larger than 2, the function should return 1.
    """
    
    def transform(z):
    
        n = 0
    
        if abs(z) > 2:
            return 1
        else:
            while abs(z) <= 2:
                z = z ** 2 + c
                n += 1
                if n > max:
                    return 0

        return n

return tranform()
