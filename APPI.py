# class Arra for manipulating arrays
class Arra:
    def __init__(self, arr):
        self.arr = arr
        self.S = 0

    def appendd(self, innp):  # appendd method to add user input data
        self.arr.append(innp)

    def spliit(self):   # splitt method to split our array into to arrays with equal size if possible
        if not self.arr:  # check to see if the array is empty
            return "Array is empty"
        self.S += self.arr[-1]
        if self.S % 2 == 0:  # check to see if the sum of array is an even number so if we can split it
            halfOfSum = self.S / 2
            sumofFirstElements = 0
            for i in range(0, len(self.arr)):
                sumofFirstElements += self.arr[i]
                if sumofFirstElements > halfOfSum:
                    return "spliting is not possible for this array"
                if sumofFirstElements == halfOfSum:
                    return [self.arr[0:i + 1], self.arr[i + 1:]]
        else:  # if the array sum is odd, we can not split it in two, because our elements are all integers
            return "splitting is not possible"
        return 0
