from flask import Flask, request, redirect
import json
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

@app.route('/add-profile', methods=['POST'])
def addProfile():
	from tumblelog.models import Post
	post = Post(
		name = request.form['Name'],
		age = request.form['Age'],
		school = request.form['School'],
        location = request.form['Location'],
        hack_ideas = request.form['Hack-ideas'],
		experience = request.form['Experience'],
		contact_info = request.form['Contact-info']
	)
	post.save()
	# posts = Post.objects.all()
	# return render_template('base.html', posts=posts)
	# return json.dumps({'status':'OK'})
	return redirect("/")

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)
