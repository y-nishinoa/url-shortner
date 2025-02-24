from flask import Flask, request, redirect, jsonify, render_template
import random
import string

app = Flask(__name__)

# 短縮URLを保存する辞書
url_mapping = {}

# 短縮URLを生成する関数
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    
    return jsonify({'short_url': request.host_url + short_code})

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
