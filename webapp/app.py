from bottle import debug
debug(True)

# add template
from bottle import (route, run, template, request, HTTPError)
from abalone_predictor import AbalonPredictor
from collections import namedtuple
from bokeh.plotting import figure
from bokeh.embed import components

READABLE_SEX=['メス','不明','オス']
# ユーザー入力のパラメータは変わらないので、tuppleで表現
INPUT_DATA=('sex', 'length', 'diameter','height', 'weight')
# Abaloneはユーザー入力のパラメータと年齢を属性として持つクラス
BaseAbalone=namedtuple('BaseAbalone',INPUT_DATA+('age',))

class Abalone(BaseAbalone):
	# propaty記法を用いて、ドット記法でアクセスできるようにする。
	@property
	def sex_str(self):
		return READABLE_SEX[int(self.sex)]

@route('/')
def index():
#	return 'hello bottle!'
	return template('templates/index.tpl')

# @route('/abalone')
@route('/abalone', method='POST')
def result():
#	return 'hello abalone!'
	try:
		age = calc_age(**request.params)
		abalone=Abalone(age=age,**request.params)
#		sex = int(request.params['sex'])
#		length = int(request.params['length'])
#		diameter = int(request.params['diameter'])
#		height = int(request.params['height'])
#		weight = int(request.params['weight'])
#		age = calc_age(sex, length, diameter, height, weight)
	except (TypeError,ValueError) as e:
		raise HTTPError(status=400,body=e)
	else:
		script, div = get_graph(abalone)
		return template('templates/result.tpl', abalone=abalone,script=script,graph=div) # 変数ageを利用
#	return template('templates/result.tpl', sex=READABLE_SEX[sex], length=length, diameter=diameter, height=height, weight=weight,age=age) # 変数ageを利用

# インスタンス化はモジュールの読み込み時のみ行う
_predictor = AbalonPredictor()

def calc_age(sex, length, diameter, height, weight):
	age =_predictor.predict(int(sex), int(length), int(diameter), int(height), int(weight))
	return float(age)
#	return template('templates/result.tpl',sex='不明', length=0, diameter=0, height=0, weight=0, age=0)

def get_graph(abalone):
	p = figure(plot_width=400,plot_height=400,title='実年齢と推定値の分布')
	p.xaxis.axis_label='実年齢'
	p.yaxis.axis_label='推定年齢'

	# 誤差がわかりやすいようにする
	p.line([0,30],[0,30],line_dash='dotted',legend='実年齢と推定値が一致するライン')

	# 実年齢と推定値のデータをプロット
	p.circle(_predictor.y_train,_predictor.prediction,legend='訓練データにおける分布')

	# ブラウザから入力したアワビの推定値をプロっと
	p.line([0,30], [abalone.age, abalone.age],legend= '捕まえたアワビの推定年齢', color='green')

	# 判例の位置を設定
	p.legend.location='top_left'

	# 判例クリックでグラフと判例を半島姪にする
	p.legend.click_policy='mute'

	# javascript コードが生成される
	script, div = components(p)
	return script, div

# reloader にTrue をセットするとファイル更新で再起動する。
run(host='localhost',port=8080,reloader=True)