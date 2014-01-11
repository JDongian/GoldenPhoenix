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
                                 'gender': r[1],
                                 'color': r[2],
                                 'phototype': r[3],
                                 'filename': r[4],
                                 'thumbname': r[5],
                                 'loc': r[6],
                                 'description': r[7],
                                 'price': r[8] },
                    'total': count_db(c, category)[0][0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)
