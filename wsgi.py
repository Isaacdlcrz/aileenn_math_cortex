"""Application entry point."""
from math_cortex import create_app
from flask import jsonify
# from dotenv import load_dotenv

# try:
#     load_dotenv()
# except Exception as e:
#     print("No .env file")

application = create_app()

@application.route("/")
def root():
    return "A.I.L.E.E.N.N. Math Cortex"

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)