from flask import Flask, request, render_template, redirect, url_for, flash
import os
import subprocess

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'cc'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'  # for flash messaging

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'walk.cc'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            score, output = grade_submission(filepath)
            return render_template('result.html', score=score, output=output)
        else:
            flash('Allowed file types are .cc')
            return redirect(request.url)
    return render_template('upload.html')

def grade_submission(filepath):
    try:
        compile_command = "/usr/bin/g++ " + filepath
        retcode = subprocess.run(compile_command, shell=True, check=True)
        test_script_command = "./test.sh"
        result = subprocess.run(test_script_command, shell=True, capture_output=True, text=True)
        score = result.returncode
        with open(filepath, 'r') as fs:
            original_code = fs.read()
        output = result.stdout + "\nScore: " + str(score) + " out of 2 correct.\n"
        output += "*************Original submission*************\n" + original_code
        return score, output
    except subprocess.CalledProcessError as e:
        return 'Compilation failed', e.output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
