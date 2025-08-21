import spacy

# Load the installed model
nlp = spacy.load("en_core_web_sm")

doc = nlp("Barack Obama was the president of the USA.")

# Print named entities
print([ent.text for ent in doc.ents])
