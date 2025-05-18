from src.main.server.server_settings import app

if __name__ == "__main__":
    app.run(debug= True, host= "0.0.0.0", port=3000)