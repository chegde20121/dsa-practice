def search_arr(arr, x):
    for num in arr:
        if num == x:
            return True
    return False


A = [10, 20, 30, 40, 50]
X = 30

if search_arr(A, X):
    print("YES")
else:
    print("NO")