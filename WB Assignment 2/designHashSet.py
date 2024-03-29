class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.setList = []

    def add(self, key: int) -> None:
        if key not in self.setList:
            self.setList.append(key)

    def remove(self, key: int) -> None:
        if key in self.setList:
            self.setList.pop(self.setList.index(key))

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.setList
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)