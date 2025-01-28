from flask import Flask

class ToolRunner:
    def __init__(self, Tool, **kargs):
      self.tool = Tool(**kargs)
      self.app = Flask(__name__)
      self.setupRoutes()

    def run(self):
      self.app.run(debug=False, port=3000, host='0.0.0.0')

    def setupRoutes(self):
      @self.app.route('/functions', methods=['GET'])
      def functions():
          functions_list = []
          for param in dir(self.tool):
            if param.startswith('__'):
              continue
            if callable(getattr(self.tool, param)):
              functions_list.append(param)
          return {
              'functions': functions_list
            }

      @self.app.route('/trigger', methods=['POST'])
      def trigger():
          return 'Hello, World!'