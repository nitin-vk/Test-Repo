class Calculator:
    a = 10
    b = 20
    
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        print("division print")
        return a/b
    
    def pow(self, a, b):
        return self.a ** self.b
    
    print("These are the calculators")
