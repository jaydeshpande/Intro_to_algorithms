class sort_my_array:

    def __init__(self,A):
        self.input_array = A

    def insertion_sort_non_decreasing(self):
        length = len(self.input_array)
        for j in range (1, length):
            card = self.input_array[j]
            i = j-1
            while (i>=0) and (self.input_array[i] > card):
                self.input_array[i+1] = self.input_array[i]
                i -= 1
            self.input_array[i+1] = card
        return self.input_array

    def insertion_sort_non_increasing(self):
        length = len(self.input_array)
        for j in range (0, length):
            card = self.input_array[j]
            i = j + 1
            while (i<length) and (self.input_array[i] < card):
                self.input_array[i-1] = self.input_array[i]
                i += 1
            self.input_array[i-1] = card
        return self.input_array

test = [35, 7, 9, 2, 11, 15, 3, 4, 20, 17, 6]
A = sort_my_array(test)
print A.insertion_sort_non_decreasing()
print A.insertion_sort_non_increasing()
