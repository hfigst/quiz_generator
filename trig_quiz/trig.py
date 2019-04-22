def texify(string):
	''' Converts specific substrings of given string into valid tex code'''
	codes = {
		'sin': '\\sin', 'cos': '\\cos', 'tan': '\\tan', 'csc': '\\csc', 'sec': '\\sec',
		'cot': '\\cot', 'pi' : '\\pi'
		}
	for key in codes:
		string = string.replace(key, codes[key])
	return string

def tex_frac(string):
	''' Parses a string into valid tex code for a fraction.  Numerator and 
	denominator should be delimited by a /'''
	temp = string.split('/')    						#output: ['numerator', 'denominator']
	temp = ''.join(['{' + x + '}' for x in temp])		#output: {'numerator'}{'denominator'}
	return '\\frac{}'.format(temp)

class trig:
	a1 = ['pi/6', 'pi/3', 'pi/4']
	a2 = ['5pi/6', '2pi/3', '3pi/4']
	a3 = ['7pi/6', '4pi/3', '5pi/4']
	a4 = ['11pi/6', '5pi/3', '7pi/4']
	angles = a1 + a2 + a3 + a4

	# Just some placeholders if for any reason someone initializes an object of the trig class
	def __init__(self):
		self.type = 'trig_function'
		self.angle = 'angle'

	def __str__(self):
		return self.type + '({})'.format(self.angle)

	def tex_output(self):
		return '$' + texify(self.type) + tex_frac(texify(self.angle)) + '$'

	@staticmethod
	def create_value_dict(val_order): 			
		angles = trig.angles					
		return dict(zip(angles, val_order))

class sin(trig): 	
	pos_vals = ['1/2', 'sqrt(3)/2', 'sqrt(2)/2']
	neg_vals = ['-1/2', '-sqrt(3)/2', '-sqrt(2)/2']
	val_order = pos_vals + pos_vals + neg_vals + neg_vals
	
	def __init__(self, angle):
		self.angle = angle
		self.type = 'sin'
		self.value_dict = trig.create_value_dict(sin.val_order)

		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'

class csc(trig):
	pos_vals = ['2', '2/sqrt(3)', '2/sqrt(2)']
	neg_vals = ['-2', '-2/sqrt(3)', '-2/sqrt(2)']
	val_order = pos_vals + pos_vals + neg_vals + neg_vals

	def __init__(self, angle):
		self.angle = angle
		self.type = 'csc'
		self.value_dict = trig.create_value_dict(csc.val_order)

		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'

class cos(trig):
	pos_vals = ['sqrt(3)/2' , '1/2', 'sqrt(2)/2']
	neg_vals = ['-sqrt(3)/2', '-1/2' , '-sqrt(2)/2']
	val_order = pos_vals + neg_vals + neg_vals + pos_vals

	def __init__(self, angle):
		self.angle = angle
		self.type = 'cos'
		self.value_dict = trig.create_value_dict(cos.val_order)
		
		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'

class sec(trig):
	pos_vals = ['2/sqrt(3)' , '2', '2/sqrt(2)']
	neg_vals = ['-2/sqrt(3)' , '-2', '-2/sqrt(2)']
	val_order = pos_vals + neg_vals + neg_vals + pos_vals

	def __init__(self, angle):
		self.angle = angle
		self.type = 'sec'
		self.value_dict = trig.create_value_dict(sec.val_order)
		
		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'
	
class tan(trig):
	pos_vals = ['1/sqrt(3)' , 'sqrt(3)', '1']
	neg_vals = ['-1/sqrt(3)' , '-sqrt(3)', '-1']
	val_order = pos_vals + neg_vals + pos_vals + neg_vals
	
	def __init__(self, angle):
		self.angle = angle
		self.type = 'tan'
		self.value_dict = trig.create_value_dict(tan.val_order)
		
		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'

class cot(trig):
	pos_vals = ['sqrt(3)' , '1/sqrt(3)', '1']
	neg_vals = ['-sqrt(3)' , '-1/sqrt(3)', '-1']
	val_order = pos_vals + neg_vals + pos_vals + neg_vals
	
	def __init__(self, angle):
		self.angle = angle
		self.type = 'cot'
		self.value_dict = trig.create_value_dict(cot.val_order)
		
		if angle in self.value_dict.keys():
			self.value = self.value_dict[angle]
		else:
			self.value = 'unknown'

if __name__ == '__main__':
	
	# Test code
	import random

	def generate_random_list():
		trig_functions = [sin, cos, tan, csc, sec, cot]
		angles = trig.a1 + trig.a2 + trig.a3 + trig.a4

		res = []

		for t in trig_functions:
			obj_list = [t(a) for a in angles]
			random.shuffle(obj_list)
			res += random.sample(obj_list, 3)

		random.shuffle(res)
		return res

	l = generate_random_list()
	for t in l:
		l = generate_random_list()
		print('{} is {}'.format(str(t), t.value))




