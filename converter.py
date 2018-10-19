from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, StringField, TextAreaField

def all_caps(content,separator=','):	
	
	words  = content.split(separator)
	words = [word.upper().strip() for word in words]
	delimiter = separator
	
	return delimiter.join(words)


def all_small(content,separator=','):	
	
	words  = content.split(separator)
	words = [word.lower().strip() for word in words]
	delimiter = separator
	
	return delimiter.join(words)


def first_capital(content):	

	def cap(inscription):
		if not inscription: return ''
		words = inscription.split(' ')
		result = []
		for word in words:
			if not word:
				result.append('')
				continue
			word = list(word)
			word[0] = word[0].upper()
			word = ''.join(word)
			result.append(word)
		return ' '.join(result)
	
	content = content.lower()
	words  = content.split(' ')	
	words = [cap(word).strip() for word in words]
	words = ' '.join(words)

	words  = content.split(',')	
	words = [cap(word).strip() for word in words]
	words = ','.join(words)

	
	return words

def monogram(content,separator=','):	
	
	words  = content.split(separator)
	def camelcasing(inscription):
		result = ''
		for index, char in enumerate(inscription):
			if index%2 == 0:
				result += char.lower()
			else:
				result += char.upper()
		return result

	words = [camelcasing(word).strip() for word in words]

	delimiter = separator
	
	return delimiter.join(words)


def paragraph(content,separator=','):	
	
	words  = content.split(separator)
	words = [word.lower() for word in words]
	words[0] = words[0].capitalize().strip()
	delimiter = separator
	
	return delimiter.join(words)

def insert_symbol(content,separator=' ', symbol='*', spaces=1):	

	words  = content.split(separator)
	words = [word.strip() for word in words]
	delimiter = ' ' * spaces + symbol + ' ' * spaces

	return delimiter.join(words)

def split(content,separator=' ', spaces=1):	

	words  = content.split(separator)
	words = [word for word in words]
	delimiter = ' ' * spaces

	return delimiter.join(words)

def concat(content):	

	words  = content.split(' ')
	words = [word for word in words if word]	

	return ','.join(words)


#--------------------------------FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK FLASK --------------------------------------------



class DataForm(FlaskForm):
	data_field = TextAreaField('Converter Field')
	font_size_field = StringField('Font Size:')
	separator_field = StringField('Separator:')
	spaces_field = IntegerField('Spaces:')
	symbol_field = StringField('Symbol:')


app = Flask(__name__)

app.config['SECRET_KEY'] = 't\x12\xd0\xb7\xab-^g\xc1\xeb\xbc\x0b\xc4\x8e\x1d\xc1G\xffM>\xcd^}\x9f'
app.config['DEBUG'] = True


@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def main():		
	form = DataForm()


	font_size = 20.0
	separator = ','
	spaces = 1
	#form.data_field.data = ''

	separator = form.separator_field.data
	spaces = form.spaces_field.data
	symbol = form.symbol_field.data
	
	if not separator: separator = ','
	if not spaces: spaces = 1
	if not symbol: symbol =  '*'
	


	font_size = form.font_size_field.data
	if not font_size: font_size = 20
	
	form.font_size_field.data = font_size
	

	if 'clear' in request.form:
		#font_size = 15.0
		form.data_field.data = ''
	elif 'basic' in request.form:
		#font_size = 15.0
		form.data_field.data = ''
		form.separator_field.data = ','
		form.spaces_field.data = 1
		form.symbol_field.data = '*'
	elif 'insert_symbol' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = insert_symbol(str(text), separator,symbol,spaces)
	elif 'ABCD' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = all_caps(str(text), separator)
	elif 'abcd' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = all_small(str(text), separator)
	elif 'Abcd' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = first_capital(str(text))
	elif 'aBc' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = monogram(str(text), separator)
	elif 'Abcd efg.' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = paragraph(str(text), separator)	
	elif 'split_by_comma' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = split(str(text), ',', spaces)
	elif 'split_by_space' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = split(str(text), ' ', spaces)
	elif 'split_by_symbol' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = split(str(text), separator, spaces)
	elif 'concat' in request.form:
		#font_size = 15.0
		text = form.data_field.data
		form.data_field.data = concat(str(text))	
	else:
		form.data_field.data = ''
	
	return render_template('index.html', form=form, font_size=font_size)










if __name__ == '__main__':
	"""
	port = 5000 #+ random.randint(0,999)
	url = 'http://127.0.0.1:{0}'.format(port)

	threading.Timer(1.25, lambda: webbrowser.open(url)).start()

	app.run(port=port,debug=False)
	"""
	app.run()
