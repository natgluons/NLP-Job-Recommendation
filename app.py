from flask import Flask, request, jsonify
from nlp_model import analyze_text

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    job_descriptions = data['job_descriptions']
    candidate_profiles = data['candidate_profiles']

    recommendations = []

    for candidate in candidate_profiles:
        candidate_recommendations = []
        candidate_profile = candidate['profile']
        
        for job in job_descriptions:
            job_description = job['description']
            topics, entities, sentiment = analyze_text(job_description, candidate_profile)
            score = sum([item['score'] for item in topics['scores']]) + len(entities) + sentiment[0]['score']
            
            candidate_recommendations.append({
                'job_id': job['id'],
                'score': score,
                'topics': topics,
                'entities': entities,
                'sentiment': sentiment
            })
        
        best_job = max(candidate_recommendations, key=lambda x: x['score'])
        recommendations.append({
            'candidate_id': candidate['id'],
            'best_job': best_job
        })

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
