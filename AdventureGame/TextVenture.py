import random
import os
import time

def printf(str):#the extra spice!
	for i in str:
		print(i, end = "",flush = True)
		time.sleep(0.1)

def Torcher():
	printf("(You chose this at your own risk if it gets unbearable plz close the game) ")
	printf("You start removing his nails one by one, he screams in agony but you do not care, you ask him again \"What do you people know?\" he replies \"Go to hell\"\nYou cut him from the waist and start peeling his skin on the right side of his waist upwards..He lets out bloodcurdling screams but doesn't answer your question \n your men tell you to stop but you do not, you have now peeled up his skin upto his stomach\nSome of our men start to vomit, some of them run away due to fear, and the ones who remain grab you and stop you\nThe men say\"We would never do such a thing, not to any other human being and we doubt that you are a human being because the way you torchered him\n is the way of the mountain cannibals, we cannot use your help, we cannot let a menace like you live any longer\n\" the men surround you and start attacking you..  ")
	time.sleep(5)
	printf("\n\t")
	End(1)
	input()
	         

	
	

def End(index):#function which stores the ending statement and thankyou
	Ends = ["-----YOU DIED-----\n\n Thanks for playing TextVenture (Made by Shahbaaz Khan)","----------THE END----------\nThanks for playing TextVenture (Made by Shahbaaz Khan) "]
	printf(Ends[int(index)])

#def Exception(invalidInput):
#	Exceptions = ["You summon a magical pony from nothingness and fly into the sky as it leaves a trail of rainbows...\nbut it doesn't exists neither does "+invalidInput+".. In short.. Invalid input,Enter a valid choice","The angels themselves descend from the sky and come down towards you and they say the words which you will remember for a long time..\n They said\" Invalid input, please enter a valid choice!\"(Nah they didn't say anything they are imaginary and so is "+invalidInput+" enter a valid choice plz) ","Suddenly an old lady offers you some peanuts and you grow wings and fly far into the horizon.. Nope that does't happen,\n neither does "+invalidInput+" Hence,ergo,i.e,Therefore... Invalid input, Enter a valid choice. ","Suddenly dumbledore Barges into the room and asks,\"HARRY, DID U PUT YOUR NAME IN THE GOBLET OF FIRE?!\"\nNope wrong story, well "+invalidInput+" is also a wrong choice.. Please Enter a valid choice!"]




	

i=1
while(i<10):	#loop or menu animation
	
	print("\t----------TextVenture----------\t \n\t\t   Made by\n\t\tShahbaaz Khan \n\t       (TheAwesomeShaz)\n\n")


	print("\t----------HOW TO PLAY----------\n\n")
	print("\tTextVenture is an Adventure Game, where your Choices define Your Fate\nWhen prompted for a choice ,enter the number preceeding the option you want to choose.\nand..Yup it's that simple\n\n")
	print(("\n\n-----1.Play \n\n----2.Exit\n\nEnter a number:"))
	
	time.sleep(0.2)
	os.system('cls')

	print("\t----------TextVenture----------\t \n\t\t   Made by\n\t\tShahbaaz Khan \n\t       (TheAwesomeShaz)\n\n")


	print("\t----------HOW TO PLAY----------\n\n")
	print("\tTextVenture is an Adventure Game, where your Choices define Your Fate\nWhen prompted for a choice ,enter the number preceeding the option you want to choose.\nand..Yup it's that simple\n\n")
	print(("\n\n----1.Play\n\n-----2.Exit\n\nEnter a number:"))
	

	time.sleep(0.2)
	os.system('cls')

	i+=1
	#menu = int (input())


	
print("\t----------TextVenture----------\t \n\t\t   Made by\n\t\tShahbaaz Khan \n\t       (TheAwesomeShaz)\n\n")


print("\t----------HOW TO PLAY----------\n\n")
print("\tTextVenture is an Adventure Game, where your Choices define Your Fate\nWhen prompted for a choice ,enter the number preceeding the option you want to choose.\nand..Yup it's that simple\n\n")
menu = int(input("\n\n-----1.Play\n\n----2.Exit\n\nEnter a number:"))
	
if (menu == 1):
	os.system('cls')
	print("Starting Game.")
	time.sleep(1)
	os.system('cls')
	print("Starting Game..")
	time.sleep(1)
	os.system('cls')
	print("Starting Game...")
	os.system('cls')
	printf("Welcome mighty hero on this Medieval Epic Quest!\n ")
	
	def strategy():
		
		name = input("During the discussion you meet the Great Elder, he asks you \"What is your name Child?\"\n\nEnter Your Name:")
		printf("\n\nThe Great Elder or the village tells you that \nThe king's defences are strong but most of the guards are drunk during night\n\nThe best way to attack would be at night\n\n")
		cs1 = int(input("----1.Gather the village's forces and plan an attack on the kingdom\n\n----2.Protest and satisfy the needs \n\nYour Choice:"))
		if(cs1==1):
		
			printf("You Decide to attack the kingdom, and gather all the men and head towards the palace at night and When you reach the palace, you and your army of 30 men is \nwell hidden in the forest.. You see two guards at the main gate of the palace\nNow the men from among you start arguing one of them says \"The guards are drunk anyway lets just barge in on them and take their weapons and kill all of them inside the palace too!!\" \nBut another one says\"Did we not kill three of their men? they know we are going to revolt and they maybe expecting our attack!\"\n\"Yes..Let us not underestimate them!\"another one adds.One of the great elder's sons says\"We do not know that! infact, we do not know anything, let us not jump to conclusions by making\nfavourable assumptions\" he then goes on to say\"Let us leave the decision to our brave man who has been in a grave situation before and escaped by killing or fleeing\"\nHe means YOU! What do you choose?\n\n")
			cs01 = int(input("----1.Go ahead with a full on attack by charging through the main palace gate\n\n----2.Go with a stealthy approach\n\nYour Choice:"))
		#yaase likhna hai
			if(cs01 == 1):
				printf("You and the army come to the conclusion that 30 men are greater than two drunk men and can\nEasily defeat them..All men charge towards the two guards, The two guards are alert! one of them runs inside and the other\none draws his sword and is ready to fight! But as he sees the men appear from the forest.. he turns back and starts to run.. drops his sword in fright and starts running inside\nYour men catch him he failed to escape! He dosen't seem drunk but you see a bottle of wine that he had with him\nYou tie him to a nearby tree and interrogate him\"What is the king planning? \nWHY DID THE OTHER GUARD RUN INSIDE? \nDID YOU KNOW ABOUT OUR ATTACK?\" He answers all this just the same...\"I won't tell you anything you peasant lowlifes deserve to die!\"What do you do now? Maybe he doen't know? maybe he knows but isn't telling...\nThere may be an entire legion of guards getting ready for the village's execution because they might have heard about the three mrurdered guards? or they may have no idea and all of them are sleeping probably drunk\nAfter a bit of discussion with the men, you now have these options\n\n")
				cs02 = int(input("----1.Make him forcibly drink wine and thereby spill out the truth\n\n----2.Torcher him until he says the truth\n\n----3.Kill him, wear his clothes, go in and open the gate for the army\n\n(Warning! Choose option 2 only if you can withstand a lot of bloodshed)\n\n\nYour Choice:"))
				if(cs02==1):#end
					printf("You make him forcibly drink all the wine in his bottle, he says gibberish at first but then you threaten him\nHe replies \"Neither you nor your men can do us any harm.. What did you think? that we didn't know about what you did?\nThose three men you killed ... didn't they have families? You all will pay the price! The king knows The entire court knows! You peasants don't stand a chance\n after that he passes out\n")
					Stealth()
					input()

				elif(cs02==2):
					Torcher()

				elif(cs02==3):#end
					printf("You take your sword and stab him in the neck, he dies after bleeding for some time,")
					printf("You take his armour and clothes and weapons and head into the court by climbing the wall by climbing a tree which is near the wall and jumping off the tree, You tell your men to wait for the signal..\nYou enter the gate slowly and raise no suspicion, you see that it IS true.. most of the guards ARE asleep on duty!\nYou gee a guard continuously banging on a door\nMaybe he is the guard who ran back inside after he saw the army? Does he know that there is an army here?! You go and grab him\nin a headlock, he struggles for sometime, then goes unconscious\nAfter searching a few rooms you find the room where all the stolen goods of the village vendors and merchants are kept! You find the opening of the main gate,\n you open the gate and signal the men to come inside, they all are happy to find their goods in here and they send some men to the village to bring a carriage\n you and the men take the stolen goods and are heading towards the exit, but you see a line of guards standing at the gate,there are about 20 guards and your armyconsists of 27 men now\n(as three men have gone to get the caravan) you order the guards to let them go! and you say that it is the king's order!\nThe guards start moving away and let you people pass, till then, the caravan had arrived and you start loading the goods into the carriage, then all of a sudden!!\n\n")
					time.sleep(5)
					printf("The guards are on the fort walls and are shooting arrows at you! \nmaybe the one you left unconscious woke up and told them about what is going on?! you take the reins of the horses and start driving the caravan, some of the men\nare with you in the carriage and the others anre rushing on foot! but then the moon was covered by the clouds..after a while, the clouds shift... The full moon appears..\n")
					time.sleep(5)
					printf("your heart skips a beat\nYour eyes stare in horror as you see the guards standing ALL ALONG THE FORT WALL WITH ARROWS WHICH HAVE FLAMING ARROWHEADS!\n")
					time.sleep(5)
					printf("You can't steer away because there is a forest on the left, the fort wall on the right, this is the only road that can lead you to the village\nYou continue driving the carriage, \nand hear the screams of your men behind you, they are being hit by the arrows! Do you throw away some goods from the carriage and let some of the running men in?\n but that would mean to slow the chariot down and it would give the archers a better aim! What do you do?")
					cst1 = int(input("\n\n----1.Slow down the chariot\n\n----2.Leave the men and spur your horses\n\nYour Choice:"))
					if(cst1==1):
						printf("You tell the men in the chariot to throw some goods away and make space for more men\nYou slow down the chariot for the men to come inside, but the archers aim at he the chariot instead of the leftover men!\nThe chariot's left hind wheel is now set ablaze, you get hit by arrow too but you are saved by the armour, the wheel is now about to break\nif this keeps going on, the whole chariot will burn and all men will die!\nYou suddenly a though crosses your mind, it is very selfish but it doesn't matter now\nYour adrenaline is too high and you do not care about others anymore, it's your life which is the most important right now!!\n")
						time.sleep(6)
						printf("You get on one of the horses, cut it loose and gallop away\n you heard screams of agony? or were they abuses? curses? or cries for help? \nyou were trembling with fear as you spurred your horse into the distance.\n\n  ")
						time.sleep(5)
						printf("you do not remember how far you rode that night, but you DID NOT LOOK BACK ..\nThe sun was rising up now.. Ofcourse! you lost your way! You are now in a desert!...Where will this path lead you?\n\nhow long will you be alive?\n\nhow long until those men find you again?\n\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
						time.sleep(5)
						printf("\n\t")
						End(1)
						input()
					elif(cst1==2):
						print("You spur your horses faster, The running men start hurling abuses, half of them are dead\nchills run down your spine as you see some of them have flaming arrows in their shoulders, some of them are getting hit in the head,The chariot's left hind wheel is now set ablaze by a flaming arrow, you get hit by arrow too but you are saved by the armour, the wheel is now about to break\nif this keeps going on, the whole chariot will burn and all men will die!\nYou suddenly a though crosses your mind, it is very selfish but it doesn't matter now\nYour adrenaline is too high and you do not care about others anymore, it's your life which is the most important right now!!\n")
						time.sleep(6)
						printf("You get on one of the horses, cut it loose and gallop away\n you heard screams of agony? or were they abuses? curses? or cries for help? \nyou were trembling with fear as you spurred your horse into the distance.\n\n  ")
						time.sleep(5)
						printf("you do not remember how far you rode that night, but you DID NOT LOOK BACK ..\nThe sun was rising up now.. Ofcourse! you lost your way! You are now in a desert!...Where will this path lead you?\n\nhow long will you be alive?\n\nhow long until those men find you again?\n\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
						time.sleep(5)
						printf("\n\t")
						End(1)
						input()		
			elif(cs01 == 2):
				printf("You all decide to take a silent approach, you sneak near the guards unnnoticed, you throw a stone at one of them, he turns around and comes towards the bush,\n the other guard sits on his chair outside the castle gate and starts drinking, as the first guard approaches closer your heart starts to race\nYou do not know if you can pull this off.. you are hands shaking with fear, as he comes close enough, you grab him\nand choke him, he seems unconscious")
				Stealth()
		#protest wala case		
		elif(cs1==2):
			printf("\n\nYou and all the Villagers agree to protest against the king and thereby \nSatisfying the demands..You and a bunch of people go to King IDOM's palace which is really big and grand\nThe Guards let you in once tell them about the treaty.. after an hour's wait, the king finally arrives\nTwo whole hours go past in you trying to convince the king but he remains peacefully stubborn as ever\nHe tells you to wait and that he will discuss the matter with his councilmen..After another hour he willingly agrees to your demands\nAlso he says that There will be a great feast the next day and all the villagers are invited\nSo you and the villagers head back home satisfied and in a sense of triumph\n")
			printf("When you and your companions reach the village, and narrate the whole incident..\nThe village elder advises you to be careful and that \nthis might be another one of the king's dirty tricks you reply\n\n")
			printf("Yes ofcourse we will carry small and well hidden weapons for our self defence..No chance for surprises!\n")
			time.sleep(5)
			printf("The next day you wake up and get ready for the event (You hide your weapon with you people forget to carry weapons in their excitement)\n along with all the villagers, you head into the king's courtyard, it is so spacious that it has space left\nEven after accomodating so many people, The king's throne is made of gold, has a few stone steps on all four sides leading to a royal gold chair. You gaze around and see the joy of the people \nas they are feasting, Then the king does a special announcement and serves a special drink\n\"The purest grape juice\" he calls it, the royal servants deliver it to you, The king speaks in a royal kingly tone\n\"My fellow villagers! you have suffered much oppression as it is.. I did not know about this corruption in our land\"\nSuddenly you hear a man cough very loudly .. you ignore him and continue listening to the King's speech\nThe king says\"Today is the day When All men are free and not oppressed!\"You hear three more men coughing loudly.. you ignore them,\"Today is the DAY all you people get what you deserve!\"\nYou are totally listening to the king not paying attention to the surroundings")
			printf("\n\"TODAY IS THE DAY YOU PEASANTS DIE! AND WE ROYALS ARE FREE OF YOUR BURDEN!\"..You come out of the trance and look around you.. All the people are not JUST COUGHING.. they are COUGHING BLOOD!!!\n Except you! you did not drink the royal grape juice! the king poisoned all the villagers!!..\nYou Stare in horror as you hear the screams of agony and then \n you see the guards coming and killing those villagers who were not poisoned\nYou run towards the king's throne, the guards being busy killing people do not notice you bolting towards the throne..You Sneak from behind\nThe king doesn't notice you, he has an evil smirk on his face seeing the villagers die\nYou take your dagger and run it through the king's heart, Then you gaze lifelessly as he falls to the ground and a puddle of blood is created, One of the Guards notices this and signals to the others! You are exposed!! \n\n")
			time.sleep(5)
			cs2 = int(input("----1.Blending in with the crowd and find a way out\n\n----2.Fight your way through with your small dagger\n\nYour Choice:"))
			#Blend In hoke bhaago case
			if(cs2 ==1):
				printf("You quickly run behind the throne, some of the guards are now searching for you..\n You start making your way through the crowd when you notice a guard coming your way! You suddenly start walking in a different direction,\n You see another guard coming your way from that side, you turn behind and a guard grabs you in a headlock! You are almost about to pass out!\n")
				time.sleep(5)
				printf("You take hold of your dagger and stab him in the head, he falls down to the ground!\nYour hands shiver with fear as you try to pull the dagger out, but the handle of the dagger has gone into his socket\nNow you don't see any other guards approaching..\nYou drag his body across the field of chaos all the way behind a giant rock.. You put on his armor, take his weapons and start heading towards the exit..\nThen you hear a guard scream \"THE KING HAS BEEN MURDERED! BLOCK ALL THE EXITS! THERE IS A MURDERER AMONG US!\" You quicken your pace towards the exit, When all of a sudden you see a swarm of Soilders approaching towards the exit.. If you run maybe you can make it?!\nOr stay blended in and avoid raising suspicion?!\n\n")
				cs3 = int(input("----1.Run towards the exit\n\n----2.Stay blended and reach for the exit\n\nYour Choice:"))
				if(cs3 ==1):
				#die
					printf("You start running towards the exit, the guards seem suspicious of you and some of them start following you\nYou see the exit,you go right out of the door and start running back to the village\n but then suddenly you get hit by arrows! One on the back of the knee, One on the shoulder blade and you fall down and scream in agony\n You look up towards the sky for help, you see a small line..")
					time.sleep(5)
					printf("The line grows shorter and shorter.. Now it has become a Dot..\nThe dot grows bigger and bigger suddenly something goes into your eye, It causes excrutiating pain, you find out that it is an arrow shot by the archers.. well that doesn't matter now does it?")
					time.sleep(5)
					printf("\n\t")
					End(0)
					input()
				elif(cs3==2):#end 
					printf("Inspite of the mental trauma you are experiencing and the cries for help you hear of the people, you manage to blend in the crowd\nNow you see the gate infront of you, but you also see archers on the rooftops!\n You see guards highly concentrated near the main gate! You almost reach the main gate, and no one noticed you...")
					time.sleep(5)	
					printf("Yet")
					time.sleep(5)
					printf("The guard shouts from behind You don't even know what he is screaming you start running out of the gate, it's not like you wanted to run\nIt was a reflex, Your mind could not bear anymore of this horrific chaos!\nThe Guard is chasing you and falls hard on the ground face first!\nIt is the great elder, he caught the guards leg and made him trip! but you see the blood all over his face he is about to die! he tells you to escape! You do not stop\nNot even for a second!... As you are running away you can hear the screams of the great elder.. was he stabbing him? hitting him? was it the poison?\nyou don't even know, you are now very far away from the royal palace you sit down to take a breath, the world starts going black from the sides\n maybe it was due to the continuous running..you lose consciousness after a while... You wake up after a while.. You start walking again ..\n")
					time.sleep(5)
					printf("Where will this path lead you?\n\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
					input()
				#don't die
			#ladleteve bhaago case
			elif(cs2==2):
				printf("You start running towards the exit with the small dagger in your hand, it doesn't take long before you gather the attention of all guards!!\nYou see three guards infront of you and only god knows how many are behind you at this point!\nThe three infront haven't noticed you yet, You stab one in the Stomach, another one in the neck!\n but The third guard notices you! He has his sword drawn and is coming towards you...\n\n")
				time.sleep(5)
				csa = int(input("----1.Run away towards the exit which is slightly visible far away\n\n----2.Stab him in the aorta\n\n----3.Stab him in the Skull\n\nYour Choice:"))
				if(csa ==1):#dead
					printf("You start running towards the exit and make your way through the crowd as fast as you can, dodging arrows and pushing away people who are coughing blood,\n By now almost all the guards are behind you You have gathered a lot of attention, You see the exit now!! it's right ahead but you also see something else!\n")
					time.sleep(5)
					printf("You see a large swarm of guards approaching towards that exit! they are there to block your path! You turn back and suddenly a sword goes into your left eye and through your skull..")
					time.sleep(5)
					printf("\n\t")
					End(0)
					input()
				elif (csa == 2):#dead
					printf("You run towards him with you dagger ready! Then you stab him in the Aorta \nYour adrenaline rush is so high that you can't even feel your own arms and legs anymore.. suddenly all your strength\nstarts to fade.. You grow weaker and weaker each second...\n")
					time.sleep(5)
					printf(" it is then that you notice the persian shamshir that is through and through your ribcage..\nYou start to lose consciousness.. ")
					time.sleep(5)
					printf("\n\t")
					End(0)
					input()
				elif(csa ==3):#end
					printf("You run towards him, take a herculean leap and stab him in the space between his ear and eye!\nYour hands are shivering with fear as you try to pull the dagger out, but it is stuck!\nYou hear men scream behind you \"INFIDEL DIE!!!\" \nYou start running towards the exit which is almost visible now, You are running out breath and....")
					time.sleep(5)
					printf(" you Finally run out of the gate, The guards stop chasing you.. but the archers on the rooftop start raining down arrows! You quickly jump into the river ahead and the archers lose track of you.. You swim across to the other shore, and lay there unconscious\n")
					time.sleep(5)
					printf("You wake up...\nYou start walking...\nWhere will this path lead you?\nHow long will you live?\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
					printf("\n\t")
					End(1)
					input()




	def Stealth():
		printf("You take his armour and clothes and weapons and head into the court by climbing the wall by climbing a tree which is near the wall and jumping off the tree, You tell your men to wait for the signal..\nYou enter the gate slowly and raise no suspicion, you see that it IS true.. most of the guards ARE asleep on duty!\nYou gee a guard continuously banging on a door\nMaybe he is the guard who ran back inside after he saw the army? Does he know that there is an army here?! You go and grab him\nin a headlock, he struggles for sometime, then goes unconscious\nAfter searching a few rooms you find the room where all the stolen goods of the village vendors and merchants are kept! You find the opening of the main gate,\n you open the gate and signal the men to come inside, they all are happy to find their goods in here and they send some men to the village to bring a carriage\n you and the men take the stolen goods and are heading towards the exit, but you see a line of guards standing at the gate,there are about 20 guards and your armyconsists of 27 men now\n(as three men have gone to get the caravan) you order the guards to let them go! and you say that it is the king's order!\nThe guards start moving away and let you people pass, till then, the caravan had arrived and you start loading the goods into the carriage, then all of a sudden!!\n\n")
		time.sleep(5)
		printf("The guards are on the fort walls and are shooting arrows at you! \nmaybe the one you left unconscious woke up and told them about what is going on?! you take the reins of the horses and start driving the caravan, some of the men\nare with you in the carriage and the others anre rushing on foot! but then the moon was covered by the clouds..after a while, the clouds shift... The full moon appears..\n")
		time.sleep(5)
		printf("your heart skips a beat\nYour eyes stare in horror as you see the guards standing ALL ALONG THE FORT WALL WITH ARROWS WHICH HAVE FLAMING ARROWHEADS!\n")
		time.sleep(5)
		printf("You can't steer away because there is a forest on the left, the fort wall on the right, this is the only road that can lead you to the village\nYou continue driving the carriage, \nand hear the screams of your men behind you, they are being hit by the arrows! Do you throw away some goods from the carriage and let some of the running men in?\n but that would mean to slow the chariot down and it would give the archers a better aim! What do you do?")
		cst1 = int(input("\n\n----1.Slow down the chariot\n\n----2.Leave the men and spur your horses\n\nYour Choice"))
		if(cst1==1):
			printf("You tell the men in the chariot to throw some goods away and make space for more men\nYou slow down the chariot for the men to come inside, but the archers aim at he the chariot instead of the leftover men!\nThe chariot's left hind wheel is now set ablaze, you get hit by arrow too but you are saved by the armour, the wheel is now about to break\nif this keeps going on, the whole chariot will burn and all men will die!\nYou suddenly a though crosses your mind, it is very selfish but it doesn't matter now\nYour adrenaline is too high and you do not care about others anymore, it's your life which is the most important right now!!\n")
			time.sleep(6)
			printf("You get on one of the horses, cut it loose and gallop away\n you heard screams of agony? or were they abuses? curses? or cries for help? \nyou were trembling with fear as you spurred your horse into the distance.\n\n  ")
			time.sleep(5)
			printf("you do not remember how far you rode that night, but you DID NOT LOOK BACK ..\nThe sun was rising up now.. Ofcourse! you lost your way! You are now in a desert!...Where will this path lead you?\n\nhow long will you be alive?\n\nhow long until those men find you again?\n\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
			time.sleep(5)
			printf("\n\t")
			End(1)
			input()
		elif(cst1==2):
			print("You spur your horses faster, The running men start hurling abuses, half of them are dead\nchills run down your spine as you see some of them have flaming arrows in their shoulders, some of them are getting hit in the head,The chariot's left hind wheel is now set ablaze by a flaming arrow, you get hit by arrow too but you are saved by the armour, the wheel is now about to break\nif this keeps going on, the whole chariot will burn and all men will die!\nYou suddenly a though crosses your mind, it is very selfish but it doesn't matter now\nYour adrenaline is too high and you do not care about others anymore, it's your life which is the most important right now!!\n")
			time.sleep(6)
			printf("You get on one of the horses, cut it loose and gallop away\n you heard screams of agony? or were they abuses? curses? or cries for help? \nyou were trembling with fear as you spurred your horse into the distance.\n\n  ")
			time.sleep(5)
			printf("you do not remember how far you rode that night, but you DID NOT LOOK BACK ..\nThe sun was rising up now.. Ofcourse! you lost your way! You are now in a desert!...Where will this path lead you?\n\nhow long will you be alive?\n\nhow long until those men find you again?\n\nWhen will corruption in this world end?\n\nWill the poor people around the world ever get what they deserve?\n\nDo these \"ROYAL\"people have humanity left in them? That my friend "+name+" is for you to answer (^_^)!")
			time.sleep(5)
			printf("\n\t")
			End(1)
			input()



	def smokebomb():
		
		if(c301 == 1):#dead
			printf("\n\nYou pull out your sword and ATTACK the guard closest to you he deflects your attack with his sword\n you strike again he dodges it\nBut the other guards shoots an arrow into your head\n\t")
			End(0)
			input()
		elif(c301 == 2):   
			printf("\n\nYou Throw a smoke bomb at the ground, suddenly every thing becomes blurry...")
			time.sleep(5)
			printf(" you cover your mouth with a cloth to prevent the smoke and kill those three guards with your sword.\nAfter a while, when the smoke dissapears.. YOU see 3 carcasses laying on the ground.. All the villageFolks witnessed this.. ")
			time.sleep(5)
			printf("They Come towards you praising and thanking you for saving them from the corrupt king!..They ask")
			printf(" \"how can we repay you?\"\n\n")
			#cho0se anything same outcome wala case cuz my wish ( -_-)! 
			c302 = int(input("----1.Ask for money and head on with your journey\n\n----2.Ask for food and shelter and Spend the night\n\nYour Choice:"))
			if(c302 == 1):
				printf("\n\nYou ask them for money, they give you only 100 coins they seem very poor by their lifestyle\nYou ask them why is this village in such a condition, they tell you about the corrupt king IDOM and his actions\nThe soilders usually take away more than half of their farm's produce and Levy heavy taxes\nThey ask for your help in this matter\n\n")		
				
			elif(c302 == 2):
				printf("\n\nYou ask them for food and shelter, they give you food and an old grass hut shelter to sleep, they seem to be good people\nYet they seem very poor by their lifestyle\nYou ask them why is this village in such a condition, they tell you about the corrupt king IDOM and his actions\nThe soilders usually take away more than half of their farm's produce and Levy heavy taxes\nThey ask for your help in this matter\n\n")
				
			c303 = int(input("----1.Help the people by Staying there and forming a strategy\n\n----2.Say\"I have other buissinesses to attend and I am sorry to hear this\"\n\nYour Choice:"))
			if (c303==1):
				printf("\n\nYou decide to stay in that village and form a strategy, after a full day of discussion and a full night's sleep \n\n")
				strategy()
			


					#mountains wala case Smokebomb wala case continued		
			elif (c303==2):    
				printf("\n\nYou take their parting gift of 100 coins and move along with your journey\nYou tread along the same path which leads you to a valley between mountains\nThere is a small river there with freshwater and fishes you start hunting fishes with your sword and \ncatch 2 fishes after a long hour suddenly you hear a man shout \"STOP RIGHT THERE YOU! WHAT DO YOU THINK YOU ARE DOING?\"\nyou tell him that you were catching fish to cook as food.. he is extremely angered by your statement\nHe SCREAMS\"you dare to kill our GODS!! YOU WILL BE OUR MEAL FOR TONIGHTS PARTY!!\"\nYour eyes stare in horror while you start to slowly step back when you see more men on the top side of the mountains, They have got bows and arrows!..\n You see a small passageway through the cave, but you also see a small opening underneath the freshwater lake.. \nyou see seagulls on the other side of the mountains and before those seagulls you see your death\n\n")
				c305 = int(input("----1.Run towards the cave opening \n\n----2.Dive underwater and swim into the underwater Cave opening\n\n----3.Try to bribe the cannibals with all you money\n\nYour Choice:"))
				if (c305 ==1 ):#dead
					printf("\n\nYou run towards a small cave opening which you think will lead you further ahead, you are frantic and LITERALLY RUNNING FOR YOUR LIFE\nThe cave is a dead end, you bolt out of the cave and start running away from the menyou keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
					time.sleep(5)
					End(0)
					input()
				elif(c305 == 2):
					printf("\n\nYou take a deep breath and dive into the lake and swim towards the small opening, it is small but you squeeze through it\nyou are now in a larger waterbody (you guessed that there might be a larger lake by seeing those seagulls)\nyou swim frantically to the top of the ocean until your last breath\nyou are about to passout when you finally reach the surface\nYou See a Beach in a long distance, it looks like a village or a small town\nDifferent from the one you saw before\nyou start swimming towards land, after reaching you are totally exhausted and lay on the beach lifeless\n")
					time.sleep(5)
					printf("\nyou wake up in a room, looks like a sickbay, you get up and thank the people who helped you\nYou ask if they have your clothes and weapons, they say that they would give it\nbut they had a favour to ask... they heard about how you came through that passageway,\nThey figured that you had escaped from the cannibals..They want you to help them in stopping \nthe Evil king IDOM from taking away their cattle forcibly and that his men come during the night to take away their\ngoods,cattle and whatever money they could find..You tell them that you need time to think and make a strategy..\nAfter an hour of brainstorming and a full night's sleep you come to these conclusions:\n\n")
					strategy()#func Call
				
				elif(c305 == 3):#dead
					printf("You try to bribe them with 100 gold coins, The men from the top of the mountain start raining down arrows\nYou start running as you keep running you keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
					time.sleep(5)
					End(0)
					input()
				
		elif(c301 == 3):#run4life case #dead
			printf("\n\nyou START TO RUN FOR YOUR LIFE.. you are almost losing them but an arrow hits you in the back of your knee\nThe soilder's hand raises the sword and that is the last thing you ever see..\n\n")
			time.sleep(5)
			End(0)
			input()
						#somke bomb case end



    #the game code or the control starts from here

	printf("\n You embark on a journey, which leads to an abandoned road\nWhere you see an old man lying on the road\nThe old man's leg looks badly wounded\n\n")
	c1 = int(input("----1.You help the old man \n\n----2.You leave him be and mind your own buissiness\n\nYour Choice:"))
	if(c1 == 1):
		printf("\nYou decide to help the old man\n The old man tells you not to help him\nas he is a wanted man and the guards are still looking for him\n\n")
		c2 = int(input("----1.Carry the old man to a nearby village anyway\n\n----2.Leave him to his fate\n\nYour Choice:"))
		if(c2==1):
			printf("\nYou pick up the old man and start walking hoping to find a village on the way, you ask the old man\n why he was being chased by the guards..The old man says,\"I told you that you should have left me there.. it is a long story I used to be one \nof the closest Members of his council One day our king decided... to increase the taxes to get rid \nof the poor people in town, because poor people cannot pay taxes, so they have to sell their lands to the Kingdom..\n I opposed this decision while all the other council members approved, They even tried to bribe me but I refused\nThen the king ordered me dead and hence I am running since.\"")
			printf("\n\n You come across a small village in the woods, you are casually talking with the old man \nand walking towards it while you see the royal guards enquiring people about something, They have spotted you!!")
			c3 = int(input("\n\n----1.Continue walking towards the village with the old man on your back\n\n----2.Leave the old man near the tree and find out what is going on\n\n----3.Run in the opposite direction\n\nYour Choice:"))			
			

			if(c3==1):
				printf("\n\nYou continue walking casually as if nothing ever happened with the old man on your back..\nThe guards identify the old man and the chief of the guards exclaims\n\"Why are you helping that wanted man! He is a wicked being whose execution has been ordered!\"\nYou are about to explain the situation but the guard interrupts you and says \" You are Helping him!!! You too must DIE ALONGSIDE HIM!!\"\n\n")
				c301 = int(input("----1.Pull out your sword and stab the nearest Soilder\n\n----2.THROW the smoke bomb and kill all the guards who are stunned by the smoke\n\n----3.Run away Leaving the old man(you can't carry him now)\n\nYour Choice:"))
				'''if(c301 == 1):#dead
					printf("You pull out your sword and ATTACK the guard closest to you he deflects your attack with his sword\n you strike again he dodges it\nBut the other guards shoots an arrow into your head\n\t-----YOU DIED-----\n\n Thanks for playing TextVenture (Made by Shahbaaz Khan)")
					input()'''
				

				smokebomb()
				#copy from this smokebomb case
				

			elif(c3==2):
				printf("\nYou leave the old man near the tree and go ahead.. The guards \nask you who was that you left behind.. you say you don't know what they are talking about..\nThe guards go and check behind the tree the old man is no longer there!..\nThe chief of the guards says \"ARREST HIM! HE IS WITH THE TRAITOR COUNCILMAN! \nAnother guard says\"yes! I SAW THAT MAN HE WAS CARRYING ON HIS BACK! it was the COUNCILMAN!\"")
				c4 = int(input("\n\n----1.Resist Arrest(Fight those 3 guards)\n\n----2.Obey their orders\n\nYour Choice:"))
				if(c4==1):
					printf("\n\nYou have decided to Resist arrest! What do you do?")
					c301 = int(input("\n\n----1.Pull out your sword and stab the nearest Soilder\n\n----2.THROW the smoke bomb and kill all the guards who are stunned by the smoke\n\n----3.Run away Leaving the old man(you can't carry him now)\n\nYour Choice:"))	
					#smokebom case ka copy
						#pastesmokebomb case here
					smokebomb()
					
				elif(c4==2):#dead
					printf("The chief says\"There will BE  NO TRIAL FOR YOU BECAUSE WE WILL FIND THAT OLD TRAITOR ANYWAY.. KILL HIM!\"\n.. you START TO RUN FOR YOUR LIFE.. you are almost losing them but an arrow hits you in the back of your knee\nThe soilder's hand raises the sword and that is the last thing you ever see..\n\t")
					End(0)				
					input()
			elif(c3==3):#dead
				printf("The guards spot you and the wanted councilman, the archer shoots an arrow which strikes and goes through \nboth your and the old man's neck\n\t")
				End(0)
				input()
		elif(c2==2):

			#paste the code of mountain cannibals here
			
			printf("\n\nYou  move along with your journey\nYou tread along the same path which leads you to a valley between mountains\nThere is a small river there with freshwater and fishes you start hunting fishes with your sword and \ncatch 2 fishes after a long hour suddenly you hear a man shout \"STOP RIGHT THERE YOU! WHAT DO YOU THINK YOU ARE DOING?\"\nyou tell him that you were catching fish to cook as food.. he is extremely angered by your statement\nHe SCREAMS\"you dare to kill our GODS!! YOU WILL BE OUR MEAL FOR TONIGHTS PARTY!!\"\nYour eyes stare in horror while you start to slowly step back when you see more men on the top side of the mountains, They have got bows and arrows!..\n You see a small passageway through the cave, but you also see a small opening underneath the freshwater lake.. \nyou see seagulls on the other side of the mountains and before those seagulls you see your death\n\n")
			c305 = int(input("----1.Run towards the cave opening \n\n----2.Dive underwater and swim into the underwater Cave opening\n\n----3.Try to bribe the cannibals with all you money\n\nYour Choice:"))
			if (c305 ==1 ):#dead
				printf("\n\nYou run towards a small cave opening which you think will lead you further ahead, you are frantic and LITERALLY RUNNING FOR YOUR LIFE\nThe cave is a dead end, you bolt out of the cave and start running away from the men you keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
				time.sleep(5)
				End(0)
				input()
			elif(c305 == 2):
				printf("\n\nYou take a deep breath and dive into the lake and swim towards the small opening, it is small but you squeeze through it\nyou are now in a larger waterbody (you guessed that there might be a larger lake by seeing those seagulls)\nyou swim frantically to the top of the ocean until your last breath\nyou are about to passout when you finally reach the surface\nYou See a Beach in a long distance, it looks like a village or a small town\nDifferent from the one you saw before\nyou start swimming towards land, after reaching you are totally exhausted and lay on the beach lifeless\n")
				time.sleep(5)
				printf("\nyou wake up in a room, looks like a sickbay, you get up and thank the people who helped you\nYou ask if they have your clothes and weapons, they say that they would give it\nbut they had a favour to ask... they heard about how you came through that passageway,\nThey figured that you had escaped from the cannibals..They want you to help them in stopping \nthe Evil king IDOM from taking away their cattle forcibly and that his men come during the night to take away their\ngoods,cattle and whatever money they could find..You tell them that you need time to think and make a strategy..\nAfter an hour of brainstorming and a full night's sleep you come to these conclusions:\n\n")
				strategy()
						
			elif(c305 == 3):#dead
				printf("You try to bribe them with 100 gold coins, The men from the top of the mountain start raining down arrows\nYou start running as you keep running you keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
				time.sleep(5)
				End(0)
				input()
			
	elif(c1==2):
		
		'''printf("You travel along the path leaving the old man be and you are now in a forest..\n  you hear the birds chirping and feel the cool wind blowing you see the butterflies of different colors \nand greenery everywhere you are enjoying nature but suddenly...\n")
		time.sleep(5)

		printf("you see a Dark figure lurk around the bushes")

		cf= int(input("----1.Go and check what's up with the bush\n\n----2.Walk away on your path\n\nYour Choice:"))
		if(cf==1):
			printf("You decide to go and check what is hiding behind the bush... \nBut u trip over a rope! The rope gets tied to your leg and the next moment you open you eyes you are hanging upside down!\nYou see three men running towards you with spears in their hands! You cut off the rope and fall on your head.. The men are getting closer!.. you get up and the three men are standing right in front of you\n they say \"You seem to be a well equipped traveller! a nice sword isn't it? well it can be sold for a large amount! Give us all your goods and we may consider letting you live!\" What will you do? Attack? Or run away? There might be  \n\n")
			time.sleep(5)
			cf2 = int (input("----1.Grab the man and Cut his throat with your sword\n\n----2.Run away"))
		
		elif(cf==2):'''

		

		#leave the old man then you go here
		printf("\n\nYou move along with your journey\nYou tread along the same path which leads you to a valley between mountains\nThere is a small river there with freshwater and fishes you start hunting fishes with your sword and \ncatch 2 fishes after a long hour suddenly you hear a man shout \"STOP RIGHT THERE YOU! WHAT DO YOU THINK YOU ARE DOING?\"\nyou tell him that you were catching fish to cook as food.. he is extremely angered by your statement\nHe SCREAMS\"you dare to kill our GODS!! YOU WILL BE OUR MEAL FOR TONIGHTS PARTY!!\"\nYour eyes stare in horror while you start to slowly step back when you see more men on the top side of the mountains, They have got bows and arrows!..\n You see a small passageway through the cave, but you also see a small opening underneath the freshwater lake.. \nyou see seagulls on the other side of the mountains and before those seagulls you see your death\n\n")



		c305 = int(input("----1.Run towards the cave opening \n\n----2.Dive underwater and swim into the underwater Cave opening\n\n----3.Try to bribe the cannibals with all you money\n\nYour Choice:"))
		if (c305 ==1 ):#dead
			printf("\n\nYou run towards a small cave opening which you think will lead you further ahead, you are frantic and LITERALLY RUNNING FOR YOUR LIFE\nThe cave is a dead end, you bolt out of the cave and start running away from the men you keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
			time.sleep(5)
			End(0)
			input()
		elif(c305 == 2):
			printf("\n\nYou take a deep breath and dive into the lake and swim towards the small opening, it is small but you squeeze through it\nyou are now in a larger waterbody (you guessed that there might be a larger lake by seeing those seagulls)\nyou swim frantically to the top of the ocean until your last breath\nyou are about to passout when you finally reach the surface\nYou See a Beach in a long distance, it looks like a village or a small town\nDifferent from the one you saw before\nyou start swimming towards land, after reaching you are totally exhausted and lay on the beach lifeless\n")
			time.sleep(5)
			printf("\nyou wake up in a room, looks like a sickbay, you get up and thank the people who helped you\nYou ask if they have your clothes and weapons, they say that they would give it\nbut they had a favour to ask... they heard about how you came through that passageway,\nThey figured that you had escaped from the cannibals..They want you to help them in stopping \nthe Evil king IDOM from taking away their cattle forcibly and that his men come during the night to take away their\ngoods,cattle and whatever money they could find..You tell them that you need time to think and make a strategy..\nAfter an hour of brainstorming and a full night's sleep you come to these conclusions:\n\n")
			strategy()
						
		elif(c305 == 3):#dead
			printf("You try to bribe them with 100 gold coins, The men from the top of the mountain start raining down arrows\nYou start running as you keep running you keep getting hit by arrows\nOne on the shoulder, another on the arm, the men are running on the mountains behind you, you hide behind a rock\n you heal your wounds, you quickly break and remove the arrows from your arm and shoulder \nand tear a part of you clothing and make a bandage applying the ancient elixir to your wounds, during which the arrows are continuously hitting the rock\nsuddenly at once The arrows stop.. you peek over the rock, no one is there, behind you is a whole swarm of cannibals\n\n")
			time.sleep(5)
			End(0)
			input()
elif (menu == 2):#exit the game
	os.system('cls')
	