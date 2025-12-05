
class Calculator:
    def add(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b

    def mul(self, a, b):
        return a * b
    
    def sqrt(self, x):
        if x < 0:
            raise ValueError("no se puede con numeros negativos")
        if x == 0:
            return 0

        guess = x
        for _ in range(50):  
            new_guess = 0.5 * (guess + x / guess)
            if abs(new_guess - guess) < 1e-6:
                break
            guess = new_guess
        
        return new_guess

    def exp(self, x):
        term = 1.0
        result = 1.0
        n = 1
    
        while abs(term) > 1e-6 and n < 100:
            term = term * x / n
            result += term
            n += 1

        return result


