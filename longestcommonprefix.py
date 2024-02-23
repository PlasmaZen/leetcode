def longestCommonPrefix(strs: list[str]) -> str:
    # split list of strings into list of list of strings
    # iterate through each list of lists and if the first set
    # of strings match another append into answer list
    listoflist = [[[k for k in j] for j in i.split()] for i in strs] # list within a list within a list
    print(listoflist)


longestCommonPrefix(["flower","flow","flight"])
# output: 'fl'