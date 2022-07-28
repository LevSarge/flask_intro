"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'stinky', 'ugly', 'cringe', 'dumb', 'A CLOWN', 'THE ENTIRE CIRCUS']
@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Tell us about yourself!</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person"><br>
          What compliment would you like? <select name="compliment">
            <option>awesome</option>
            <option>terrific</option>
            <option>neato</option>
            <option>fantabulous</option>
            <option>wowza</option>
            <option>brilliant</option>
            <option>coolio</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss" method='GET'>
          Or would you like to be roasted instead? <input type="text" name="roastee"><br>
          How would you like to be insulted? <select name="roast">
            <option>stinky</option>
            <option>ugly</option>
            <option>cringe</option>
            <option>dumb</option>
            <option>A CLOWN</option>
            <option>THE ENTIRE CIRCUS</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Diss the user. No, really."""
  roastee = request.args.get("roastee")
  roast =request.args.get("roast")

  return f"""
  <!doctype html>
  <html>
    <head>
      <title>A Roast</title>
    </head>
    <body>
      Hello {roastee}. I think you're {roast}.
    </body>
  </html>
"""

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
