""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = '៕។៛ៗ៚៙៘,.? '
_kh_letters = 'កខគឃងចឆជឈញដឋឌឍណតថទធនបផពភមយរលវឝឞសហឡអឣឤឥឦឧឨឩឪឫឬឭឮឯឰឱឲឳ'
_kh_vowel = '឴឵ាិីឹឺុូួើឿៀេែៃោៅ\u17c6\u17c7\u17c8'
_kh_sub = '្'
_kh_sub_2 = '៎'
_letters_ipa = "acefhigjklmnoprstuwzĕŋŏŭɑɓɔɗəɛɡɨɲʋʔʰː"


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_kh_letters) +list(_kh_vowel)+list(_kh_sub)+list(_kh_sub_2) + list(_letters_ipa)

# print(f'Total symbols: {len(symbols)}')
# print(f'Unique symbols: {len(set(symbols))}')
# assert len(symbols) == len(set(symbols)), "Duplicate symbols detected!"

# Special symbol ids
SPACE_ID = symbols.index(" ")

