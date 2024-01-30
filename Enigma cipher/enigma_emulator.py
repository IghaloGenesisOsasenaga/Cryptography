class EnigmaEmulator:
    def __init__(self, rotor_order, plugboard_sequence, ring_settings, starting_positions, text, decrypt):
        self.rotor_order = rotor_order
        self.plgb_sequence = plugboard_sequence
        self.rg_settings = ring_settings
        self.start_pos = starting_positions
        self.text = text
        self.decrypt = decrypt
        self._alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.text_cluster = len_of_cluster # This tells the _keyboard function when to a space the lampboard during encryption
        self._num_of_rotors = len(rotor_order)
        self._nulls = {
            'SHT': r'(', 'SHR': r')', 'SHM': r'{', 'SHN': r'}',
            'SHL': r'[', 'STR': r']', 'STM': r'"', 'STN': r"'",
            'STL': '\\', 'SRM': r'/', 'SRN': r'|', 'SRL': r'~',
            'SMN': r'^', 'SML': r'+', 'SNL': r'-', 'HTR': r'=',
            'HTM': r'>', 'HTN': r'<', 'HTL': r'$', 'HRM': r'&',
            'HRN': r'@', 'HRL': r' ', 'HMN': r'%', 'HML': r'?',
            'HNL': r'!', 'TRM': r'_', 'TRN': r'#', 'TRL': r':',
            'TMN': r';', 'TML': r'*', 'TNL': r',', 'RMN': r'.',
            'RML': r'`'
        }
        self._reversed__nulls = {
            r'(': 'SHT', r')': 'SHR', r'{': 'SHM', r'}': 'SHN',
            r'[': 'SHL', r']': 'STR', r'"': 'STM', r"'": 'STN',
            '\\': 'STL', r'/': 'SRM', r'|': 'SRN', r'~': 'SRL',
            r'^': 'SMN', r'+': 'SML', r'-': 'SNL', r'=': 'HTR',
            r'>': 'HTM', r'<': 'HTN', r'$': 'HTL', r'&': 'HRM',
            r'@': 'HRN', r' ': 'HRL', r'%': 'HMN', r'?': 'HML',
            r'!': 'HNL', r'_': 'TRM', r'#': 'TRN', r':': 'TRL',
            r';': 'TMN', r'*': 'TML', r',': 'TNL', r'.': 'RMN',
            r'`': 'RML'
        }
        self._plugboard_cipher = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
            'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
            'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
            'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
            'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
            'Z': 'Z'
        }
        self._rotor_pack = {
            # More rotor models can be added
            'I': {
                'wiring': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                'offset_wiring': "",
                'position': 0,
                'turnover_notch': 17,
                'ring_setting': 0
            },
            'II': {
                'wiring': "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                'offset_wiring': "",
                'position': 0,
                'turnover_notch': 5,
                'ring_setting': 0
            },
            'III': {
                'wiring': "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                'offset_wiring': "",
                'position': 0,
                'turnover_notch': 22,
                'ring_setting': 0
            },
            'IV': {
                'wiring': "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                'offset_wiring': "",
                'position': 0,
                'turnover_notch': 10,
                'ring_setting': 0
            },
            'V': {
                'wiring': "VZBRGITYUPSDNHLXAWMJQOFECK",
                'offset_wiring': "",
                'position': 0,
                'turnover_notch': 0,
                'ring_setting': 0
            }
        }
        self._reflectors = {
            # More reflector models can be added
            'B': {
                'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q',
                'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X',
                'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M',
                'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z',
                'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A',
                'Z': 'T'
            }
        }
        self._lampboard = "" # This is basically an output variable.
        self._sequence_marker = {k[0] for k, v in self._nulls.items()}
        
        # Applying settings
        self._apply_settings()
        if not self.decrypt:
            # Replace special characters in text with their corresponding null sequence
            self._refine_text()
            print(self.text, self._sequence_marker)
        else:
            # Join encrypted texts that might be separated with a spaces
            self._join_text()
     
    def _apply_settings(self):
        for swap in self.plgb_sequence:
            fst_letter = swap[0]
            lst_letter = swap[1]
            self._plugboard_cipher[fst_letter] = lst_letter
            self._plugboard_cipher[lst_letter] = fst_letter
        for i in range(self._num_of_rotors):
            rotor = self._rotor_pack[self.rotor_order[i]]
            # Set the properties of rotors in use
            rotor['position'] = self.start_pos[i]
            rotor['ring_setting'] = self.rg_settings[i]
            # Ofset wiring is the resulting wiring after applying ring setting
            cut = rotor['ring_setting']
            rotor['offset_wiring'] = rotor['wiring'][cut:] + rotor['wiring'][:cut]
    
    def _decrypt(self):
        output = ""
        # Variable to store suspected sequences
        current_sequence = ""
        # Replacement dictionary for special characters
        replacement_dict = self._nulls
        # Boolean to know if the current_sequence variable is not empty
        in_sequence = False
        for char in self._lampboard:
            if not in_sequence and char in self._sequence_marker:
                # Start a sequence
                current_sequence += char
                in_sequence = True
            elif in_sequence:
                # Add a character to the current sequence if it's length is less than 3
                current_sequence += char
                if len(current_sequence) == 3:
                    # Current sequence has reached max length, so add the corresponding special character to the output if current_sequence is found in the dictionary else add all the letters in current sequence to the output
                    output += replacement_dict.get(current_sequence, current_sequence)
                    # Important reset
                    current_sequence = ""
                    in_sequence = False
            else:
                # Add character to output as character doesn't begin a null sequence and current_sequence is empty 
                output += char
        return output
     
    def _refine_text(self):
        # Output
        refined_text = ""
        # Replacement dictionary for special characters
        replacement_dict = self._reversed__nulls
        for char in self.text:
            # Add the character to the Output variable if it's an alphabet else add it's appropriate null sequence
            if char.isalpha():
                refined_text += char
            else:
                replacement = replacement_dict.get(char, char)
                refined_text += replacement
        self.text = refined_text
     
    def _join_text(self):
        output = ""
        for c in self.text:
            # Adding only non-space characters to the output
            output += c if c != ' ' else ''
        self.text = output
     
    def _rotors(self, letter, reflected=False):
        """
        Explanation of how my rotor works
          Rf        Rt1       Rt2    Rt3        Ent
        Y <-> A | E -> X |  A -> P |  B -> H | <- A <- in
        G <-> B | K -> Y |  D -> Q |  D -> I | <- B
        I <-> C | M -> Z |  F -> R |  Y -> J | <- C
        H <-> D | F -> A |  J -> S |  K -> K | <- D -> out
        F <-> E | J -> B |  U -> T |  M -> L | <- E
        E <-> F | I -> C |  D -> U |  L -> M | <- F
        B <-> G | H -> D |  G -> V |  C -> N | <- G
        D <-> H | T -> E |  H -> W |  A -> O | <- H
        .......   ......    ......    ......   ....
        Where Rf = Reflector; Rt = Rotor; Ent = Entry
        After the ring setting and the current position has been applied to all rotors,
        the rotors function receives an entry letter. That letter enters the first rotor
        and that rotor checks which letter has been substituted for it in the original
        wiring of the rotor. Then the signal leaves through that letter on the other side
        of the rotor. Then that signal becomes the entry for the next rotor and the whole
        process repeats it self for the other rotors till it gets to the reflector.
        
        If the rotors function is given a reflected signal, it does something similar
        excepts that it does the reverse i.e it takes the left side of the rotors as the
        entry point to the rotor, then it checks which letter that entry substitutes for
        in the original English alphabet. After that, it exits the signal through that
        point on the right side of the rotor till the signal gets back to the entry point.
        """
        entry_index = self._alphabets.index(letter)
        _range = range(self._num_of_rotors-1, -1, -1) if not reflected else range(self._num_of_rotors)
        for i in _range:
            rotor = self._rotor_pack[self.rotor_order[i]]
            input_pin = (entry_index + rotor['position']) % 26
            if reflected:
                input_letter = rotor['offset_wiring'][input_pin]
                output_contact = (rotor['wiring'].index(input_letter) - rotor['position']) % 26
            else:
                output_letter = rotor['wiring'][input_pin]
                output_contact = (rotor['offset_wiring'].index(output_letter) - rotor['position']) % 26
            entry_index = output_contact
        
        return self._alphabets[entry_index]
     
    def _reflector(self, letter):
        # 'B' selects the choice of reflector and returns the reflected letter
        reflected_letter = self._reflectors['B'][letter]
        return reflected_letter
     
    def _turnover(self):
        for i in range(self._num_of_rotors-1, 0, -1):
            current_rotor = self._rotor_pack[self.rotor_order[i]]
            previous_rotor = self._rotor_pack[self.rotor_order[i-1]]
      
            # Move the rightmost rotor by one unit at each keypress
            if i == self._num_of_rotors-1:
                current_rotor['position'] = (current_rotor['position'] + 1) % 26
                current_rotor['offset_wiring'] = current_rotor['offset_wiring'][1:] + current_rotor['offset_wiring'][:1]
            
            # Check if the current rotor's turnover notch is reached
            if current_rotor['position'] == current_rotor['turnover_notch']:
                # Move the previous rotor if the notch is reached
                previous_rotor['position'] = (previous_rotor['position'] + 1) % 26
                previous_rotor['offset_wiring'] = previous_rotor['offset_wiring'][1:] + previous_rotor['offset_wiring'][:1]
            else:
                # If the notch is not reached, break the loop
                break
     
    def _plugboard(self, letter):
        return self._plugboard_cipher[letter]
     
    def _keyboard(self):
        # Spacing variables
        j = 0
        cluster_length = self.text_cluster
        
        for char in self.text:
            # Step 1 letter to Plugboard
            plgb1 = self._plugboard(char)
            # Step 2 from Plugboard to rotors through the entry wheel 
            rtl_rotors = self._rotors(plgb1)
            # Step 3 from leftmost rotor to reflector
            reflctd_letter = self._reflector(rtl_rotors)
            # Step 4 from reflectors back to entry wheel through rotors
            ltr_rotors = self._rotors(reflctd_letter, reflected=True)
            # Adjust the positions of the rotors
            self._turnover()
            # Step 5 back to the Plugboard
            plgb2 = self._plugboard(ltr_rotors)
            # Step 6 from Plugboard to lampboard
            self._lampboard += plgb2
            
            # Adding a space after every n characters defined by self.text_cluster
            if (j % cluster_length == cluster_length-1) and not self.decrypt:
                self._lampboard += ' '
            j = (j + 1) % cluster_length
     
    def run(self):
        # Encrypting the text letter by letter
        self._keyboard()
        output = self._lampboard
        
        # Modify output to replace nulls with the corresponding special character
        if self.decrypt:
            output = self._decrypt()
        print(output)
        return output


# Customizable Variables
num_of_rotors = 3
len_of_cluster = 5
valid_roman_numerals = {'I', 'II', 'III', 'IV', 'V'}


def validate_sequence_of_three(inp):
    output = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if inp.isalpha() and inp.isupper() and len(inp) == num_of_rotors:
        # This runs when inp is in the form of 'BQI' consisting of only letters
        for char in inp:
            output.append(alphabets.index(char))
    else:
        # This runs when inp is in the form of '2 17 9' consisting of only digits
        for digits in inp.split():
            num = int(digits)-1
            if digits.isdigit() and num <= 26:
                # number must consists of numbers and be less than or equal to 26
                output.append(num)
            else:
                output = []
                break
    
    return output


def validate_rotor_order(inp):
    output = inp.split()
    # Set to store distinct roman numerals
    distinct_rtr = set()
    if len(output) == 3:
        for i in range(3):
            rom_num = output[i]
            # Check if roman numeral is a registered one and it has only occured once
            if rom_num not in valid_roman_numerals or rom_num in distinct_rtr:
                output = []; break
            # Add current roman numeral to set
            distinct_rtr.add(rom_num)
    else:
        output = []
    
    return output


def validate_plugboard(inp):
    # Set to store distinct characters in sequence
    distinct_char = set()
    output = []
    swp = ""
    for swap in inp.split():
        # Make a swap doesn't contain more than two letters and number of swaps are less than 13
        if len(swap) > 2 or len(output) > 13:
            output = []
            break
        for char in swap:
            if char in distinct_char or not char.isalpha():
                # A character appears more than once or it's not an alphabet
                output = []; break
            
            swp += char
            if len(swp) == 2:
                output.append(swp)
                swp = ""
            distinct_char.add(char)
    
    return output


def validate_text(inp):
    output = inp[1:]
    decrypt = False
    length = len(output)
    if inp[0] not in ('+', '-'):
        return ""
    if inp[0] == '-':
        # Pattern for encrypted messages
        cut = count  = 0
        for char in output:
            count += 1
            # Check for complete clusters at beginning and middle of string
            if cut == len_of_cluster and char == ' ' and count != length:
                cut = -1; valid = True
            # Check for complete and incomplete clusters at end of string
            elif cut != len_of_cluster and char != ' ' and count == length:
                valid = True
            # Anything else is considered invalid
            else:
                valid = False
            cut += 1
        decrypt = True
        if not valid:
            output = ""
    
    return (output.upper(), decrypt)


if __name__ == '__main__':
    print("""
    Python Enigma Emulator, #Terminal Community model.
    -> Usage:
    Input;
    Rotor order: I V III
    Plugboard sequence: EU RT FI GH JK LM NQ PD OA WV BZ SY XC
    Ring settings: 2 17 9 or BQI
    Starting positions: 6 4 2 or FDB
    Text: +Some normal text or -Some encrypted text
    
    Output:
    DECRPYTED OUTPUT IN ALL CAPS
    ENCR YPTE DHRL OUTP UTHR LINH RLAL LHRL CAPS
    
    -> Notes:
    Rotor order must be three in length.
    The sequence 'HRL' is a null sequence for the space ' ' character.
    These nulls are usually encrypted in the encrypted output, So it's
    likely you won't be seeing them in the output, as the sequence would
    have been encrypted. And in decrypted messages, you won't see them
    either as they would have be translated to their special character.
    In summary, Encrypted output contains encrypted letters in groups
    of four and decrypted messages contains letters and special
    characters in word groups.
    """)
    
    rtr_ord = []
    plgb_sq = []
    rng_stg = []
    str_pos = []
    inp_txt = ""
    decrypt = False
    
    # Proceed booleans to specify breakpoints in collecting inputs
    p1 = p2 = p3 = p4 = p5 = False
    """
    The P1 variable means that the rotor order has been collected,
    meaning it allows to proceed to collect the next input, which
    is the plug box sequence. P2 variable signifies that plugboard
    sequence has been collected, and it allows to collect the next
    input, which is ring setting. Then P3 signifies that ring setting
    has been collected, and it allows to collect the next input,
    which is starting position. Now, P4 means starting position has
    been collected, and it allows to collect the next input, which
    is input text. Now, P5 signifies that input text has been
    collected, and it allows to proceed to the next action.
    """
    while True:
        # Input validation logic
        
        err_message = ""
        if rtr_ord == []:
            # rtr_ord is empty
            inp1 = input("Rotor order: ")
            rtr_ord = validate_rotor_order(inp1)
            p1 = True if rtr_ord else False
        
        if plgb_sq == [] and p1:
            # plgb_sq is empty and previous input/inputs has been collected
            inp2 = input("Plugboard sequence: ")
            plgb_sq = validate_plugboard(inp2)
            p2 = True if plgb_sq else False
        # previous input does not allow to proceed
        elif not p1: err_message = "Invalid rotor order"
        
        if rng_stg == [] and p2:
            # rng_stg is empty and previous input/inputs has been collected
            inp3 = input("Ring settings: ")
            rng_stg = validate_sequence_of_three(inp3)
            p3 = True if rng_stg else False
        # previous input does not allow to proceed
        elif not p2 and p1: err_message = "Invalid plugboard sequence"
        
        if str_pos == [] and p3:
            # str_pos is empty and previous input/inputs has been collected
            inp4 = input("Starting positions: ")
            str_pos = validate_sequence_of_three(inp4)
            p4 = True if str_pos else False
        # previous input does not allow to proceed
        elif not p3 and p2 and p1: err_message = "Invalid ring settings"
        
        if inp_txt == "" and p4:
            # inp_txt is empty and previous input/inputs has been collected
            inp5 = input("Text: ")
            inp_txt, decrypt = validate_text(inp5)
            p5 = True if inp_txt else False
        # previous input does not allow to proceed
        elif not p4 and p3 and p2 and p1: err_message = "Invalid starting positions"
        
        # All input allow to proceed
        if p1 and p2 and p3 and p4 and p5: break
        # All input allow to proceed but inp_txt doesn't
        elif not p5 and p1 and p2 and p3 and p4: err_message = "Invalid text"
        
        print(err_message)
    
    sample = EnigmaEmulator(rtr_ord, plgb_sq, rng_stg, str_pos, inp_txt, decrypt).run()