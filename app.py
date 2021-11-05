from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.Constellation


# HTML 화면 보여주기
@app.route('/')
def show_main():
    return render_template('index.html')

@app.route('/fortune')
def show_con():
    return render_template('index2.html')

@app.route('/constellation_Aquarius')
def constellation_Aquarius():
    return render_template('/Constellation/constellation_Aquarius.html')

@app.route('/constellation_Pisces')
def constellation_Pisces():
    return render_template('/Constellation/constellation_Pisces.html')

@app.route('/constellation_Aries')
def constellation_Aries():
    return render_template('/Constellation/constellation_Aries.html')

@app.route('/constellation_Taurus')
def constellation_Taurus():
    return render_template('/Constellation/constellation_Taurus.html')

@app.route('/constellation_Gemini')
def constellation_Gemini():
    return render_template('/Constellation/constellation_Gemini.html')

@app.route('/constellation_Leo')
def constellation_Leo():
    return render_template('/Constellation/constellation_Leo.html')

@app.route('/constellation_Cancer')
def constellation_Cancer():
    return render_template('/Constellation/constellation_Cancer.html')

@app.route('/constellation_Virgo')
def constellation_Virgo():
    return render_template('/Constellation/constellation_Virgo.html')

@app.route('/constellation_Libra')
def constellation_Libra():
    return render_template('/Constellation/constellation_Libra.html')

@app.route('/constellation_Scorpio')
def constellation_Scorpio():
    return render_template('/Constellation/constellation_Scorpio.html')

@app.route('/constellation_Sagittarius')
def constellation_Sagittarius():
    return render_template('/Constellation/constellation_Sagittarius.html')

@app.route('/constellation_Capricorn')
def constellation_Capricorn():
    return render_template('/Constellation/constellation_Capricorn.html')

@app.route('/special')
def special_thanks():
    return render_template('aboutus.html')


# API 역할을 하는 부분
@app.route('/api/Aquarius', methods=['GET'])
def Aquarius():
    fortune_cons = list(db.fortune.find({'title' : '물병자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Pisces', methods=['GET'])
def Pisces():
    fortune_cons = list(db.fortune.find({'title' : '물고기자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Aries', methods=['GET'])
def Aries():
    fortune_cons = list(db.fortune.find({'title' : '양자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Taurus', methods=['GET'])
def Taurus():
    fortune_cons = list(db.fortune.find({'title' : '황소자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Gemini', methods=['GET'])
def Gemini():
    fortune_cons = list(db.fortune.find({'title' : '쌍둥이자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Cancer', methods=['GET'])
def Cancer():
    fortune_cons = list(db.fortune.find({'title' : '게자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Leo', methods=['GET'])
def Leo():
    fortune_cons = list(db.fortune.find({'title' : '사자자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Virgo', methods=['GET'])
def Virgo():
    fortune_cons = list(db.fortune.find({'title' : '처녀자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Libra', methods=['GET'])
def Libra():
    fortune_cons = list(db.fortune.find({'title' : '천칭자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Scorpio', methods=['GET'])
def Scorpio():
    fortune_cons = list(db.fortune.find({'title' : '전갈자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Sagittarius', methods=['GET'])
def Sagittarius():
    fortune_cons = list(db.fortune.find({'title' : '사수자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

@app.route('/api/Capricorn', methods=['GET'])
def Capricorn():
    fortune_cons = list(db.fortune.find({'title' : '염소자리' },{'_id':False}))
    return jsonify({'cons_fortune': fortune_cons})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)