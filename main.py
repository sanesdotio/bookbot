def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characters_list = count_characters(file_contents)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"The file contains {word_count} words.")
        for characters in characters_list:
            print(f"The character '{characters['character']}' appears {characters['count']} times.")
        print("--- End report of books/frankenstein.txt ---")
        
def count_words(text):
    words = text.split()
    
    return len(words)

def sort_on(dict):
    return dict["count"]

def count_characters(text):
    characters = text.lower()
    characters_list = []
    character_counts = {}
    
    for character in characters:
        if character in character_counts:
            character_counts[character] += 1
        elif character.isalpha():
            character_counts[character] = 1
            
    for character, count in character_counts.items():
        characters_list.append({"character": character, "count": count})
    
    characters_list.sort(reverse=True, key=sort_on)
    
    return characters_list
    
        
main()