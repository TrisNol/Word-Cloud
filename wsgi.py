# TODO Deployment via Docker instead of this weird Heroku specific way with the procfile and such

from Backend.app import app

if __name__ == "__main__":
    app.run()
