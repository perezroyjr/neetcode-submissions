class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return None


    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.arr[self.size] = n
            self.size += 1
        else:
            self.resize()
            self.pushback(n)
        return None

    def popback(self) -> int:
        temp = self.arr[self.size-1]
        self.size -= 1
        return temp

    def resize(self) -> None:
        self.capacity = (self.capacity * 2)
        array_copy = [0] * self.capacity
        
        for i in range(self.size):
            array_copy[i] = self.arr[i]
        
        self.arr = array_copy

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
