from urllib.request import urlopen
from flask import Flask, request
from wand.image import Image
import tempfile
import subprocess

app = Flask(__name__)

@app.route("/api/num_colors")
def num_colors():
    result = "Please include URL to image!"
    if request.args.get('src') is not None:
        url = request.args.get('src')
        r = urlopen(url)
        temp_file = tempfile.NamedTemporaryFile()
        Image(file=r).save(filename=temp_file.name)
        call = subprocess.Popen('identify -format %k ' + temp_file.name, shell=True, stdout=subprocess.PIPE)
        result = call.stdout.read()
        temp_file.close()
    return result

if __name__ == "__main__":
    app.run()
