# Job Recommendation System Using NLP Techniques

This repository contains a Flask-based API for a job recommendation system that leverages NLP models from Hugging Face's transformers library. The system is designed to improve job matching by understanding the context and semantics of job descriptions and candidate profiles instead of just using the keywords.

More on this concept: https://natashagluons.medium.com/building-a-job-recommendation-system-using-nlp-techniques-bart-and-ner-models-149d607a9934 

## Features

- **NLP Models Used:**
  - BART for topic modeling.
  - Named Entity Recognition (NER) using BERT.
  - Sentiment Analysis using a pre-trained sentiment model.

- **API:**
  - `/recommend` endpoint accepts job descriptions and candidate profiles, performs NLP analysis, and returns the best job match for each candidate.

- **Docker:**
  - Containerization for consistent deployment.

- **Kubernetes:**
  - Deployment using Kubernetes for scalability.

## Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/natgluons/job_recommendation_system.git
   cd job_recommendation_system

## Usage

curl -X POST http://localhost:5000/recommend -H "Content-Type: application/json" -d '{
    "job_descriptions": [
        {"id": 1, "description": "Software development and programming skills."}
    ],
    "candidate_profiles": [
        {"id": 1, "profile": "Experienced in coding, software engineering."}
    ]
}'
