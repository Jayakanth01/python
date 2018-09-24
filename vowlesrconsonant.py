ch = input("Input a letter of the alphabet: ")

if ch in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif ch == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l)
