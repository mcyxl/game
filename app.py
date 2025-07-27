from flask import Flask, render_template, redirect
import random
import os

app = Flask(__name__)

def get_random_joke():
    # 获取文件路径
    file_path = os.path.join(app.static_folder, 'hhh.txt')
    
    # 读取所有笑话
    with open(file_path, 'r', encoding='utf-8') as f:
        jokes = [line.strip() for line in f if line.strip()]
    
    # 随机选择一个笑话
    return random.choice(jokes) if jokes else "今天没有笑话，这本身就是个笑话！"

@app.route('/')
def a():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    joke = get_random_joke()
    return render_template('hello.html', joke=joke)

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():  
    return render_template('contact.html')

@app.route('/guess_number')
def guess_number():
    return render_template('guess_number.html')

@app.route('/memory_cards')
def memory_cards():
    return render_template('memory_cards.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/tic_chess')
def tic_chess():
    return render_template('tic_chess.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
