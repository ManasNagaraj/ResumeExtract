import pandas as pd
import spacy

# load pre-trained model
nlp = spacy.load('en_core_web_sm')
# noun_chunks = nlp.noun_chunks

def exSkills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("../skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    noun_chunks = nlp(resume_text)
    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)


    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]
