from flask import Flask

class Application:
    def __init__(self) -> None:
        self.app = Flask(__name__)
    
    def setup(self) -> None:
        @self.app.route('/')
        def youaregay():
            return 'You are a gay'

    def run(self) -> None:
        self.app.run()
    