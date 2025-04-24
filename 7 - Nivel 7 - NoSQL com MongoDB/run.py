from src.main.server.server import app
from src.models.connections.connection_handler import db_connection_handler


if __name__ == "__main__":
    db_connection_handler.connection_to_db()
    app.run(debug=True, host="0.0.0.0", port=3000)