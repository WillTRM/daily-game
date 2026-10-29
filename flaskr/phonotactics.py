import random
import re

onset_consonants = [" ", "b", "d", "dʒ", "ð", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ʃ", "t", "ch", "θ", "v", "w", "z", "ʒ"]
coda_consonants = [" ", "b", "d", "dge", "ð", "f", "g", "j", "k", "l", "m", "n", "ŋ", "p", "r", "s", "ʃ", "t", "tch", "θ", "v", "w", "z", "ʒ"]
vowels = ["ɑ", "ɒ", "æ", "aɪ", "aʊ", "ɛ", "eɪ", "ɪ", "i", "oʊ", "ɔ", "ɔɪ", "ʊ", "u", "ʌ"]

# generates random IPA for a word, loosely following english phonotactic constraints
# IPA is not fully accurate to simplify things like ch at start and tch at end
def generate(seed: int) -> list:
    random.seed(seed)
    word = []
    last_char = ""
    for idx in range(random.randint(1, 3)):
        char1 = random.choice([x for x in onset_consonants if x != last_char])
        char2 = random.choice(vowels)
        char3 = random.choice(coda_consonants)
        last_char = char3
        syllable = [char1, char2, char3]
        word = word + syllable
    word = [s for s in word if s != " "]
    return word

# poorly converts list of IPA characters to a word
def to_latin(ipa: list) -> str:
    word = ""
    for char in ipa:
        match char:
            case "dʒ":
                word = word + "j" # or dge, we'll need to sort that out
            case "ð":
                word = word + "th"
            case "j":
                word = word + "y"
            case "ŋ":
                word = word + "ng"
            case "ʃ":
                word = word + "sh" # or che?
            case "tʃ":
                word = word + "tch" # or ch
            case "θ":
                word = word + "th"
            case "ʒ":
                word = word + "s" # or g, no clue about this one
            case "ɑ":
                word = word + "a"
            case "ɒ":
                word = word + "o"
            case "æ":
                word = word + "a"
            case "aɪ":
                word = word + "i"
            case "aʊ":
                word = word + "ow" # or ou
            case "ɛ":
                word = word + "e"
            case "eɪ":
                word = word + "a"
            case "ɪ":
                word = word + "i"
            case "i":
                word = word + "ee"
            case "oʊ":
                word = word + "oa" # or o, i think
            case "ɔ":
                word = word + "au"
            case "ɔɪ":
                word = word + "oi"
            case "ʊ":
                word = word + "oo" # oo in foot, this is a bad one
            case "u":
                word = word + "oo" # same oo or u as above
            case "ʌ":
                word = word + "u"
            case _:
                word = word + char
    return word