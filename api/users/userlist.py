from app import app

@app.route("user/user_list")
def user_list():
    return {"Name: Alex", "Name: rohit"}