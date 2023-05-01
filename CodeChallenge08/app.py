from linkedlist import LinkedList, zip_lists

if __name__ == "__main__":
    
    linked_list1 = LinkedList()
    linked_list1.append("a")
    linked_list1.append("b")

    linked_list2 = LinkedList()
    linked_list2.append("a")
    linked_list2.append("b")
    linked_list2.append("c")

    linked_list3 = zip_lists(linked_list1,linked_list2)
    
    print(linked_list3)
    