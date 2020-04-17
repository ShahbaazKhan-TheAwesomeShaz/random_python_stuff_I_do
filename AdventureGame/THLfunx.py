import time
def validate (choice): # To check if :he playin or he PLAYIN if u know what I mean ( ͡~ ͜ʖ ͡°)
	if int(choice) >=1 and int(choice) <=3:
		return True
	else:
		return False

def judge (player_name,pleyah,compyutah,language,score):	#to judge who's the WINNER!! .. sorta (-_-*) and create ossum output
	global result 
	global comment 
	result = " "
	comment = " "
	if pleyah == 1 and compyutah == 2:
		if language ==1 :
			result = player_name +" is tiger and computer is hunter"
			comment = "computer shoots down  "+player_name
		elif language == 2:
			result = "Mah boy "+player_name+ " is the TIGER! and computer's the HUNTER!"
			time.sleep(3)
			comment = "computer unloads dat 9mm mag in the skull of "+player_name+". He DEAD!"
		elif language == 3:
			result = player_name+" chooseth tiger, whereas the computer hath chosen hunter"
			time.sleep(3)
			comment = "Computer lets looseth the bullets in thy skull o "+player_name+", thou art not but expired"
		score-=1
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == 2 and compyutah == 3:
		if language == 1:
			result = player_name +" is hunter and computer is lady"
			time.sleep(3)
			comment = "computer slaps "+player_name+" to death"
		elif language == 2:
			result = "Mah boy "+player_name+" is the HUNTER!! and the computer is a waman!?"
			time.sleep(3)
			comment = "OH!! DAMNNNN!! !ಠoಠ) Computer slaps "+player_name+" so hard, that nigg just travelled all them DIMENSIONS!!... HE ain't getiin up!! "
		elif language == 3:
			result = player_name+" did not but chooseth the hunter, to their surprise computer hath chosen the mistress!"
			time.sleep(3)
			comment = "computer did slapp'd "+player_name+ " oft a times but "+player_name+" being a mere mortal hath left this w'rld"
		score-=1		
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == 3 and compyutah == 1:
		if language == 1:
			result = player_name +" is lady and computer is tiger" 
			time.sleep(3)
			comment = "computer tears "++player_name+" apart"
		elif language == 2:
			result = "yo "+player_name+" is a femme fatale aight, and the computer is a beast tiger!... yeeeeah"
			time.sleep(3)
			comment = "OH SH!T !! (ಠoಠ)"+player_name+"!! rest in pieces.. computer ripped "+player_name+" tah shreds lyk that one time I grinded coffee yo this shit's legit! "
		elif language	==  3:
			result = player_name+" choseth the mistress but dram didst that gent knoweth yond computer hath chosen the tiger"
			time.sleep(3)
			comment = "computer rippeth the mere mortal "+player_name+" into pieces amounting the largest number known to man (who is't wastes timeth f'r counting concluded, be it?) "
		score-=1
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == 2 and compyutah == 1:
		if language == 1:
			result = player_name +" is hunter and computer is tiger"
			time.sleep(3)
			comment = player_name+" shoots down the computer"
		elif language == 2:
			result = "Mah boy "+player_name+ " is the HUNTER! and computer's the TIGER!"
			time.sleep(3)
			comment =player_name +" unloads dat 9mm mag COMPLETELY in the bony head of computer. That nigg DEAD! "
		elif language == 3:
			result = " computer chooseth tiger, whereas "+player_name+" hath chosen hunter"
			time.sleep(3)
			comment = player_name+" lets looseth the bullets in thy skull o computer , thou art not but expired"
		score+=1
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == 3 and compyutah == 2:
		if language == 1:
			result = player_name +" is lady computer is hunter "
			time.sleep(3)
			comment = player_name+" slaps the computer to death"
		elif language == 2:
			result = "Mah boy "+player_name+" issa waman?!.. (he ain't ma boy now) and the computer is a HUNTER!"
			time.sleep(3)
			comment = "OH!! DAAMNNNN!! (ಠoಠ) "+player_name+"slaps computer so hard, that nigg just travelled all them DIMENSIONS!!... HE ain't getiin up!! "
		elif language == 3:
			result = "computer did not but chooseth the hunter, to their surprise "+player_name+" hath chosen the mistress!"
			time.sleep(3)
			comment = player_name+" did slapp'd computer oft a times but computer being a mere mortal hast hath left this w'rld"			
		score+=1 
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == 1 and compyutah == 3:
		if language == 1:
			result = player_name +" is tiger computer is lady"
			time.sleep(3)
			comment = player_name+" tears the computer apart"
		elif language == 2:
			result = "yo the computer is a femme fatale aight, and "+player_name+" is a beast tiger!... yeeeeah"
			time.sleep(3)
			comment = "OH SH!T !! (ಠoಠ) computer!! rest in pieces.. "+player_name+" ripped the computer tah shreds lyk that one time I grinded coffee yo this shit's legit!"
		elif language	==  3:
			result = "computer choseth the mistress but dram didst that gent knoweth yond "+player_name+" hath chosen the tiger"
			time.sleep(3)
			comment = player_name+" rippeths the mere mortal computer into pieces amounting the largest number known to man (who is't wastes timeth f'r counting concluded, be it?)"
		score+=1
		return (str (result +"\n" +comment+"\n Score :"+str(score)))
	elif pleyah == compyutah:
		if language == 1:
			result = "they both chose same"
			time.sleep(3)
			comment = "What more can I say, it's a draw"
		elif language == 2:
			result = "wait... these both niggs look the same aight!!"
			time.sleep(3)
			comment = "Them fools, both stare at each other to death"	
		elif language == 3:
			result == "Both hast hath chosen the same fate and henceforth did not but meet it"	
			time.sleep(3)
			comment == "Stareth into each other's eyes they did, to speak'st the truth , they did so till death came upon them"
		score+=0
		return (str (result +"\n" +comment+"\n Score :"+str(score)))


