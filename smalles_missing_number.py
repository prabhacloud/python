def solution(A):
    largest = max(A)
    if largest < 1: #Rules out all negative integers
        return 1
    if len(A) == 1:
        return 2 if A[0] == 1 else 1 #When array has only one element     
    p = [0] * largest  # initializing positive array
    
    for i in range(len(A)): 
        if A[i] > 0: 
            if p[A[i] - 1] != 1:    # setting index status
                p[A[i] - 1] = 1 
    for i in range(len(p)):
        if p[i] == 0:
            return i+1
    return i+2     
num_array = list()
num = raw_input("Enter the legnth of the array:")
print 'Enter elements in array: '
for i in range(int(num)):
    n = raw_input("elements :")
    num_array.append(int(n))
print 'ARRAY: ',num_array
print(solution(num_array))