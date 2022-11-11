num1 = int(input("Enter no. of shirts in stock:\t"))
a = input ("Enter the shirt sizes available:")
num2 = int(input("Enter np. of shirts required:\t"))
b = input("Enter the required shirt sizes")
L1 = a.split()
L2 = b.split()
result = True
if num1>num2 and len(L1) == num1 and len(L2) == num2:
    for size in L2:
        for new in L1:

            if len(size) != len(new):
                    if size[-1] == "S":
                        if new[-1] in ["M", "L"]:
                            result = True
                            break
                           
                        else:
                            if len(size[0:-2:1]) > len(new[0:-2:1]):
                                result = True
                                break
                                
                            else:
                                result = False
                                #break
                                
                    elif size[-1] == "M":
                        if new[-1] in ["L"]:
                            result = True
                            break
                            
                        else:
                            #
                            if len(size[0:-2:1]) > len(new[0:-2:1]):
                                result = False
                                #break
                            else:
                                result = True
                                break
                                
                    elif size[-1] == "L":
                        if new[-1] in ["L"]:
                                if len(size[0:-2:1]) > len(new[0:-2:1]):
                                    result = False
                                    #break
                                else:
                                    result = True
                                    break
                                    
                        else:
                            result = False
                            #break
            else:
                if size[-1] == "S":
                    if new[-1] == "S":
                        result = True
                        break
                        
                    else:
                        result = False
                elif size[-1] == "M":
                    if new[-1] in ["S", "M"]:
                        result = False
                    else:
                        result = True
                        break
                        
                else:
                    if new[-1] == "L":
                        result = True
                        break
                        
                    else:
                        result = False
    if result == True:
        print ("Yes")
    else:
        print ("No")
else:
    print ("No")

    


                
