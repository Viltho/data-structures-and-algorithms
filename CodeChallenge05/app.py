from linkedlist import LinkedList

if __name__ == "__main__":
    
    linked_list1 = LinkedList()

    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")

    print(linked_list1)

    print(linked_list1.includes("a"))
