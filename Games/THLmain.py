import THLfunx
import random
import time

player_name = input("please enter your name here \n (first name is enough but if you still wanna then go ahead)\n")
nor = input ("Enter the no. of rounds you want to play :")
score = 0

while True:
	language = input ("Select your language (1-3)\n 1.Normal\n 2.Snoop dog \n 3.Shakespeare\n Your choice:")
	if (THLfunx.validate(language	) == True):
		break
	else:
		print("you trynna PLAY GAMES with a GAME?! (ಠ~ಠ)!.... Enter a valid choice!")
rno = int(nor)-(int(nor)-1)
s = rno
for i in range (int(nor),0,-1):
	while True:
		
		print("ROUND "+str(s))
		time.sleep(1)
		player = input("Enter what you choose (1-3) \n 1.Tiger \n 2.Hunter \n 3.Lady \n Your choice:")
		
		if (THLfunx.validate(player) == True):
			s+=1
			break
		else:
			responses = ["What's that a dinosaur?.... Enter a valid choice! (─‿‿─) \n",
			"WHAt diD yOu eNteR! Oh nOooooOOoooOO I'm goNNa CrAaaAAaasH!........\n Enter a valid choice, not gonna crash so easily (¬‿¬)!\n",
			"Srsly ... just enter a number (1-3) My GOD HOW SIMPLE IS THAT? and you couldn't do it? (-_-)\n"]
			print(responses[random.randint(0,2)])
			input()
	com = random.randint(1,3)
	output = THLfunx.judge(player_name,int(player),int(com),int(language),int(score))
	print(output)
	input()
	time.sleep(6)


	



