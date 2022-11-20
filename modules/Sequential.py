import time

class SequentialSort:
    def __init__(self, name_dict : dict):
        self.nd = name_dict

    def partition(self, low: int, high: int, firstLast: str):
        pivot = self.nd[high][firstLast]

        i = low - 1

        for j in range(low, high):
            if self.nd[j][firstLast] <= pivot:
                i = i + 1
                (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])

        (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])

        return i + 1

    def quicksort(self, low: int, high: int, firstLast: str):
        if low < high:
            part = self.partition(low, high, firstLast)

            self.quicksort(low, part - 1, firstLast)

            self.quicksort(part+1, high, firstLast)

    def count_groups(self, low: int, high: int):
        count_high = 0

        for j in range(low,high):
            if self.nd[j]['last'] == self.nd[j+1]['last']:
                count_high+=1
            elif count_high > 0:
                return [count_high, j+1]
            else:
                pass

    def sort_names(self):
        print("\nSHOWING TOP 10 FROM FILE")
        for i in range(0,10):
            print(self.nd[i]['first'] + ' ' + self.nd[i]['last'])

        self.quicksort(0,len(self.nd)-1, 'last')
        init = 0
        high = -1

        while init < len(self.nd)-1:
            high = self.count_groups(init,len(self.nd)-1)
            if high is None:
                break
            elif high[0] > 0:
                self.quicksort(init, init+high[0], 'first')
                init=high[1]
            elif high[0] == 0:
                init = high[1]

        print("\nSHOWING TOP 10 FROM SORT")
        for i in range(0,len(self.nd)-1):
            print(self.nd[i]['first'] + ' ' + self.nd[i]['last'])
