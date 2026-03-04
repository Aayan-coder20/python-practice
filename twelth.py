print("--- Extracting Words from Text File ---")

n = int(input("\nEnter Length of Words: "))

f = open("story.txt", "r")
text = f.read()
f.close()

words = text.lower().split()
unique = []

for w in words:
    if len(w) == n and w not in unique:
        unique.append(w)

unique.sort()

print("\nWords with length", n, "are:", unique)
