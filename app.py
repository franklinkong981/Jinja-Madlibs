from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story1

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug  = DebugToolbarExtension(app)

@app.route('/story1-form')
def generate_story1_form():
    return render_template("story1_form.html", placeholders_list=story1.placeholders)

@app.route('/story1-result')
def generate_story1_result():
    placeholders_and_values = request.args
    story_text = story1.generate(placeholders_and_values)
    return render_template("story1_result.html", completed_story=story_text)


