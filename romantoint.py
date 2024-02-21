def romanToInt(s: str) -> int:
    numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_list = [i for i in s]
    answer = 0
    # i need to go through the list and convert each value to an integer with the key value in the dictionary
    for i in range(len(numeral_list)):
        if numeral_list[i] in numeral_values:
            if i < len(numeral_list) - 1:
                if numeral_values[numeral_list[i + 1]] > numeral_values[numeral_list[i]]:
                    answer -= numeral_values[numeral_list[i]]
                else:
                    answer += numeral_values[numeral_list[i]]
            else:
                answer += numeral_values[numeral_list[i]]
            # chatgpt said that i need to put numerallist[i] in numeral value
    return answer

print(romanToInt("IX"))

