import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Render! Your Python app is successfully running.</h1>"

if __name__ == '__main__':
    # Render assigns a dynamic port via environment variables
    port = int(os.environ.get("PORT", 5000))
    # It must listen on 0.0.0.0 to be accessible externally
    app.run(host='0.0.0.0', port=port)