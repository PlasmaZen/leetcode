def romanToInt(s: str) -> int:
    numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_list = [i for i in s]
    answer = 0
    # i need to go through the list and convert each value to an integer with the dictionary
    for i in len(numeral_list):
        if i in numeral_values:
            answer += i

print(romanToInt("III"))
