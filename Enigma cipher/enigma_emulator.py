class EnigmaEmulator:
    def __init__(self, rotor_order=[], plugboard_sequence=[], ring_setting=[], starting_positions=[]):
        self.rotor_order = rotor_order
        self.num_of_rotors = len(rotor_order)
        self.plgb_sequence = plugboard_sequence
        self.rg_setting = ring_setting
        self.start_pos = starting_positions
        self.alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.nulls = {
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
        self.plugboard_cipher = {
            'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',
            'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',
            'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',
            'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',
            'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
            'Z': 'Z'
        }
        self.rotor_pack = {
            'I': {
                'wiring': "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                'position': 0,
                'turnover_notch': "",
                'ring_setting': 0
            }
            'II': {
                'wiring': "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                'position': 0,
                'turnover_notch': "",
                'ring_setting': 0
            }
            'III': {
                'wiring': "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                'position': 0,
                'turnover_notch': "",
                'ring_setting': 0
            }
            'IV': {
                'wiring': "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                'position': 0,
                'turnover_notch': "",
                'ring_setting': 0
            }
            'V': {
                'wiring': "VZBRGITYUPSDNHLXAWMJQOFECK",
                'position': 0,
                'turnover_notch': "",
                'ring_setting': 0
            }
        }
        self.reflectors = {
            'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        }
     
    def plugboard(self, letter):
        return self.plugboard_cipher[letter]
     
    def apply_settings(self):
        for swap in self.plgb_sequence:
            fst_letter = swap[0]
            lst_letter = swap[1]
            self.plugboard_cipher[fst_letter] = lst_letter
            self.plugboard_cipher[lst_letter] = fst_letter
        for i in range(self.num_of_rotors):
            rotor_wiring = self.rotor_pack[self.rotor_order[i]]['wiring']
            cut = self.rg_setting[i]
            rotor_wiring = rotor_wiring[cut:] + rotor_wiring[:cut]
            self.rotor_pack[self.rotor_order[i]]['wiring'] = rotor_wiring
        
    
    def rotors(self, letter):
        entry_letter = letter
        for i in range(len(self.rotor_order)-1, -1, -1):
            rotor = self.rotor_order
            