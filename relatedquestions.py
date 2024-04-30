from rake_nltk import Rake
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def generate_questions(summary):
    """
    Generate related questions based on the summarized text.
    
    Parameters:
        summary (str): The summarized text.
    
    Returns:
        list: A list of related questions.
    """
    r = Rake()
    r.extract_keywords_from_text(summary)
    keywords = r.get_ranked_phrases()[:5]  # Extract top 5 keywords
    
    questions = []
    for keyword in keywords:
        questions.append(f"What is {keyword}?")
        questions.append(f"Can you explain {keyword}?")
        questions.append(f"What are the implications of {keyword}?")
        # You can add more question templates as needed
        
    return questions

# Example usage:
summary = """
         What is RPA"""
questions = generate_questions(summary)
print("Related Questions:")
for question in questions:
    print(question)
