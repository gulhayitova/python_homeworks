class Vector:
    def __init__(self, *n):
        self.n = tuple(n)

    def __repr__(self):
        return f"{self.n}"
    
    def __sub__(self, other):
            if isinstance(other, Vector) and len(other.n) == len(self.n):
                return Vector(*[a - b for a, b in zip(self.n, other.n)])
            else:
                return "Vectors must have the same dimension to perform subtraction."
    
    def __add__(self, other):
         if isinstance(other, Vector) and len(self.n) == len(other.n):
              return Vector(*[a + b for a, b in zip(self.n, other.n)])
         else:
              return "Vectors must have the same dimension to perform addition."

    def __mul__(self, other):
         if isinstance(other, Vector) and len(self.n) == len(other.n):
              return Vector(*[a * b for a, b in zip(self.n, other.n())])
         elif isinstance(other, int) or isinstance(other, float):
              return Vector(*[a * other for a in self.n])
         else:
              return "Vectors must have the same dimension to perform multiplication."
    def __div__(self, other):
         if isinstance(other, Vector) and len(self.n) == len(other.n):
              return Vector(*[a / b for a, b in zip(self.n, other.n)])
         else:
              return "Vectors must have the same dimension to perform division."
         
    def magnitude(self):
         l = sum([a * a for a in self.n]) ** 0.5
         return l
    
    def dot_product(self, other):
         if isinstance(other, Vector) and len(other.n) == len(self.n):
              return sum([a * b for a, b in zip(self.n, other.n)])
    def normalize(self):
         try:
              return Vector(*[round(a / self.magnitude(), 3) for a in self.n])
         except ZeroDivisionError:
              return "A zero vector cannot be normalized."
