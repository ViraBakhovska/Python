from PIL import Image, ImageFilter
from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename

app = Flask(__name__)

def convert_file(fileName):
    try:
        img = Image.open(fileName).convert('L') #img.convert('L')
        if img.size[0] < img.size[1]:
            img = img.rotate(90, expand=1)
        img.save(fileName)
    except OSError as e:
        print("Помилка при відкритті файлу \"{0}\": {1}".format(fileName, e.strerror))
    except:
        print("Неочікувана помилка \"{0}\"".format(fileName))

@app.route('/')

def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])

def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        fn = secure_filename(f.filename)
        f.save(fn)
        convert_file(fn);
        return send_file(fn)

if __name__ == '__main__':
    app.run(debug=True)