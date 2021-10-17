from datetime import datetime
import os

def day_converter(day_num):
	day_dict = {0:'日', 1: '月', 2: '火', 3: '水', 4:'木', 5:'金', 6:'土'}
	return day_dict[int(day_num)]

def date_convert_to_string(date_obj):
	date_str = date_obj.strftime('%Y年%m月%d日')
	day = day_converter(date_obj.strftime('%w'))
	time = date_obj.strftime('%H時%M分%S秒')
	return {'date_obj': date_obj, 'date_str':date_str, 'day_str': day, 'time_str': time}

def timestamp():
	stamp = datetime.now()
	stamp_dict = date_convert_to_string(stamp)
	return stamp_dict

def delta_tuple(start, finish):
	delta = finish - start
	seconds = round(delta.total_seconds())
	hour, sec = divmod(seconds, 3600)
	min, sec = divmod(sec, 60)
	
	return hour, min, sec

if __name__=='__main__':
	current_dir = os.getcwd()
	f = input('何について計測しますか？（入力後、Enterキーでスタート）-> ')
	filename = f'{current_dir}/{f}_log.txt'
	start = timestamp()

	right_input = {'q'}
	correct = False
	while not correct:
		s = input('終了する場合は「q」を押してください-> ')
		if s in right_input:
			correct = True
	finish = timestamp()
	hour, min, sec = delta_tuple(start=start['date_obj'], finish=finish['date_obj'])
	delta_str = f'{hour}時間{min}分{sec}秒'

	log_text = f"【{start['date_str']}({start['day_str']})】合計時間：{delta_str}(開始時間：{start['time_str']} - 終了時間：{finish['time_str']})\n"

	with open(filename, 'at') as f:
		f.write(log_text)
	print(f'{filename}への記録が完了しました')
