from flask import Flask
app = Flask(__name__)

@app.route('/<name>')               #app.add_url_rule(‘/’, ‘hello’, hello_world)
def hello_world(name):
   return 'Hello boy %s ❤😘' % name

if __name__ == '__main__':
   app.run(debug=True)
   
   
'''
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID
'''   