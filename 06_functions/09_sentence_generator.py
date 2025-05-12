def make_sentence(word: str, part_of_speech: int) -> None:
    """Generate and print a sentence based on the word and its part of speech.
    
    Args:
        word: The word to insert into the sentence
        part_of_speech: 0 (noun), 1 (verb), or 2 (adjective)
    """
    templates = [
        "I am excited to add this {} to my vast collection of them!",  # noun
        "It's so nice outside today it makes me want to {}!",          # verb
        "Looking out my window, the sky is big and {}!"               # adjective
    ]
    
    if 0 <= part_of_speech < len(templates):
        print(templates[part_of_speech].format(word))
    else:
        print("Error: Part of speech must be 0 (noun), 1 (verb), or 2 (adjective)")

def main() -> None:
    """Main function to get user input and generate sentences."""
    try:
        word = input("Please type a noun, verb, or adjective: ").strip()
        print("Is this a noun, verb, or adjective?")
        part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Error: Please enter a valid number (0, 1, or 2) for part of speech")

if __name__ == '__main__':
    main()