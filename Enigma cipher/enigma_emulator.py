class EnigmaEmulator:
    def __init__(self, rotor_order, plugboard_sequence, ring_settings, starting_positions, text, decrypt=False):
        self.rotor_order = rotor_order
        self.plgb_sequence = plugboard_sequence
        self.rg_settings = ring_settings
        self.start_pos = starting_positions
        self.text = text
        self.decrypt = decrypt
        self._num_of_rotors = len(rotor_order)
        self._alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._nulls = {
            'SHT': r'(', 'SHR': r')', 'SHM': r'{', 'SHN': r'}',
            'SHL': r'[', 'STR': r']', 'STM': r'"', 'STN': r"'",
            'STL': r'\', 'SRM': r'/', 'SRN': r'|', 'SRL': r'~',
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
            r'\': 'STL', r'/': 'SRM', r'|': 'SRN', r'~': 'SRL',
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
            'I': {
                'wiring': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                'position': 0,
                'turnover_notch': 17,
                'ring_setting': 0
            },
            'II': {
                'wiring': "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                'position': 0,
                'turnover_notch': 5,
                'ring_setting': 0
            }
            'III': {
                'wiring': "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                'position': 0,
                'turnover_notch': 22,
                'ring_setting': 0
            },
            'IV': {
                'wiring': "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                'position': 0,
                'turnover_notch': 10,
                'ring_setting': 0
            },
            'V': {
                'wiring': "VZBRGITYUPSDNHLXAWMJQOFECK",
                'position': 0,
                'turnover_notch': 0,
                'ring_setting': 0
            }
        }
        self._reflectors = {
            'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        }
        self._lampboard = "" # This is basically an output variable.
        self._sequence_marker = [v for k, v in self.nulls.items()]
        
        #Applying settings
        self._apply_settings()
        if not self.decrypt:
            self._refine_text()
     
    def _plugboard(self, letter):
        return self._plugboard_cipher[letter]
     
    def _apply_settings(self):
        for swap in self.plgb_sequence:
            fst_letter = swap[0]
            lst_letter = swap[1]
            self._plugboard_cipher[fst_letter] = lst_letter
            self._plugboard_cipher[lst_letter] = fst_letter
        for i in range(self._num_of_rotors):
            self._rotor_pack[self.rotor_order[i]]['position'] = self.start_pos[i]
            self._rotor_pack[self.rotor_order[i]]['ring_setting'] = self.rg_settings[i]
     
    def _rotors(self, letter, reflected=False):
        letter_index = self._alphabets.index(letter)
        _range = range(self._num_of_rotors-1, -1, -1) if not reflected else range(self._num_of_rotors)
        for i in _range:
            rotor = self._rotor_pack[self.rotor_order[i]]
            input_index = (letter_index + rotor['position'] - rotor['ring_setting']) % 26
            rotor_output_letter = rotor['wiring'][input_index]
            output_offset = abs(input_index - self._alphabets.index(rotor_output_letter))
            letter_index = (letter_index + output_offset) % 26
        if reflected:
            return letter_index
        return self._alphabets[letter_index]
     
    def _reflector(self, letter_index):
        reflected_letter = self._reflectors['B'][letter_index]
        return reflected_letter
     
    def _refine_text(self):
        refined_text = ""
        replacement_dict = self._reversed__nulls
        for char in self.text:
            if char.isalpha():
                refined_text += char
            else:
                replacement = replacement_dict.get(char, char)
                refined_text += replacement
        self.text = refined_text
     
    def _turnover(self):
        step = True
        for i in range(self._num_of_rotors):
            rotor = self._rotor_pack[self.rotor_order[i]]
            if step:
                rotor['position'] += 1
                step = False
            if rotor['position'] == rotor['turnover_notch']:
                step = True
            else: break
     
    def _keyboard(self):
        j = 0
        for char in self.text:
            plgb1 = self._plugboard(char)
            rtl_rotors = self._rotors(plgb1)
            reflctd_letter = self._reflector(rtl_rotors)
            ltr_rotors = self._rotors(reflctd_letter, reflected=True)
            self._turnover()
            plgb2 = self._plugboard(ltr_rotors)
            if j == 4:
                self._lampboard += ' '
            self._lampboard += plgb2
            j = (j + 1) % 4
     
    def _decrypt(self):
        output = ""
        current_sequence = ""
        replacement_dict = self.nulls
        in_sequence = False
        for char in self._lampboard:
            if char.isalpha():
                if not in_sequence and char in self._sequence_marker:
                    current_sequence += char
                    in_sequence = True
                elif in_sequence:
                    current_sequence += char
                    if len(current_sequence) == 3:
                        output += replacement_dict.get(current_sequence, current_sequence)
                        current_sequence = ""
                        in_sequence = False
                else:
                    output += char
        return output
     
    def run():
        self._keyboard()
        if self.decrypt:
            print(self._decrypt())
        else:
            print(self._lampboard)


if __name__ == '__main__':
    print("""
    Python Enigma Emulator, #Terminal Community model.
    -> Usage:
    Input;
    Rotor order: 15 23 14 or OWN
    Plugboard sequence: EU RT FI GH JK LM NQ PD OA WV BZ SY XC
    Ring settings: 2 17 9 or BQI
    Starting positions: 6 4 2 or FDB
    Text: +Some normal text or -Some encrypted text
    
    Output:
    DECRPYTED OUTPUT IN ALL CAPS
    ENCR YPTE DHRL OUTP UTHR LINH RLAL LHRL CAPS
    
    Notes:
    The sequence 'HRL' is a null sequence for the space ' ' character.
    These nulls are usually encrypted in the encrypted output, So it's
    likely you won't be seeing the in output, as that sequence would
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
    invalid_input = True
    while invalid_input:
        if rtr_ord = []: inp1 = input()
        if plgb_sq = []: inp2 = input()
        if rng_stg = []: inp3 = input()
        if str_pos = []: inp4 = input()
        if inp_txt = "": inp5 = input()
        
        if inp1.isalpha() and t:
            t1 = 
    EnigmaEmulator().run()