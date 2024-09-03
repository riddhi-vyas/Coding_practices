from queue  import queue_operations
from stack import stack_operations

def q_main():
    object_1 = queue_operations()
    object_1.enque_method(15)
    object_1.enque_method(12)
    object_1.enque_method(14)
    _ = object_1.deque_method()
    return object_1

def s_main():
    object_1 = stack_operations()
    object_1.push_method(5)
    object_1.push_method(2)
    object_1.push_method(4)
    _ = object_1.pop_method()
    return object_1


def extra():
    q_obj = q_main()
    s_obj = s_main()

    while s_obj.is_not_empty():
        q_obj.enque_method(s_obj.pop_method())

    q_obj.show_list()

extra()