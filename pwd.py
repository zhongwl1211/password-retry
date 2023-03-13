#password ='a123456'
#請使用者重複輸入密碼
#最多三次
#正確的話,登入成功
#錯誤的話,'印出密碼錯誤!還有_次機會!'
password ='a123456'
x = 3 #扣打 總次數
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		x = x - 1
		print('印出密碼錯誤!還有', x ,'次機會!')
		if x == 0:
			break
