text = input("введіть унікальні символи: ")
unique_symbols = set(text)
print(unique_symbols)
count = len(unique_symbols)
if count > 10:
    print(True)
else:
    print(False)