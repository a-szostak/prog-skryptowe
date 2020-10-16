
lancuch1 = """Napisy są z reguły jednowierszowe.
Jeśli jednak masz taką potrzebę,
to możesz tworzyć napisy wielowierszowe.
"""

lancuch2 = """Napisy, jak wspomniałem na początku,
to łańcuchy znaków o określonej kolejności.
Python może używać indeksów do wywołania poszczególnych znaków.
"""

print((lancuch1 + lancuch2)*3)

lancuch = "Dowolny tekst, może tu być cokolwiek, a jest takie coś"

print(lancuch[0])
print(lancuch[0:2])
print(lancuch[2:])
print(lancuch[-2])
print(lancuch[-3:])
print(lancuch[0::2])

lancuch[2] = "3"   #wniosek: nie da się, napisy są niemodyfikowalne
print(lancuch)
