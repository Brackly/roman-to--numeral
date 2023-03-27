def roman_to_integer(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    c=roman_map.keys()
    integer_value = 0
    prev_value = 0
    # IV
    for char in s:
        if char not in c:
            return "The roman numeral is invalid"
        curr_value = roman_map[char]
        if curr_value > prev_value:
            integer_value += curr_value - 2*prev_value
        else:
            integer_value += curr_value
        prev_value = curr_value
    return integer_value


def main():
    x=input()
    print(roman_to_integer(x))

if __name__=="__main__":
    main()