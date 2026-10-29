current plan:
the user must guess a word that follows the given properties

for example:
our forecast detects hootchbootch
find words that are extremely rainy but not very serious


1. Generate a secret target word
2. Calculate the target vector
3. Display this vector to the user in weather terms
4. Let the user guess. On guess, do the following:
    1. Record the word
    2. Get vector of word
    3. Compare vector to target vector
        1. If within a certain threshold, win
        2. Else, show the user their word and similarity score and keep it visible somehow