from linkedlist import LinkedList

if __name__ == "__main__":
    
    linked_list1 = LinkedList()

    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.append(False)
    linked_list1.insert_before("a", "D")
    linked_list1.insert_after("D", "B")


    print(linked_list1)

    print(linked_list1.includes("a"))
    