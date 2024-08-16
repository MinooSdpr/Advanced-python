import random

def get_random_emoji():
    emoji_ranges = [
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F300, 0x1F5FF),  # Miscellaneous Symbols and Pictographs
        (0x1F680, 0x1F6FF),  # Transport and Map Symbols
        (0x1F700, 0x1F77F),  # Alchemical Symbols
        (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF),  # Supplemental Arrows-C
        (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
        (0x1FA00, 0x1FA6F),  # Chess Symbols
        (0x1FA70, 0x1FAFF)   # Symbols and Pictographs Extended-A
    ]


    start, end = random.choice(emoji_ranges)

    code_point = random.randint(start, end)
    
    # Convert the code point to a Unicode character
    return chr(code_point)


random_emoji = get_random_emoji()
print("Random Emoji:", random_emoji)
