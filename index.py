from setup import create_app
# from livereload import Server

app = create_app()

if __name__ == '__main__':
  # server.serve(port=8000, host='0.0.0.0')
  app.run(port=8000, host='0.0.0.0')
