import pronouncing
#'AH': "əˈ",#'ʌ',
def phonet_def(word):
# word = "translation"
    phonetic_transcriptions = pronouncing.phones_for_word(word)
    if phonetic_transcriptions:
        phonetic_dict = {
        'AA': 'ɑ',
        'AA0': 'ɑ',
        'AA1': 'ɑː',
        'AE': 'æ',
        'AE0': 'æ',
        'AE1': 'æː',
        'AH': 'ə',
        'AH0': 'ə',
        'AH1': 'ʌː',
        'AO': 'ɔ',
        'AO0': 'ɔ',
        'AO1': 'ɔː',
        'AW': 'aʊ',
        'AW0': 'aʊ',
        'AW1': 'aʊː',
        'AY': 'aɪ',
        'AY0': 'aɪ',
        'AY1': 'aɪː',
        'B': 'b',
        'CH': 'tʃ',
        'D': 'd',
        'DH': 'ð',
        'EH': 'ɛ',
        'EH0': 'ɛ',
        'EH1': 'ɛː',
        'ER': 'ɝ',
        'ER0': 'ɝ',
        'ER1': 'ɝː',
        'EY': 'eɪ',
        'EY0': 'eɪ',
        'EY1': 'eɪː',
        'F': 'f',
        'G': 'ɡ',
        'HH': 'h',
        'IH': 'ɪ',
        'IH0': 'ɪ',
        'IH1': 'ɪː',
        'IY': 'i',
        'IY0': 'i',
        'IY1': 'iː',
        'JH': 'dʒ',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'NG': 'ŋ',
        'OW': 'oʊ',
        'OW0': 'oʊ',
        'OW1': 'oʊː',
        'OY': 'ɔɪ',
        'OY0': 'ɔɪ',
        'OY1': 'ɔɪː',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'SH': 'ʃ',
        'T': 't',
        'TH': 'θ',
        'UH': 'ʊ',
        'UH0': 'ʊ',
        'UH1': 'ʊː',
        'UW': 'u',
        'UW0': 'u',
        'UW1': 'uː',
        'V': 'v',
        'W': 'w',
        'Y': 'j',
        'Z': 'z',
        'ZH': 'ʒ',
        'ˈ': 'ˈ',
        'ˌ': 'ˌ',
        'ː': 'ː',
        ' ': ' '
    }
        # print(f"Phonetic transcriptions for '{word}':")
        for transcription in phonetic_transcriptions:
            text=""
            for i in transcription.split(" "):
                # if "0" in i or "1" in i:
                #     i=i.replace("0","")
                #     i=i.replace("1","")
                text+=phonetic_dict[i]
            print("teeext",text)
            return text
    else:
        print(f"No phonetic transcriptions found for '{word}'.")


from eng_to_ipa import ipa_list

def get_ipa(word):
    ipa = ipa_list(word)
    return ipa[-1] if ipa else "IPA not found for the given word."

# word = "hello"
# ipa = get_ipa(word)
# print(f"The IPA transcription of '{word}' is: {ipa}")
