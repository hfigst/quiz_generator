# Random Trig Problem Generator

import random
from trig import *

def generate_random_list():
		trig_functions = [sin, cos, tan, csc, sec, cot]
		weights = [4, 4, 4, 2, 2, 2]
		angles = trig.angles

		result = []
		
		n = 0
		for func in trig_functions:						
			obj_list = [func(x) for x in angles]		# Creates a list of all possible objects for a single trig function
			random.shuffle(obj_list)					
			result += random.sample(obj_list, weights[n]) 
			n += 1

		random.shuffle(result)
		return result

def return_tex_code():
	template_path = 'trig_quiz_template.txt'
	
	with open(template_path, 'r') as f:
		tex_code = ''.join(f.readlines())

	question_list = generate_random_list()
	questions = ''
	for x in question_list:
		questions += '\\item {}\n'.format(x.tex_output())

	tex_code = tex_code.replace('***Questions***', questions)
	return tex_code

def create_tex_file(tex_code):
	filepath = r'tex_output\trig_quiz.tex'
	
	with open(filepath, 'w+') as f:
		f.write(tex_code)

if __name__ == '__main__':
	
	create_tex_file(return_tex_code())

