class Sorting:     
    def __init__(self):
        self.list1 = []


    def bubble_sort_method(self, list1):
        my_list = list1
        n = len(my_list)
        for num in range(n):
            for i in range(num+1, n):
                if my_list[num] > my_list[i]:
                    my_list[i], my_list[num] = my_list[num], my_list[i]
        return my_list


def main():
    data = [2,0,4,1, 6, -2, -3, 5, 6, 7]
    object1 = Sorting()
    result =  object1.bubble_sort_method(data)

if __name__ == "__main__":
    main()