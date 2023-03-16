# pip install spacy 
# python -m spacy download en_core_web_sm

import pandas as pd
import spacy
from collections import Counter

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Function to encode the company description
def encode_description(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def most_common_descriptions(df, description_col="short_description", target_col="target", target_value=1, n=10):
    # Apply the encoding function to the "description" column
    df["encoded_description"] = df[description_col].apply(encode_description)

    # Filter the DataFrame to include rows with "target" equal to target_value
    target_df = df[df[target_col] == target_value]

    # Count the occurrences of encoded descriptions
    description_counts = Counter(target_df["encoded_description"])

    # Get the most common encoded descriptions
    top_descriptions = description_counts.most_common(n)
    
    return top_descriptions
