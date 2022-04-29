def convert(value):
    try:
         return int(value)
    except ValueError:
        return None

print(convert('a'))