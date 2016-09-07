from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

@app.route('/<password>')
def index (password):

    #hash_value = generate_password_hash(password,method='sha256')
    hash_value = generate_password_hash(password)
    stored_password= 'pbkdf2:sha1:1000$YmCTyg30$d2cdbf8c5520ab3bd66a8b7d54c1990e66a2703e'

    result= check_password_hash(stored_password, password)

    return str(result)

if __name__=='__main__':
    app.run(debug=True)