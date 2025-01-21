from app import app

@app.route("/user/signup")
def user():
    return "Welcome signup page"