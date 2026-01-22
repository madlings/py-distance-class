class Distance:

    def __init__(self, km : int) -> None:
        self.km = km

    def __add__(self, other) -> "Distance":
        lkm = 0
        if(isinstance(other, (int, float))):
            lkm = other
        elif isinstance(other, Distance):
            lkm = other.km
        else:
            raise TypeError("given type not valid, use int or float")
        return Distance(self.km + lkm)

    def __mul__(self, other: "Distance") -> "Distance":
    	return Distance(self.km * other.km)

    def __truediv__(self, other: "Distance") -> "Distance":
    	return Distance(round(self.km / other.km, 2))

    def __iadd__(self, other) -> "Distance":
        if( isinstance(other, (int, float))):
            self.km += other
        else:
        	raise TypeError("given type not valid, use int or float")
        return self

    def __eq__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km == other
        elif isinstance(other, Distance):
            return self.km == other.km
        else:
        	raise TypeError("given type not valid, use int or float")

    def __ne__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km != other
        elif isinstance(other, Distance):
            return self.km != other.km
        else:
        	raise TypeError("given type not valid, use int or float")

    def __lt__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km < other
        elif isinstance(other, Distance):
            return self.km < other.km
        else:
        	raise TypeError("given type not valid, use int or float")

    def __le__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km <= other
        elif isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError("given type not valid, use int or float")

    def __gt__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km > other
        elif isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError("given type not valid, use int or float")

    def __ge__(self, other) -> bool:
        if( isinstance(other, (int, float))):
            return self.km >= other
        elif isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError("given type not valid, use int or float")
