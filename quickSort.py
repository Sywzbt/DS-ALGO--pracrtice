def swap(A, i, j):
  temp = A[i]
  A[i] = A[j]
  A[j] = temp

def partition(A, p, r):
  pk = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= pk:
      i = i + 1
      swap(A, i, j)
  swap(A, i+1, r)
  return i+1

def quickSort(A, p, r):
  if p < r:
    q = partition(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)
  return A

A = [7,6,5,4,3,2,1]
quickSort(A, 0, 6)
print(A)