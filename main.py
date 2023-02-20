import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.snake import initGamers
#from model.scores import initCool
#from model.facts import initFactDay

# setup APIs
from api.snake import snake_api # Blueprint import api definition
#from api.score import score_api # Blueprint import api definition
#from api.fact import fact_api

# register URIs
app.register_blueprint(snake_api) # register app pages
#app.register_blueprint(score_api)
#app.register_blueprint(fact_api)


@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')  
def index():
    return render_template("index.html")

@app.route('/snakes')  
def snakes():
    return render_template("snakes.html")

@app.route('/snake_game/')
def render_static():
    return render_template('snake_game.html')

@app.route('/snake_game/snake_apk/')
def render_static_snakeapk():
    return render_template('snake.apk')

@app.before_first_request
def activate_job():
    initGamers()
 #   initCool()
 #   initFactDay()
 #   initBreakingNews()


# this runs the application on the development server
if __name__ == "__main__":
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snake.db'
    app.run(debug=True, host="0.0.0.0", port="8086")
#    initNFLTeams()
