###
# Make and iterator to check two arrays.
# array S contains characters, each char corresponds to the numeric value at its position in array C.
# Calculate the minimum cost of removing the duplicates.
###


def iterator(S,C):
    'get duplicates from S'
    'set will get rid of duplicate instances'
    test = set([letter for letter in S if S.count(letter) > 1])
    finalCostArr = []
    'put each set element into a list called dups'
    dups = []
    for element in test:
        x = element
        dups.append(x)
    'determine array positions of each duplicate'
    for letter in dups:
        arr = []
        position = 0
        for element in S:
            if element == letter:
                print("letter = " + letter + " @ position: " + str(position))
                arr.append(position)
            position = position + 1
        #print(str(arr))
        'for each duplicate position in the array (num), find the corresponding value in C'
        newArr = []
        for num in arr:
            x = C[num]
            print("position: " + str(num) + " = value: "+ str(x))
            newArr.append(x)
            newArr.sort()
        print(newArr)
        y = newArr[0]
        finalCostArr.append(y)
        'determine lowest cost'
        total = 0
        for n in finalCostArr:
            total = total + n
        print("final lowest cost: " + str(total))


if __name__ == '__main__':
    S = ['a','b','c','c','d','b','d']
    C = [1,8,6,4,3,5,7]
    result = iterator(S,C)
    print("duplicates are: " + str(result))

