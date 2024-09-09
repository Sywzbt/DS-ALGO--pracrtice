def merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q

  L = A[p:q+1]
  R = A[q+1:r+1]

  i = 0
  j = 0
  k = p

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1

  while i < n1:
    A[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    A[k] = R[j]
    j += 1
    k += 1

def mergeSort(A, l, r):
  if l < r:
    m = l+(r-l)//2
    mergeSort(A, l, m)
    mergeSort(A, m+1, r)
    merge(A, l, m, r)
  return A

A = [7,6,5,4,3,2,1]
mergeSort(A, 0, 6)
print(A)