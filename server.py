from flask import Flask, request
import requests
import tempfile
import subprocess

from shutil import copyfile

from flask import Flask
app = Flask(__name__)

@app.route("/api/num_colors")
def num_colors():
    result = "Please include URL to image!"
    if request.args.get('src') is not None:
        url = request.args.get('src')
        r = requests.get(url, stream=True)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        for chunk in r.iter_content(chunk_size=1024):
            temp_file.write(chunk)
        call = subprocess.Popen('identify -format %[kurtosis] ' + temp_file.name, shell=True, stdout=subprocess.PIPE)
        result = call.stdout.read()
        temp_file.close()
    return result

if __name__ == "__main__":
    app.run()
