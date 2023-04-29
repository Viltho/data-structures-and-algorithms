from linkedlist import LinkedList

if __name__ == "__main__":
    
    linked_list1 = LinkedList()

    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.append(False)
    linked_list1.insert_before("a", "D")
    linked_list1.insert_after("D", "B")
    linked_list1.delete("D")
    print(linked_list1.kthfromend(2))

    print(linked_list1)

    print(linked_list1.includes("a"))
    