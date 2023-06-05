from flask import Flask
from chat_gpt.chat_gpt_controller import chat_gpt_route_path, chat_gpt_route
from dotenv import load_dotenv

load_dotenv()

# Create the Flask application
app = Flask(__name__)

# Register modules/blueprints
app.register_blueprint(chat_gpt_route, url_prefix=f'/{chat_gpt_route_path}')

def bootstrap():
    # Start the Flask application
    app.run(port=3000, debug=True)

if __name__ == '__main__':
    bootstrap()

