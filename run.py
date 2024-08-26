""" Flask APP Setup"""

from app.config import DevConfig
from app import create_app

config = DevConfig()

app = create_app(config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
