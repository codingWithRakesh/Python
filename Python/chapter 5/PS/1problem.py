words = {
    "billi" : "cat",
    "kutta" : "dog",
    "gadha" : "donkey",
    "gai" : "cow",
    "ghora" : "horse",
    "billi ka bachcha" : "kitten",
    "kutte ka bachcha" : "puppy",
    "gadha ka bachcha" : "foal",
    "madat" : "help",
    "dost" : "friend",
    "pyaar" : "love",
    "khushi" : "happiness",
    "dard" : "pain", 
}

word = input("Enter a word in Hindi: ").strip().lower()


print(words.get(word, "Word not found in the dictionary."))