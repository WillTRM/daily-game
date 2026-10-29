import random
import statistics
import math

features = ["magnitude", "seriousness", "wetness", "duration", "loudness"]

def vec(**kwargs):
    return [kwargs.get(name, 0.0) for name in features]

PHONEME_VECTORS = {
    # vowels
    "ɪ": vec(magnitude=-1.0),
    "i": vec(magnitude=-0.8),
    "ɛ": vec(magnitude=-0.3),
    "æ": vec(magnitude=0.2),
    "ɑ": vec(magnitude=0.7),
    "aʊ": vec(magnitude=0.9, loudness=0.6),
    "u": vec(magnitude=0.8, seriousness=0.5),
    "oʊ": vec(magnitude=0.6, seriousness=0.6),
    "ʌ": vec(magnitude=0.3),
    # consonants
    "l": vec(wetness=0.8),
    "r": vec(wetness=0.5, loudness=-0.2),
    "ʃ": vec(wetness=0.4, loudness=-0.3),
    "k": vec(loudness=0.8, duration=0.5),
    "t": vec(loudness=0.5, duration=0.7),
    "p": vec(loudness=0.6, magnitude=-0.3),
    "m": vec(seriousness=0.7, loudness=-0.5),
    "n": vec(seriousness=0.5, loudness=-0.4),
}

def phoneme_score(phoneme, goal_features, mask = [1.0] * 5):
    v = PHONEME_VECTORS.get(phoneme, [0.0] * 5) # 5 is number of features
    score = -sum(m * (x - p) ** 2 for p, x, m, in zip(v, goal_features, mask))
    return score

def word_score(word, goal_features, mask):
    print(sum(phoneme_score(char, goal_features, mask) for char in word) / len(word))
    return sum(phoneme_score(char, goal_features, mask) for char in word) / len(word)

def generate_daily_goal():
    return [random.random() * 2 - 1 for x in range(5)]

# vector representation of an IPA word, calculated by averaging the phoneme vectors
# slightly cursed one liner but it works
# ai wouldn't dare do this lmao
def word_vector(word):
    avg = [statistics.mean(k) for k in zip(*[PHONEME_VECTORS.get(phoneme, [0.0] * 5) for phoneme in word])]
    return avg

# dot product
# apparently the @ operator doesn't work on standard lists
def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

# cosine similarity
def similarity(v1: list, v2: list):
    v1_len = math.sqrt(sum(n ** 2 for n in v1))
    v2_len = math.sqrt(sum(n ** 2 for n in v2))
    num = dot(v1, v2)
    den = v1_len * v2_len
    return num / den

g = generate_daily_goal()
# print(g)
# m = [1, 0, 1, 1, 0]
# print(phoneme_score("ɪ", g, m))
# print(phoneme_score("ɑ", g, m))
print(word_vector("ik"))
print(similarity([1.0, 0.5], [0.9, 0.4]))
print(similarity([1.0, 0.5], [0.5, 0.25]))
