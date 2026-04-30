''' 
    Emotion detection application powerd by flask 
'''

# Import the emotion detection function from the package created:
from flask import Flask, render_template, request
from emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotions Detector")

@app. route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotional analysis over it using emotion detection)
        function. The output returned shows the label and its
        confidence score for the provided text.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print('----response----', response)
    
    emotions = response[0]   # first dict
    label_info = response[1] # second dict

    return (
        "For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

@app. route("/")
def render_index_page():
    '''
        Calling index page as landing
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run (debug=True, host="0.0.0.0", port=5000)

