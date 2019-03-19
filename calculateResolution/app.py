from flask import Flask, request, render_template
import matplotlib.image as mpimg
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('index.html')

@app.route('/uploader', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        Image = mpimg.imread(f.filename)
        return(str(Image.shape[1]) + "x" + str(Image.shape[0]))
