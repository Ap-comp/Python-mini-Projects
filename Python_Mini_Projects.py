
#  Prime number checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
print("Prime?" , is_prime(num))


#  Simple calculator
def add(x, y):
    return float(x) + float(y)

def subtract(x, y):
    return float(x) - float(y)

x = input("Enter first number: ")
y = input("Enter second number: ")
op = input("Enter operator (+ or -): ")

if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", subtract(x, y))
else:
    print("Invalid operator")



#  Count vowels in a string
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))



#  Palindrome checker
def is_palindrome(text):
    return text == text[::-1]

word = input("Enter a word to check for palindrome: ")
print("Is palindrome?", is_palindrome(word))



#  Find most frequent character
def most_frequent(text):
    freq = {}
    for char in text:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

text = input("Enter text: ")
print("Most frequent character:", most_frequent(text))



#  Compress string (character counts)
def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

string = input("Enter string to compress: ")
print("Compressed:", compress_string(string))
