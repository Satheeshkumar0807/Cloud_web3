from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for displaying the uploaded files table
@app.route('/file_list')
def file_list():
    # Logic to fetch uploaded files from AWS S3 and pass them to the template
    uploaded_files = []  # Replace this with actual logic to fetch uploaded files
    return render_template('file_list.html', uploaded_files=uploaded_files)

if __name__ == '__main__':
    app.run(debug=True)
