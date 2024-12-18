from transformers import pipeline

class HealthRecommender:
    def __init__(self):
        self.recommendation_pipeline = pipeline('text-generation', model='gpt-3')

    def generate_recommendation(self, symptoms_description):
        result = self.recommendation_pipeline(symptoms_description, max_length=150, num_return_sequences=1)
        return result[0]['generated_text']
