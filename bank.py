times = 3
password = '123456'
deposit = 10000
while times > 0:
	times -= 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('\n登入成功')
		while True:
			money = input('\n請輸入提款金額: ')
			money = int(money)
			if money <= 0:
				print('\n格式錯誤, 請輸入正整數')
			elif money <= deposit:
				deposit -= money
				print('\n成功提取', money, '元, 餘額為: ', deposit,'元')
			else:
				print('\n餘額不足無法提取')
			quit = input('\n離開請輸入q: ')
			if quit == 'q':
				times = 0
				break
	else:
		print('密碼錯誤!還有', times, '次機會')



