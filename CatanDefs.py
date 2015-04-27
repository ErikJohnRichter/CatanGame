Description = 'Description'
North = 'north'
South = 'south'
East = 'east'
West = 'west'
Port = 'port'
Lighthouse = 'lighthouse'
Ground = 'ground'
Desc = 'desc'
Name = 'name'
Inventory = 'inventory'
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
		Ground: ['Ore']},
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
		North: 'Dense Fog',
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
	'Dense Fog': {
		Description: 'You just discovered a secret island hidden by the fog!',
		South: 'North Sea of Catan',
		Ground: ['Gold']},
	'Fog' : {
		Description: 'You just entered a dense patch of fog.',
		Lighthouse: 'Sea of Catan',
		Ground: ['Nothing']},
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
	}

# Default Location and Inventory
location = 'Catanian Desert'
inventory = ['Map']
showExits = True

import cmd, textwrap, os

def hexName(loc):
	# Hex Name
	print '-' * (len(loc)+4)
	print '|',(loc),'|'
	print '-' * (len(loc)+4)

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
	for direction in (North, South, East, West, Port):
		if direction in hexes[loc].keys():
			exit.append(direction.title())
	print''
	if showExits:
		for direction in (North, South, East, West, Port):
			if direction in hexes[location]:
				print'%s: %s' % (direction.title(), hexes[location][direction])
	else:
		print 'Exits: %s' % ' '.join(exits)

def moveDirection(direction):
	# Moves Traveler
	global location

	if direction in hexes[location]:
		os.system('cls')
		os.system('clear')
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

	# Allows for Caps or Lower
	do_North = do_north
	do_South = do_south
	do_East = do_east
	do_West = do_west
	do_Port = do_port
	do_Lighthouse = do_lighthouse

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

	# Pick something up off the ground
	def do_take(self, arg):

		itemToTake = arg.lower()

		if itemToTake == '':
			print 'Take what?'
			return

		cantTake = False

		# Need Paddle before picking up boat
		if 'Paddle' in inventory:
			resources['Boat']['Takeable'] = True
			for item in getAllItems(itemToTake, hexes[location][Ground]):
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