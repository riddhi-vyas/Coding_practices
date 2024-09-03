class stack_operations:
    def __init__(self):
        self.s_list = []

    def push_method(self, item):
        self.s_list.append(item)

    def pop_method(self):
        if self.is_not_empty():
            n = len(self.s_list)
            popped_item = self.s_list[n-1]
            self.s_list = self.s_list[0:n-1]
            return popped_item
        else:
            return None

    def show_list(self):
        print(self.s_list)

    def is_not_empty(self):
        n = len(self.s_list)
        if n!=0:
            return True
        else:
            return False