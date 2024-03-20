def bulbashka_sort(arr: list[int]):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

my_list = [20, 19, 17, 16, 18, 14, 15]
bulbashka_sort(my_list)
print("Відсортований масив:")
for i in range(len(my_list)):
    print("%d" % my_list[i])
