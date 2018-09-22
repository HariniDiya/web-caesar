from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method="post">
        <label for="Rotate">Rotate by:</label>
        <input id="Rotate" type="text" name="rot" value=0 />
        <label>
            <textarea name="text">{0}</textarea>
        </label>
        <input type="submit" />
        
    </form>
      
    </body>

</html>

"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])

def enc():
    rotate = request.form['rot']
    text = request.form['text']
    return form.format(encrypt(text,rotate))

""" def add_movie():
    new_movie = request.form['new-movie']
    movies.append(new_movie)
    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content """


app.run()