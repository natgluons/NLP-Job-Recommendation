from transformers import pipeline

# Load pre-trained NLP models
topic_model = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
ner_model = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')
sentiment_model = pipeline('sentiment-analysis')

def analyze_text(job_description, candidate_profile):
    topics = topic_model(job_description, candidate_profile)
    entities = ner_model(candidate_profile)
    sentiment = sentiment_model(job_description)
    return topics, entities, sentiment
