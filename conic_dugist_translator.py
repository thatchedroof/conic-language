#%%
# Definitions

import pandas as pd
import re
import random

conemes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
onsets = ['p', 'b', 't', 'd', 'k', 'g', 'n', 'ng', 'm', 'f', 'v', 's', 'z', 'sh', 'zh', 'ch', 'r', 'l', 'j', 'w']
vowels = ['a', 'e', 'i', 'o', 'u']#'a2','e2','i2','o2','u2'
codas  = ['', 'n', 'ng', 'm', 'f', 'v', 's', 'sh', 'ch', 'l']

coneme_to_index = dict(zip(conemes, range(10)))

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

def conon_to_word(conon: str) -> str:

    initial = conon[0]

    medial = conon[1]

    try:
        final = conon[2]

    except:
        final = ''

    if initial == medial:
        print('INIT == MEDI ERROR:', initial + medial + final)

    if medial == final:
        print('MEDI == FINA ERROR:', initial + medial + final)

    if len(conon) == 2:
        if initial == 'A' and medial == 'A':
            return 'na'

        if initial == 'B' and medial == 'B':
            return 'ku'

        if initial == 'C' and medial == 'C':
            return 'li'

        if initial == 'D' and medial == 'D':
            return 'so'

        else:
            print('INVALID 2-CONON ERROR:', initial + medial)

    coda = codas[coneme_to_index[final]]

    vowel = vowels[coneme_to_index[medial] % 5]

    if coneme_to_index[medial] < 5:
        onset = onsets[coneme_to_index[initial]]

    else:
        onset = onsets[coneme_to_index[initial] + 10]

    return onset + vowel + coda


def word_to_conon(word: str) -> str:

    onset, vowel, coda = re.split('([aeiou])', word)

    final = conemes[codas.index(coda)]

    initial = conemes[onsets.index(onset) % 10]

    if onsets.index(onset) < 10:
        medial = conemes[vowels.index(vowel)]

    else:
        medial = conemes[vowels.index(vowel) + 5]

    if initial == medial:
        print('INIT == MEDI ERROR:', initial + medial + final)

    if medial == final:
        print('MEDI == FINA ERROR:', initial + medial + final)

    return initial + medial + final

def check_all_conons():
    errors = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if conemes[i] == conemes[j]:
                    continue
                if conemes[j] == conemes[k]:
                    continue
                original = conemes[i] + conemes[j] + conemes[k]
                translated = word_to_conon(conon_to_word(original))
                if original != translated:
                    errors.append([original, translated])
    return errors

"""
def sentence_to_conon(sentence):
    return list(map(word_to_conon, sentence.split(' ')))
"""
#%%
# Running

if __name__ == '__main__':

    # sentence = ''

    # for i in range(100):
    #     sentence += conon_to_word(random_conon()) + ' '

    # print(sentence)
    cdict = pd.read_csv('conicdictionary.csv',
                        index_col='conic')


    def process_row(cdict, index, row):
        #print(index)
        return pd.Series({
            'dugist': conon_to_word(index),
            'english': row[1],
            'synonyms': row[2]
        }, name=index)

    new_cdict = pd.DataFrame()

    for index, row in cdict.iterrows():
        new_cdict = new_cdict.append(process_row(new_cdict, index, row))

    new_cdict = new_cdict.sort_index()

    print(new_cdict)

    new_cdict.to_csv('conicdictionary.csv')

# %%
