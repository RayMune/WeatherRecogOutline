from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    # You can process the uploaded image here, for example:
    # Save the file to disk, use a machine learning model to analyze it, etc.
    # For simplicity, let's just print out the filename here
    print(f'Uploaded file: {file.filename}')
    
    # You can also call an external API to get climate change data for the user's area
    # For demonstration, let's just use a placeholder response
    climate_data = {'temperature': '25°C', 'humidity': '60%', 'sea_level': '1 meter'}
    
    return render_template('result.html', filename=file.filename, climate_data=climate_data)

if __name__ == '__main__':
    app.run(debug=True)
