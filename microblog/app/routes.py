from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

# chapter 1
# def index():
#     return "Hello, World!"


# chapter 2
def index():

# 1.

    #the user variable is define a temporary mock user
    # user = {"username": "Gim Sheng"}
#     return (
#         """
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, """
#         + user["username"]
#         + """!</h1>
#     </body>
# </html>"""
#     )

# 2. Templetes
# # above are messy code, so we use the template engine to simplify the code
#     user = {"username": "Sheng"}
# # render_template is a function that renders a template and returns the result
# # In short, this command tells Flask to:
# # 1. Take the 'index.html' template file.
# # 2. Inject the 'title' and 'user' Python variables into it.
# # 3. Return the final, complete HTML result to the browser.
#     return render_template('index.html', title='Home', user=user)


# 3. Loops
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
