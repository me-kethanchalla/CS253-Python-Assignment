def validate_input( n, s):
    if n<=0 :
        raise ValueError("Entered n is negative number. n must be a positive integer.")
    elif len(s)<=0 :
        raise ValueError("Entered string is empty. s must be a non-empty string.")
    elif s.isalpha() == False :
        raise ValueError("Text must be a contain alphabets only.")
    
    else :
        pass


def process_string(n, s) :

    # even registration number -> should reverse the text
    if (n%2 == 0) :
        reversed = s[::-1]
        return reversed

    # odd registration number -> should capitalise the vowels 
    else :
        vowels = ['a','e', 'i', 'o', 'u' ]

        # strings are immutable in python and we cannot capitalise them in the same string
        # initialize a new string
        new_s = ""
        for char in s:
            if char in vowels :
                new_s = new_s + char.upper()
            else :
                new_s = new_s + char.lower()  

        return new_s


def count_set_bits(n) :
    temp = n
    binary_1s = 0

    while(temp!=0) :
        if (temp%2 == 0) :
            binary_1s += 0
        else :
            binary_1s += 1

        temp = temp//2    

    count = binary_1s
    return count


def extract_substrings(s, k) :
    n = len(s)
    num_substrings = n+1-k
    substrings = []
    for i in range(num_substrings) :
        substrings.append(s[i:i+k:1])

    return substrings


def sort_or_reverse(n,s, substrings):
    if (n & len(s)== 0) :
        sorted_substrings = sorted(substrings)
        return sorted_substrings

    else :
        reversed_substrings = substrings[::-1]
        return reversed_substrings






def main():
    try:
        n = input("Enter registration number n (a positive integer):\n")
        s = input("Enter Text (only alphabets):\n")
        
        n = int(n)
        
        # Check for valid inputs.
        validate_input(n, s)
        
        processed_str = process_string(n, s)
        print("Processed string:", processed_str)

        k = count_set_bits(n)
        print("Substring length k: ", k)
        
        if k > len(processed_str):
            print("No substrings can be extracted because k is greater than the length of the string.")

        else:
            substrings = extract_substrings(processed_str, k)
            substrings = sort_or_reverse(n, s, substrings)
            print("Substrings:", substrings)
    
    except ValueError as ve:
        print("Error:", ve)


if __name__ == "__main__":
    main()


