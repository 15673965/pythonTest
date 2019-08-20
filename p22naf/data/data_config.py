# coding:utf-8
class GlobalVar:
	# case_id
	Id = '0'
	request_name = '1'
	url = '2'
	run = '3'
	request_way = '4'
	header = '5'
	case_depend = '6'
	data_depend = '7'
	field_depend = '8'
	data = '9'
	expect = '10'
	result = '11'
# 获取caseid
def get_id():
	return GlobalVar.Id

# 获取url
def get_url():
	return GlobalVar.url

def get_run():
	return GlobalVar.run

def get_run_way():
	return GlobalVar.request_way

def get_header():
	return GlobalVar.header

def get_case_depend():
	return GlobalVar.case_depend

def get_data_depend():
	return GlobalVar.data_depend

def get_field_depend():
	return GlobalVar.field_depend

def get_data():
	return GlobalVar.data

def get_expect():
	return GlobalVar.expect

def get_result():
	return GlobalVar.result

def get_header_value():
	return GlobalVar.header
