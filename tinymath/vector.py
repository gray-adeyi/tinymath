# Vector Class With Its Operations
# Note that most of the operations do not alter the vector but return a new vector.

from math import cos, sqrt


class Vector:
    def __init__(self, x: float, y: float, z: float, w: float):
        """Initializing the vector components"""
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    def zero(cls):
        """Returns a zero Vectors"""
        return cls(x=0.0, y=0.0, z=0.0, w=0.0)

    def __add__(self, other: "Vector") -> "Vector":
        """Override To Use The + sign To Add Two Vectors"""
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w

        return Vector(x, y, z, w)

    def __sub__(self, other: "Vector") -> "Vector":
        """Override To Use The - sign To Subtract Two Vectors"""
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w

        return Vector(x, y, z, w)

    def scalar_mul(self, scalar: float) -> "Vector":
        """Multiply a vector by a value to scale"""
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        w = self.z * scalar

        return Vector(x, y, z, w)

    def scalar_div(self, scalar: float) -> "Vector":
        """Convenience function for diving vector by scalar"""
        x = self.x * (1 / scalar)
        y = self.y * (1 / scalar)
        z = self.z * (1 / scalar)
        w = self.z * (1 / scalar)

        return Vector(x, y, z, w)

    def magnitude(self) -> float:
        """Get the Magnitude of the Vector"""
        sq_sums = (self.x**2) + (self.y**2) + (self.z**2) + (self.z**2)
        return sqrt(sq_sums)

    def negate(self) -> "Vector":
        """Negate the vector"""
        x = -self.x
        y = -self.y
        z = -self.z
        w = -self.w

        return Vector(x, y, z, w)

    def normalize(self) -> "Vector":
        """Normalize the vector"""
        if self.magnitude == 0:
            raise ValueError("Can't Normalize Zero Vector")
        x = self.x / self.magnitude()
        y = self.y / self.magnitude()
        z = self.z / self.magnitude()
        w = self.w / self.magnitude()

        return Vector(x, y, z, w)

    def dot_product(self, other) -> "Vector":
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        w = self.w * other.w

        return x + y + z + w

    def dot_product_angle(self, other: "Vector", angle: float) -> float:
        return self.magnitude() * other.magnitude() * cos(angle)

    def cross_product(self, other: "Vector") -> "Vector":
        x = (self.y * other.z) - (self.z * other.y)
        y = (self.z * other.x) - (self.x * other.z)
        z = (self.x * other.y) - (self.y * other.x)

        return Vector(x, y, z, w=0.0)

    def __str__(self) -> str:
        return f"Vector: x={self.x}, y={self.y}, z={self.z}, w={self.w}"
