def groupAnagrams(strs: list[str]) -> list[list[str]]:
    #initialize an empty dictionary for storing a sorted string of the word with a list of the words that we're checking
    anagrams = {}

    for word in strs:
        # for each word in the user provided list, we will sort the word alphabetcially and store it as a string (lists are not hashable, and the sorted function returns a list)
        sortStr = str(sorted(word))

        # if the sorted string is not already in the dictionary, add it along with an empty list
        if sortStr not in anagrams:
            anagrams[sortStr] = []

        # append the word into the list for the proper sorted string name
        anagrams[sortStr].append(word)

    # Return as a list, the values for the dicitonary    
    return list(anagrams.values())


if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))