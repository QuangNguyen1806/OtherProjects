# This can check whether if what the user sends is a haiku or not.

def count_syllables(word):

    return len([ph for ph in word.split(',') if ph])

def is_haiku(input_string):

    lines = input_string.strip().split('/')
    
    # Check if there are exactly 3 lines
    if len(lines) != 3:
        print("WARNING: The haiku must contain exactly 3 lines.")
        return False
    
    # Check syllable count for each line
    syllable_counts = [5, 7, 5]
    for i, line in enumerate(lines):
        syllables = [count_syllables(word) for word in line.split()]
        if sum(syllables) != syllable_counts[i]:
            print(f"WARNING: The {ordinal(i + 1)} line is not {syllable_counts[i]} syllables long.")
            return False
    
    # If all conditions are met, it is a haiku
    return True

def ordinal(n):

    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def haiku_string_parser(input_string):

    if is_haiku(input_string):
        lines = input_string.strip().split('/')
        formatted_haiku = '\n'.join([' '.join([word.split(',')[0] for word in line.split()]) for line in lines])
        return formatted_haiku
    else:
        return ""

def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    
    if formatted_haiku:
        print(formatted_haiku)
    else:
        print("Input is not a valid haiku.")

if __name__ == "__main__":
    main()

