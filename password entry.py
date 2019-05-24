password = 'a123456'
i = 3
while True:
	pwd = input('Please input password:')
	if pwd == password:
		print('Correct Assess!')
		break
	else:
		i = i - 1
		print('Wrong Password! You still have ', i, 'chances')
		if i ==0:
			break