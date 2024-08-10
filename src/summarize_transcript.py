import json
from summarizer import Summarizer

def summarize(json_input: str):
    # Load the JSON data from the string
    data = json.loads(json_input)
    
    # Create and configure the summarization model
    model = Summarizer()
    ideal_summary_length = 130

    topics = []

    # Process each transcript entry
    for entry in data['transcript']:
        transcript_text = entry['text']
        transcript_length = len(transcript_text.split())
        ratio = ideal_summary_length / transcript_length if transcript_length > ideal_summary_length else 1.0
        
        if transcript_length < ideal_summary_length:
            print("Transcript segment is too short to summarize to the desired length. Returning original transcript.")
            summary = transcript_text
        else:
            # Generate summary
            result = model(transcript_text, ratio=ratio)
            summary = ''.join(result)

        # Extract or create a 5-word topic from the summary
        topic_words = summary.split()[:5]
        topic = ' '.join(topic_words)

        # Append the summarized data to topics
        topics.append({
            "topic": topic,
            "start_time": entry['start_time'],
            "end_time": entry['end_time'],
            "summary": summary
        })
    
    # Create the output JSON structure
    output_json = {
        "lecture_title": data['lecture_title'],
        "topics": topics
    }

    return json.dumps(output_json, indent=2)
