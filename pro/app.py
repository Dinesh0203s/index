from flask import Flask, request, render_template, send_from_directory
import os
from photo_filter import find_person_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    selfie = request.files['selfie']
    group_photos = request.files.getlist('group_photos')
    output_folder = 'static/output_photos/'

    # Save the uploaded selfie
    selfie_path = os.path.join('static', 'selfie.jpg')
    selfie.save(selfie_path)

    # Create or clear the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        for file in os.listdir(output_folder):
            os.remove(os.path.join(output_folder, file))

    # Save and process group photos
    group_photos_folder = 'static/group_photos'
    if not os.path.exists(group_photos_folder):
        os.makedirs(group_photos_folder)
    for photo in group_photos:
        photo_path = os.path.join(group_photos_folder, photo.filename)
        photo.save(photo_path)

    find_person_image(selfie_path, group_photos_folder, output_folder)

    return render_template('results.html', photos=os.listdir(output_folder))

@app.route('/static/<filename>')
def serve_image(filename):
    return send_from_directory('static/output_photos', filename)

if __name__ == '__main__':
    app.run(debug=True)
