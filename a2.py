def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    Pre-condition: dna consists of characters 'A', 'T', 'C', 'G'

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    return dna1 > dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleo = 0

    for char in dna:
        if char == nucleotide:
            num_nucleo = num_nucleo + 1

    return num_nucleo

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs
    in the DNA sequence dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if dna1.find(dna2) >= 0:
        return True
    else:
        return False

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (a valid
    DNA sequence only contains characters 'A', 'T', 'C', and 'G'.

    >>> is_valid_sequence('GTCACAT')
    True
    >>> is_valid_sequence('atag')
    False
    >>> is_valid_sequence('TgAgc')
    False
    >>> is_valid_sequence('GATGCCT2')
    False
    """

    non_nucleo_ltrs = 0

    for char in dna:
        if char not in 'ACTG':
            non_nucleo_ltrs += 1

    if non_nucleo_ltrs > 0:
        return False
    else:
        return True
    
def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second
    DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCGG', 'TCTCACC', 4)
    'ATCGGTCTCACC'
    """

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the complement nucleotide of nucleotide ('A', 'T', 'C', or 'G').

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """

    if nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'A':
        return 'T'
    else:
        return 'A'

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence complementary to DNA sequence dna.

    >>> get_complementary_sequence('CGGA')
    'GCCT'
    >>> get_complementary_sequence('TAG')
    'ATC'
    """

    complement = ''

    for char in dna:
        if char == 'C':
            complement = complement + 'G'
        elif char == 'G':
            complement = complement + 'C'
        elif char == 'A':
            complement = complement + 'T'
        else:
            complement = complement + 'A'

    return complement
            
            
        
