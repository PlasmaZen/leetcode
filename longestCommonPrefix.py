def longestCommonPrefix(strs: list[str]) -> str:
    # split list of strings into list of list of strings
    # of strings match another append into answer list
    list_list_letters = [[list(j) for j in i.split()] for i in strs] # list within a list within a list
    answer_list = []
    print(list_list_letters)
    # iterate through each list of lists and if the first set
    for i in list_list_letters:
        # goes through each list in i, only going as far as i[0]
        for j in range(len(i[0])):
            # if [0] is the same on every list, append it to answer list
            # the all() function returns True if the stuff inside it is True
            if all(i[0][j] == k[j] for k in i[1:]):
                answer_list.append(i[0][j])
            else:
                break
    return ''.join(answer_list)

longestCommonPrefix(["flower","flow","flight"])
# output: 'fl'
