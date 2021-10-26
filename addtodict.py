#%%

import pandas as pd
import secrets

coneme_to_rep = {
    '1': "∧∧",
    '2': "V∧",
    '3': "∧V",
    '4': "VV",
    '5': "∧'",
    '6': "V'",
    '7': "'∧",
    '8': "'V",
    '9': "<>",
    '0': "><"
}

conemes = list(coneme_to_rep.keys())

columns = ['english','synonyms']
#print('\n'.join([coneme_to_rep[x] for x in 'FDEN']))

def ask_for_entry():
    english = input('Please give an english word')
    synonyms = input('Please give any synonyms')
    conic = secrets.choice(conemes[1:]) + secrets.choice(conemes) + secrets.choice(conemes)
    while conic in list(cdict.index):
        conic = secrets.choice(conemes[1:]) + secrets.choice(conemes) + secrets.choice(conemes)
    return pd.DataFrame([[english, synonyms]], columns=columns, index=[conic])

if __name__ == '__main__':
    again = True
    while again == True:
        cdict = pd.read_csv('conicToEnglish.csv',
                        index_col='conic')
        new_entry = ask_for_entry()
        new_cdict = cdict.append(new_entry)
        new_cdict.index.name = 'conic'
        new_cdict.to_csv('conicToEnglish.csv')
        again = True if input('Again?') in {'', 'yes', 'Yes', 'y', 'Y'} else False

# %%

# %%
