MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """

    # Open the input file and read its contents
    with open(input_file, 'r') as f:
        text = f.read()

    #--------------------------------------------------------------------------------------
    # Convert the text to Morse code -method 1
    # morse_code = ''
    # for char in text:
    #     if char.upper() in MORSE_CODE:
    #         morse_code += MORSE_CODE[char.upper()] 
    #     elif char == ' ':
    #         morse_code += '\n'  # Use '/' to represent space between words
    #     else:
    #         morse_code += char  # Keep non-alphabetic characters unchanged
    #--------------------------------------------------------------------------------------
    # Convert the text to Morse code using string methods - method 2

    # morse_code = "\n".join(
    #     " ".join(MORSE_CODE[char.upper()] for char in word if char.upper() in MORSE_CODE)
    #     for word in text.split()
    # )
    #--------------------------------------------------------------------------------------
    # Convert the text to Morse code using string methods - method 3

    # Create a translation table for str.translate
    translation_table = str.maketrans(
        {char: MORSE_CODE[char] for char in MORSE_CODE}
    )

    # Translate the text to Morse code using the translation table
    
    morse_code = "\n".join(
        "\n".join(word.translate(translation_table) for word in line.split())
        for line in text.upper().splitlines()
    )

    # Write the Morse code to the output file
    with open(output_file, 'w') as f:
        f.write(morse_code)

english_to_morse()

