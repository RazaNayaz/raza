def size_look(shirts, sizes, required, req_size):
    L1 = sizes.split(" ")
    L2 = req_size.split(" ")
    flag = False
    s1 = set (L1)
    s2 = set (L2)
    z = s2.intersection(s1) # for removing 1 instance of the same sizes...(just a trial..for debugging)
    for element in z:
        a = L2.index(element)
        b = L1.index(element)
        L1.pop(b)
        L2.pop(a)
    else: # for all the remaining elements
        for i in L2:
            for j in L1:
                if i[-1] == "S" and j[-1] in {"S", "M", "L"}:
                    index_i = L2.index(i)
                    index_j = L1.index(j)
                    L1.pop(index_j)
                    break
                elif i[-1] == "M" and j[-1] in {"M", "L"}:

                    index_i = L2.index(i)
                    index_j = L1.index(j)
                    L1.pop(index_j)
                    break
                elif i[-1] == "L":
                    if j[-1] in {"L"}:
                        index_j = L1.index(j)
                        L1.pop(index_j)
                        break
                else:
                    flag = True # need to return This properly 
                    break
        

    if flag == True:
        return ("No")
    else:
        return ("Yes")

shirts = int(input("Number of shirts in stock:\t"))
sizes = input("Sizes in stock:\t")
required = int(input("Required t-shirts:\t"))
req_size = input("Sizes required:\t")
if shirts > required:
    print(size_look(shirts, sizes, required, req_size))
else:
    print ("Invalid")

    
    
