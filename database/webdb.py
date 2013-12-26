from flask import Flask, jsonify
from dbtools import get_cursor, fetch_image_db, count_db
app = Flask(__name__)
c = get_cursor()

#@app.route('/<category>')
#def count(category, number):
#    return jsonify({'total': count_db(c, category)})

@app.route('/<category>/<int:number>')
def image(category, number):
    result = list(fetch_image_db(c, category, number)[0])+[0]*4
    return jsonify({'results': {'name': result[0],
                                'dir': result[1],
                                'description': result[2],
                                'price': result[3]},
                    'total': count_db(c, category)})

if __name__ == '__main__':
    app.run(debug=True)
