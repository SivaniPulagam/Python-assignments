def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Largest element is:", list1[length-1])
    print("Smallest element is:", list1[0])
    print("difference between largest and smallest :",list1[length-1]-list1[0])
 
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)
