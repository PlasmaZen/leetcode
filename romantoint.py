def romanToInt(s: str) -> int:
    numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_list = [i for i in s]
    print(numeral_list)

print(romanToInt("III"))
