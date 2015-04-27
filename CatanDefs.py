Description = 'Description'
North = 'north'
South = 'south'
East = 'east'
West = 'west'
Port = 'port'
Lighthouse = 'lighthouse'
Ground = 'ground'
Down = 'down'
Up = 'up'
Desc = 'desc'
Name = 'name'
Inventory = 'inventory'
Map = 'Map'
Takeable = 'takeable'
Word = 'word'

# Dictionary for Terrain Hexes
hexes = {
	'Catanian Desert': {
		Description: 'Hot and parched, you wander for days. What is that figure on the horizon?',
	    North: 'Great Northern Mountains',
		East: 'Forest',
		South: 'Pastureland',
		West: 'Wheat Fields',
		Ground: ['Carcass']},
	'Great Northern Mountains': {
		Description: '-The wind howls- You cower at the beautiful majesty before you.',
		East: 'Ore Mines',
		South: 'Catanian Desert',
		West: 'City of Northumberland',
		Ground: ['Nothing']},
	'City of Northumberland': {
		Description: '-a bell tower tolls the hour- This city is a beauty of human ingenuity.',
		East: 'Great Northern Mountains',
		South: 'Wheat Fields',
		Port: 'Sea of Catan',
		Ground: ['Boat']},
	'Ore Mines': {
		Description: 'Deep in the Earth, cold, dank air wafts upward. Angry dwarves are known to inhabit these dark halls.',
		South: 'Forest',
		West: 'Great Northern Mountains',
		Down: 'Mine Cavern',
		Ground: ['Ore']},
	'Mine Cavern': {
		Description: 'It is said the mining dwarves hold the Magic of Catan.',
		Up: 'Ore Mines',
		Ground: ['Box']},
	'Wheat Fields': {
		Description: '-soft, warm sun shines down- The wheat waves in the wind before you. You are tempted to frolick.',
		North: 'City of Northumberland',
		East: 'Catanian Desert',
		South: 'Settlement',
		Ground: ['Wheat']},
	'Forest': {
		Description: 'Night falls. It is rumored these woods are haunted.',
		North: 'Ore Mines',
		South: 'Brick Factory',
		West: 'Catanian Desert',
		Ground: ['Wood']},
	'Pastureland': {
		Description: 'A beautiful sea of green grass. Far on the hill, a shepherd rounds up his flock.',
		North: 'Catanian Desert',
		East: 'Brick Factory',
		West: 'Settlement',
		Ground: ['Sheep']},
	'Settlement': {
		Description: 'Once pastureland, the Earth gave way to this budding hamlet.',
		North: 'Wheat Fields',
		East: 'Pastureland',
		Ground: ['Paddle']},
	'Brick Factory': {
		Description: 'Workers toil in the hot sun. A settlement is seen in the far distance.',
		North: 'Forest',
		West: 'Pastureland',
		Ground: ['Brick']},
	'Sea of Catan': {
		Description: 'You just entered the sea!',
		North: 'North Sea of Catan',
		South: 'City of Northumberland',
		East: 'East Sea of Catan',
		West: 'West Sea of Catan',
		Ground: ['Water']},
	'North Sea of Catan': {
		Description: 'A true sailor!',
		North: 'Fog',
		South: 'Sea of Catan',
		East: 'Fog',
		West: 'Fog',
		Ground: ['Water']},
	'West Sea of Catan': {
		Description: 'A true sailor',
		North: 'Fog',
		South: 'Fog',
		East: 'Sea of Catan',
		West: 'Fog',
		Ground: ['Water']},
	'East Sea of Catan': {
		Description: 'A true sailor',
		North: 'Fog',
		South: 'Fog',
		East: 'Fog',
		West: 'Sea of Catan',
		Ground: ['Water']},
	'Dense Fog ': {
		Description: '|-- You just discovered a island hidden in the fog! --|',
		North: 'Fog',
		South: 'Fog',
		East: 'Fog',
		West: 'Fog',
		Ground: ['Key']},
	'Fog': {
		Description: 'You just entered a dense patch of fog.',
		Lighthouse: 'Sea of Catan',
		North: 'More Fog',
		South: 'More Fog',
		East: 'More Fog',
		West: 'More Fog',
		Ground: ['Fog']},
	'More Fog': {
		Description: 'You are lost in the fog! \nYou need to look for something to guide you back! \nBe careful for terrain...rocky islands were rumored to be in this area.',
		Lighthouse: 'Sea of Catan',
		North: 'Dense Fog ',
		South: 'Dense Fog',
		East: 'Dense Fog',
		West: 'Dense Fog',
		Ground: ['Fog']},
	'Dense Fog': {
		Description: '',
		Ground: ['Fog']},
	}

# Dictionary for Terrain Resources
resources = {
	'Boat': {
		Name: 'a Row Boat',
		Desc: 'Use this to travel the seas...but what good is a boat without a paddle?',
		Takeable: False,
		Word: ['boat']},
	'Paddle': {
		Name: 'a Paddle',
		Desc: 'You found a paddle! Take it, now, and go find a boat!',
		Word: ['paddle']},
	'Carcass': {
		Name: 'a Carcass',
		Desc: 'Whatever this was, it didn\'t survive here. You probably won\'t either.',
		Word: ['carcass']},
	'Brick': {
		Name: 'a Brick',
		Desc: 'Sun and Earth. Use these to build.',
		Word: ['brick']},
	'Ore': {
		Name: 'a Chunk of Ore',
		Desc: 'Forged deep in the Earth, Ore is used to make tools...and weapons.',
		Word: ['ore']},
	'Box': {
		Name: 'a Locked Box',
		Desc: 'This box appears to need a key to open it.',
		Takeable: False,
		Word: ['box']},
	'Wheat': {
		Name: 'a Shaff of Wheat',
		Desc: 'Born of the land to feed your hunger',
		Word: ['wheat']},
	'Wood': {
		Name: 'a Pile of Wood',
		Desc: 'Wood is versatile. Use it to build, cook, or fight.',
		Word: ['wood']},
	'Sheep': {
		Name: 'a Lost Sheep',
		Desc: 'Used it for wool or food. Sheep are valuable resources.',
		Word: ['sheep', 'lost sheep']},
	'Key': {
		Name: 'an old rusty key',
		Desc: ' ',
		Word: ['key']},
	'Gold': {
		Name: 'a Gold Coin',
		Desc: 'This is currency of the land. Beware...others value it just as much as you!',
		Word: ['gold', 'gold coin']},
	'Map': {
		Name: 'a Map',
		Desc: 'This is a map of Catan',
		Word: ['map']},
	'Sword': {
		Name: 'a Sword',
		Desc: 'A simple form of protection. Take this to be safe.',
		Word: ['sword']},
	'Nothing': {
		Name: 'Nothing',
		Desc: 'Travel to another region of Catan to find more items.',
		Word: ['nothing']},
	'Water': {
		Name: 'Water',
		Desc: 'Actually, there is water everywhere!',
		Word: ['water']},
	'Fog': {
		Name: 'Fog',
		Desc: 'There is fog everywhere! \nYou better find something to help you!',
		Word: ['fog']},
	}

# Default Location and Inventory
location = 'Catanian Desert'
inventory = ['Map']
showExits = True

import cmd, textwrap, os

def cls():
	# Clears Screen
    os.system(['clear','cls'][os.name == 'nt'])

def hexName(loc):
	# Hex Name
	if location == 'Dense Fog':
		for each in range (30):
			print ''
		print '   You wandered, lost, in the fog for days.'
		print ''
		print '          You just died of thirst.'
		print ''
		for each in range (10):
			print ''
		quit()
	else:
		print ''
		print '-' * (len(loc)+4)
		print '|',' '* (len(loc)),'|'
		print '|',(loc),'|'
		print '|',' '* (len(loc)),'|'
		print '-' * (len(loc)+4)
		print ''

		# Hex Description
		print '\n'.join(textwrap.wrap(hexes[loc][Description]))

		if len(hexes[loc][Ground]) > 0:
			print ''
			for item in hexes[loc][Ground]:
				print "There is", resources[item][Name], "on the ground."
				print resources[item][Desc]
		else:
			print ''
	
	# Surrounding Hexes
	exit = []
	for direction in (North, South, East, West, Port, Down, Up):
		if direction in hexes[loc].keys():
			exit.append(direction.title())
	print''
	if showExits:
		for direction in (North, South, East, West, Port, Down, Up):
			if direction in hexes[location]:
				print'%s: %s' % (direction.title(), hexes[location][direction])
	else:
		print 'Exits: %s' % ' '.join(exits)

def moveDirection(direction):
	# Moves Traveler
	global location

	if direction in hexes[location]:
		cls()
		print 'You traveled to the %s.' % direction
		location = hexes[location][direction]
		hexName(location)
	else:
		print 'You need to enter or exit the seas through a port.'

def getAllWords(itemList):
	# Returns Inventory Description for each item
	itemList = list(set(itemList))
	descWords = []
	for item in itemList:
		descWords.extend(resources[item][Word])
	return list(set(descWords))

def getAllFirstWords(itemList):

	itemList = list(set(itemList))
	descWords = []
	for item in itemList:
		descWords.append(resources[item][Word][0])
	return list(set(descWords))

def getFirstItems(word, itemList):
	# Gets one item on the ground
	itemList = list(set(itemList))
	for item in itemList:
		if word in resources[item][Word]:
			return item
	return None

def getAllItems(word, itemList):
	# Gets all items on the ground
	itemList = list(set(itemList))
	matchingItems = []
	for item in itemList:
		if word in resources[item][Word]:
			matchingItems.append(item)
	return matchingItems

class explore(cmd.Cmd):
	# Class of functions for movement and interaction.
	prompt = '\nWhat would you like to do?\n> '

	def default(self, arg):
		print 'Sorry, that word is not understood in Catan.'

	def do_quit(self, arg):
		return True

	# Movement Functions
	def do_north(self, arg):
		moveDirection('north')

	def do_south(self, arg):
		moveDirection('south')

	def do_east(self, arg):
		moveDirection('east')

	def do_west(self, arg):
		moveDirection('west')

	def do_lighthouse(self, arg):
		moveDirection('lighthouse')

	def do_port(self, arg):
		if 'Boat' in inventory:
			moveDirection('port')
		else:
			print 'You need a boat to enter the seas.'

	def do_down(self, arg):
		moveDirection('down')

	def do_up(self, arg):
		moveDirection('up')

	# Allows for Caps or Lower
	do_North = do_north
	do_South = do_south
	do_East = do_east
	do_West = do_west
	do_Port = do_port
	do_Lighthouse = do_lighthouse
	do_Down = do_down
	do_Up = do_up

	# View Inventory
	def do_inventory(self, arg):
		if len(inventory) == 0:
			print 'Inventory:\n  (nothing)'
			return

		itemCount = {}
		for item in inventory:
			if item in itemCount.keys():
				itemCount[item] += 1
			else:
				itemCount[item] = 1

		print('Inventory:')
		for item in set(inventory):
			if itemCount[item] > 1:
				print '  %s (%s)' % (item, itemCount[item])
			else:
				print '  ' + item

	do_inv = do_inventory

	# View Map
	def do_map(self, arg):
		if 'Map' in inventory:
			cls()
			print hexName(location)
			print '                                          '
			print '              --MAP of CATAN--               N'
			print '    Port                                     ^'
			print '  ---||-----------------------------------   |'
			print '  |            |            |            |'
			print '  |  City of   |   North    |    Ore     |'
			print '  |    the     |  Mountain  |   Mines    |'
			print '  |   North    |            |            |'
			print '  |            |            |            |'
			print '  ----------------------------------------'
			print '  |            |            |            |'
			print '  |   Wheat    |  Catanian  |    Dark    |'
			print '  |   Field    |   Desert   |   Forest   |'
			print '  |            |            |            |'
			print '  |            |            |            |'
			print '  ----------------------------------------'
			print '  |            |            |            |'
			print '  |            |            |   Brick    |'
			print '  | Settlement |  Pastures  |  Factory   |'
			print '  |            |            |            |'
			print '  |            |            |            |'
			print '  ----------------------------------------'
			print '  --> You are in the %s' % location
			print '                                          '

		else:
			print 'You do not have a map.'

	do_Map = do_map

	# Unlock Box
	def do_unlock(self, arg):
		if 'Box' in inventory:
			for each in range (30):
				print ''
			print '           ********************************'
			print '                                           '
			print '                   You now possess         '
			print '                         the               '
			print '                   MAGIC of CATAN!         '
			print '                                           '
			print '           ********************************'
			print ''
			print '   Whoever possesses this magic is Lord of the Land.'
			print ''
			print '                --VICTORY is YOURS!--       '
			for each in range (10):
				print ''
			quit()
		else:
			print 'You do not have a box to unlock.'

	do_Unlock = do_unlock

	# Pick something up off the ground
	def do_take(self, arg):

		itemToTake = arg.lower()

		if itemToTake == '':
			print 'Take what?'
			return

		if itemToTake == 'carcass':
			for each in range (30):
				print ''
			print '   Why would you pick up a rotting carcass?'
			print ''
			print '        You just died of listeriosis.'
			print ''
			print '              == Darwin Award =='
			for each in range (10):
				print ''
			quit()
			

		cantTake = False

		# Need Paddle/Key before picking up boat/box
		if 'Paddle' in inventory:
			resources['Boat']['Takeable'] = True
			if 'Key' in inventory:
				resources['Box']['Takeable'] = True
				for item in getAllItems(itemToTake, hexes[location][Ground]):
					print 'You take %s.' % (resources[item][Name])
					hexes[location][Ground].remove(item)
					inventory.append(item)
					return
			else:
				for item in getAllItems(itemToTake, hexes[location][Ground]):
					print 'You take %s.' % (resources[item][Name])
					hexes[location][Ground].remove(item)
					inventory.append(item)
					return
		else:
			if 'Key' in inventory:
				resources['Box']['Takeable'] = True
				for item in getAllItems(itemToTake, hexes[location][Ground]):
					if resources[item].get(Takeable, True) == False:
						cantTake = True
						continue
					print 'You take %s.' % (resources[item][Name])
					hexes[location][Ground].remove(item)
					inventory.append(item)
					return
			else:
				for item in getAllItems(itemToTake, hexes[location][Ground]):
					if resources[item].get(Takeable, True) == False:
						cantTake = True
						continue
					print 'You take %s.' % (resources[item][Name])
					hexes[location][Ground].remove(item)
					inventory.append(item)
					return

		if cantTake:
			print 'You cannot take this now.'
		else:
			print 'That is not on the ground.'

	def do_drop(self, arg):
		# Drop An Item
		itemToDrop = arg.lower()

		invDescWords = getAllWords(inventory)

		if itemToDrop not in invDescWords:
			print 'What would you like to drop?'
			return

		item = getFirstItems(itemToDrop, inventory)
		if item != None:
			print 'You drop %s.' % (resources[item][Name])
			inventory.remove(item)
			hexes[location][Ground].append(item)