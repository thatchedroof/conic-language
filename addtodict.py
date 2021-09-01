#%%

import pandas as pd
import secrets

conemes = ['N','A','B','C','D','E','F','G','H','I','J']

coneme_to_rep = {
    'N': "''",
    'A': "∧∧",
    'B': "V∧",
    'C': "∧V",
    'D': "VV",
    'E': "∧'",
    'F': "V'",
    'G': "'∧",
    'H': "'V",
    'I': "OO",
    'J': "XX"
}

columns = ['english','synonyms']
#print('\n'.join([coneme_to_rep[x] for x in 'FDEN']))

def ask_for_entry():
    english = input('Please give an english word')
    synonyms = input('Please give any synonyms')
    conic = secrets.choice(conemes) + secrets.choice(conemes) + secrets.choice(conemes) + secrets.choice(conemes)
    while conic in list(cdict.index) or any([x + x in conic for x in conemes]):
        conic = secrets.choice(conemes) + secrets.choice(conemes) + secrets.choice(conemes) + secrets.choice(conemes)
    return pd.DataFrame([[english, synonyms]], columns=columns, index=[conic])

if __name__ == '__main__':
    again = True
    while again == True:
        cdict = pd.read_csv('conicdictionary.csv',
                        index_col='conic')
        new_entry = ask_for_entry()
        new_cdict = cdict.append(new_entry)
        new_cdict.index.name = 'conic'
        new_cdict.to_csv('conicdictionary.csv')
        again = True if input('Again?') in {'', 'yes', 'Yes', 'y', 'Y'} else False

# %%

# %%
