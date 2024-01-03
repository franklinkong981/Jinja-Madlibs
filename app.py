from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story1, story2, story3

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug  = DebugToolbarExtension(app)

current_stories = {"story1": story1, "story2": story2, "story3": story3}

@app.route('/')
def generate_story_dropdown():
    return render_template("main.html", story_list = list(current_stories.keys()))

@app.route('/story-form')
def generate_story_form():
    chosen_story_text = request.args["chosen_story"]
    chosen_story = current_stories.get(chosen_story_text)
    story_number = chosen_story_text[-1]
    return render_template("story_form.html", story=chosen_story_text, story_number=story_number, placeholders_list=chosen_story.placeholders)

@app.route('/story-result/<story>')
def generate_story_result(story):
    placeholders_and_values = request.args
    story_text = current_stories.get(story).generate(placeholders_and_values)
    return render_template("story_result.html", completed_story=story_text)


