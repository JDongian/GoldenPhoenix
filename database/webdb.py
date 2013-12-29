from flask import Flask, jsonify
from dbtools import get_cursor, fetch_image_db, count_db
app = Flask(__name__)
c = get_cursor()

#@app.route('/<category>')
#def count(category, number):
#    return jsonify({'total': count_db(c, category)})

@app.route('/<category>/<int:number>')
def image(category, number):
    r = list(fetch_image_db(c, category, number)[0])+[0]*4
    print r
    return jsonify({'results': { 'category': r[0],
                                 'color': r[1],
                                 'phototype': r[2],
                                 'filename': r[3],
                                 'thumbname': r[4],
                                 'loc': r[5],
                                 'description': r[6],
                                 'price': r[7] },
                    'total': count_db(c, category)[0][0]})

if __name__ == '__main__':
    app.run(debug=True)
