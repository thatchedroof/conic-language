#%%
# Definitions

import random

conemes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
phonemes = ['p', 't', 'k', 'b', 'd', 'g', 'n', 'm', 'l', 's']
vowel_pairs = ['aa', 'ei', 'ii', 'oo', 'uu', 'ai', 'oi', 'ou', 'ia', 'oa',]

def random_conon() -> str:

    def random_conic_string(inp: str, length: int) -> str:

        # Base case
        if length <= 0:
            return inp

        # If inp is empty, pick random initial coneme
        elif inp == '':
            return random_conic_string(random.choice(conemes), length-1)

        # Pick random coneme, not identical to previous coneme
        else:
            return random_conic_string(inp + random.choice(
                list(
                    filter(lambda x: x != inp[-1], conemes))
                ), length-1)

    # Return conon of 3 conemes
    return random_conic_string('', 3)

def conon_to_word(conon) -> str:

    coneme_to_phoneme = dict(zip(conemes, phonemes))

    coneme_to_vowel_pair = dict(zip(conemes, vowel_pairs))

    consonant_1 = coneme_to_phoneme[conon[0]]

    consonant_2 = coneme_to_phoneme[conon[1]]

    vowel_pair = coneme_to_vowel_pair[conon[2]]

    vowel_1 = vowel_pair[0]

    vowel_2 = vowel_pair[1]

    return consonant_1 + vowel_1 + consonant_2 + vowel_2

def word_to_conon(word) -> str:

    phoneme_to_coneme = dict(zip(phonemes, conemes))

    vowel_pair_to_coneme = dict(zip(vowel_pairs, conemes))

    coneme_1 = phoneme_to_coneme[word[0]]

    coneme_2 = phoneme_to_coneme[word[2]]

    coneme_3 = vowel_pair_to_coneme[word[1] + word[3]]

    assert coneme_1 != coneme_2

    assert coneme_2 != coneme_3

    return coneme_1 + coneme_2 + coneme_3

def sentence_to_conon(sentence):
    return list(map(word_to_conon, sentence.split(' ')))

#%%
# Running

if __name__ == '__main__':
    for i in range(10):
        print(conon_to_word(random_conon()))

# %%
