def countsort(arr):
    freq=[0 for i in range(256)]
    for j in arr:
        freq[ord(j)]+=1 #Incrementing count for the character
    sorted_string=""
    for i in range(256):
        for j in range(freq[i]):
            sorted_string+=chr(i)
    return sorted_string

arr="Information And Communiation Technology"
sorted_string=countsort(arr)
print(sorted_string)