class queue_operations:
    def __init__(self):
        self.q_list = []

    def enque_method(self,item):
        self.q_list.append(item)

    def deque_method(self):
        n = len(self.q_list)
        if n != 0:
            popped_item = self.q_list[0]
            self.q_list = self.q_list[1:n]
            return popped_item
        else:
            return -1
    
    def show_list(self):
        print(self.q_list)
