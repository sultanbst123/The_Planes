import random
import pygame

width = 1340
height = 670
blue = ((51,153,255))#light blue
red = ((255,0,0))#red

#player sprite
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player,self).__init__()
		self.image = []
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Player/Plane1.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Player/Plane2.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Player/Plane3.png").convert_alpha())
		
		self.image = [pygame.transform.smoothscale(x,(120,80)) for x in self.image]
			
		self.index = 0
		
		self.surf = self.image[self.index]
		
		self.rect = self.surf.get_rect()
		#hover button
		self.hover1 = False
		self.hover2 = False
		self.hover3 = False
		self.hover4 = False
		
	#move up	
	def atas(self):
		self.rect.move_ip(0,-3)
		
	#move down
	def bawah(self):
		self.rect.move_ip(0,3)
		
	#move right	
	def kanan(self):
		self.rect.move_ip(3,0)
	
	#nove left
	def kiri(self):
		self.rect.move_ip(-3,0)
		
		
	#control android //////
	#move left (android)
	def kiri1(self):
		img_hover = pygame.image.load("/storage/emulated/0/Pesawat/Control/Kiri_hover.png").convert_alpha()
		img = pygame.image.load("/storage/emulated/0/Pesawat/Control/Kiri.png").convert_alpha()
		
		if self.hover1:
			rect = img_hover.get_rect()
			rect.center=(90,570)
			screen.blit(img_hover,rect)
		else:
			rect = img.get_rect()
			rect.center=(90,570)
			screen.blit(img,rect)
		return rect
	
	#move up (android)
	def atas1(self):
		img_hover = pygame.image.load("/storage/emulated/0/Pesawat/Control/Atas_hover.png").convert_alpha()
		img = pygame.image.load("/storage/emulated/0/Pesawat/Control/Atas.png").convert_alpha()
		
		if self.hover2:
			rect = img_hover.get_rect()
			rect.center=(190,470)
			screen.blit(img_hover,rect)
		else:
			rect = img.get_rect()
			rect.center=(190,470)
			screen.blit(img,rect)
		return rect
	
	#move right (android)	
	def kanan1(self):
		img_hover = pygame.image.load("/storage/emulated/0/Pesawat/Control/Kanan_hover.png").convert_alpha()
		img = pygame.image.load("/storage/emulated/0/Pesawat/Control/Kanan.png").convert_alpha()
		
		if self.hover3:
			rect = img_hover.get_rect()
			rect.center=(290,570)
			screen.blit(img_hover,rect)
		else:
			rect = img.get_rect()
			rect.center=(290,570)
			screen.blit(img,rect)
		return rect
	
	#move down(android)	
	def bawah1(self):
		img_hover = pygame.image.load("/storage/emulated/0/Pesawat/Control/Bawah_hover.png").convert_alpha()
		img = pygame.image.load("/storage/emulated/0/Pesawat/Control/Bawah.png").convert_alpha()
		
		if self.hover4:
			rect = img_hover.get_rect()
			rect.center=(190,570)
			screen.blit(img_hover,rect)
		else:
			rect = img.get_rect()
			rect.center=(190,570)
			screen.blit(img,rect)
		return rect
		
	#update player		
	def update(self):
		#update animation
		self.index += 1
		if self.index >= len(self.image):
			self.index = 0
		self.surf = self.image[self.index]
		
		#kotak kiri kanan (tetap di screen)	
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > width:
			self.rect.right = width
		#kotak atas bawah (tetap di screen)	
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= height:
			self.rect.bottom = height

#musuh sprite
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy,self).__init__()
		self.image = []
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Enemy/torpedo_2.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Enemy/torpedo.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Enemy/torpedo_2_2.png").convert_alpha())
		
		self.image = [pygame.transform.smoothscale(x,(60,20))for x in self.image]
		
		self.index = 0
		
		self.surf = self.image[self.index]
				
		self.rect = self.surf.get_rect(center = 
		(random.randint(width+20,width+100),
		random.randint(0,450),
		))
		#speed enemy
		self.speed = random.randint(6,8)
		
	#enemy update 	
	def update(self):
		#update animation
		self.index += 1
		if self.index >= len(self.image):
			self.index = 0
		self.surf = self.image[self.index]
		
		#enemy from right
		self.rect.move_ip(-self.speed,0)
		if self.rect.right < 0:
			self.kill()

#awan sprite
class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super(Cloud,self).__init__()
		self.surf = pygame.image.load("/storage/emulated/0/Pesawat/Cloud/cloud.png").convert()
		self.surf.set_colorkey((0,0,0),pygame.RLEACCEL)
		
		self.rect = self.surf.get_rect(center = 
		(random.randint(width + 20,width + 100),
		random.randint(0,450),))
	
	#update cloud
	def update(self):
		self.rect.move_ip(-5,0)
		if self.rect.right < 0:
			self.kill()

#coin sprite			
class Coin(pygame.sprite.Sprite):
	def __init__(self):
		super(Coin,self).__init__()
		self.image = []
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin0.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin1.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin2.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin3.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin4.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin5.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin6.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin7.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin8.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin9.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin10.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin11.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin12.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin13.png").convert_alpha())
		self.image.append(pygame.image.load("/storage/emulated/0/Pesawat/Coins/Coin14.png").convert_alpha())
		
		self.image = [pygame.transform.smoothscale(x,(100,100))for x in self.image]
		
		self.index = 0
		
		self.surf = self.image[self.index]
		
		#random possition
		self.rect = self.surf.get_rect(center = 
		(random.randint(width + 20,width + 100),
		random.randint(0,450),))
		
	#update coin
	def update(self):
		#update animation coin
		self.index += 1
		if self.index >= len(self.image):
			self.index = 0
		self.surf = self.image[self.index]
		
		#coin from right
		self.rect.move_ip(-5,0)
		if self.rect.right < 0:
			self.kill()

#font function		
def text_object(text,font):
	textsurface = font.render(text,True,(255,255,255))
	return textsurface,textsurface.get_rect()

#game exit			
def keluar():
	pygame.quit()
	quit()
			
#button function			
def button(msg,x,y,w,h,ic,ac,action=None):
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	#font local
	font = pygame.font.Font("/storage/emulated/0/Pesawat/Fonts/ShortBaby.ttf",30)
	
	#hover effect
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen,ac,(x,y,w,h),5,10)
		if click[0] == 1 and action != None:
			intro_sound.stop()
			action()
	else:
		pygame.draw.rect(screen,ic,(x,y,w,h),0,10)
		
	textsurf,textrect = text_object(msg,font)
	textrect.center = ((x+(w/2)),(y+(h/2)))
	screen.blit(textsurf,textrect)

#game over
def gameover():
	#font local
	font = pygame.font.Font("/storage/emulated/0/Pesawat/Fonts/ShortBaby.ttf",70)
	
	#print gameover
	textsurf,textrect = text_object("GameOver",font)
	textrect.center = ((width/2),(250))
	
	#print score
	scoresurf,scorerect = text_object("Your Score " + str(value),font)
	scorerect.center = ((width/2),350)
	
	#backgroun background
	img = pygame.image.load("/storage/emulated/0/Pesawat/Background/Gameover_panel.png").convert_alpha()
	img = pygame.transform.scale(img,(600,400))
	img_rect = img.get_rect()
	img_rect.center = ((width/2,height/2))
	
	#title The plane
	back = pygame.image.load("/storage/emulated/0/Pesawat/Background/title_panel.png").convert_alpha()
	back = pygame.transform.scale(back,(600,80))
	back_rect = back.get_rect()
	back_rect.center=(width/2,100)
	screen.blit(back,back_rect)
	
	#print the plane
	font = font.render("The Planes",True,(255,255,255))
	font_rect = font.get_rect()
	font_rect.center = (width/2,110)
	
	#loop game over
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		#print all		
		screen.blit(img,img_rect)
		screen.blit(back,back_rect)
		screen.blit(font,font_rect)
		screen.blit(textsurf,textrect)
		screen.blit(scoresurf,scorerect)
		button("Quit",590,400,150,50,red,red,keluar)
		
		#update
		pygame.display.update()
		clock.tick(15)
		
#game intro
def game_intro():
	#font local
	title = pygame.font.Font("/storage/emulated/0/Pesawat/Fonts/ShortBaby.ttf",60)
	intro_sound.play()
	#loop game intro
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		#background intro		
		screen.blit(background,(0,0))
		
		#background title
		back = pygame.image.load("/storage/emulated/0/Pesawat/Background/title_panel.png").convert_alpha()
		back = pygame.transform.scale(back,(600,100))
		back_rect = back.get_rect()
		back_rect.center=(width/2,100)
		screen.blit(back,back_rect)
		
		#title the plane
		font = title.render("The Planes",True,(255,255,255))
		font_rect = font.get_rect()
		font_rect.center = (width/2,110)
		screen.blit(font,font_rect)
		
		#button start
		button("Start",500,250,100,50,blue,blue,main)
		#button quit
		button("Quit",750,250,100,50,red,red,keluar
		)
		#update
		pygame.display.update()
		clock.tick(15)		

#show counter score
value = 0		
def show_score(x,y):
		font1 = pygame.font.Font("/storage/emulated/0/Pesawat/Fonts/ShortBaby.ttf",50)
		scores = font1.render("Score " + str(value),True,(255,255,255))
		screen.blit(scores,(x,y))
						
pygame.init()

clock = pygame.time.Clock()

#screen 1400x700
screen = pygame.display.set_mode((width,height))

#create a userevent to add class except class player
musuh = pygame.USEREVENT + 1
pygame.time.set_timer(musuh,random.randint(500,750))

awan = pygame.USEREVENT + 2
pygame.time.set_timer(awan,1000)

coin = pygame.USEREVENT + 3
pygame.time.set_timer(coin,random.randint(3000,7000))

#create a group sprite
player = Player()
musuh_musuh = pygame.sprite.Group()
awan_awan = pygame.sprite.Group()
coin_coin = pygame.sprite.Group()
semuanya = pygame.sprite.Group()
semuanya.add(player)

#music game
pygame.mixer.music.load("/storage/emulated/0/Pesawat/Music/Badguy.mp3")

#intro sound
intro_sound = pygame.mixer.Sound("/storage/emulated/0/Pesawat/Music/Intro.wav")

#coin sound
coin_sound = pygame.mixer.Sound("/storage/emulated/0/Pesawat/Effect/Coin.wav")

#collisio  sound
collision_sound = pygame.mixer.Sound("/storage/emulated/0/Pesawat/Effect/die.ogg")

#game over sound
gameover_sound = pygame.mixer.Sound("/storage/emulated/0/Pesawat/Music/Gameover.ogg")

#background game
background = pygame.image.load("/storage/emulated/0/Pesawat/Background/sky_background.png").convert_alpha()
background = pygame.transform.scale(background,(width,height))

intro_sound.set_volume(0.5)
coin_sound.set_volume(0.5)
gameover_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

key = pygame.key.get_pressed()

def main():
	direction = "down"
	run = True
	keys = pygame.key.get_pressed()
	
	pygame.mixer.music.play(loops=-1)
	
	global value
	
	while run:
	
		for event in pygame.event.get():
				#control for computer
			if event.type == pygame.KEYDOWN:
				if keys[pygame.K_w] or keys[pygame.K_UP]:
					player.atas()
					player.hover1 = False 
					player.hover2 = True
					player.hover3 = False
					player.hover4 = False
					
				if keys[pygame.K_s] or keys[pygame.K_DOWN]:
					player.bawah()
					player.hover1 = False
					player.hover2 = False
					player.hover3 = False
					player.hover4 = True
					
				if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
					player.kanan()
					player.hover1 = False
					player.hover2 = False
					player.hover3 = True
					player.hover4 = False
					
				if keys[pygame.K_a] or keys[pygame.K_LEFT]:
					player.kiri()
					player.hover1 = True
					player.hover2 = False
					player.hover3 = False
					player.hover4 = False		
					
				if event.key == pygame.K_ESCAPE:
					run = False
				
				
			elif event.type == pygame.QUIT:
				run = False
			#control to mobile	
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if player.atas1().collidepoint(mouse_pos):
					direction = "up"
					#hover2
					player.hover1 = False 
					player.hover2 = True
					player.hover3 = False
					player.hover4 = False
				
				if player.bawah1().collidepoint(mouse_pos):
					direction = "down"
					#hover4
					player.hover1 = False
					player.hover2 = False
					player.hover3 = False
					player.hover4 = True
				
				if player.kanan1().collidepoint(mouse_pos):
					direction = "right"
					#hover3
					player.hover1 = False
					player.hover2 = False
					player.hover3 = True
					player.hover4 = False
				
				if player.kiri1().collidepoint(mouse_pos):
					direction = "left"
					#hover1
					player.hover1 = True
					player.hover2 = False
					player.hover3 = False
					player.hover4 = False		
			
			elif event.type == musuh:
				musuh_baru = Enemy()
				musuh_musuh.add(musuh_baru)
				semuanya.add(musuh_baru)
			
			elif event.type == awan:
				awan_baru = Cloud()
				awan_awan.add(awan_baru)
				semuanya.add(awan_baru)
		
			elif event.type == coin:
				coin_baru = Coin()
				coin_coin.add(coin_baru)
				semuanya.add(coin_baru)
			
		if direction == "down":
			player.bawah()	
		elif direction == "up":
			player.atas()
		elif direction == "right":
			player.kanan()
		elif direction == "left":
			player.kiri()
		
		player.update()
			
#	keyo = pygame.key.get_pressed()		
#	player.update(keyo)
	
		musuh_musuh.update()
		awan_awan.update()
		coin_coin.update()
		screen.fill((255,255,255))
		screen.blit(background,(0,0))
		
		#print control android
		player.atas1()
		player.kiri1()
		player.kanan1()
		player.bawah1()
	
		#draw all sprite
		for entity in semuanya:
			screen.blit(entity.surf,entity.rect)
		
			#collision player and coin
		hit = pygame.sprite.spritecollide(player,coin_coin,True)
		if hit:
			coin_sound.play()
			value+= 1
		
		show_score(1100,10)
	
		#collision player and musuh	
		if pygame.sprite.spritecollideany(player,musuh_musuh):
			collision_sound.play()
			pygame.mixer.music.stop()
			gameover_sound.play()
			player.kill()
			gameover()
			run = False
			
		pygame.display.flip()
		#Fps 60
		clock.tick(60)

#end
game_intro()
main()
pygame.quit()
quit()