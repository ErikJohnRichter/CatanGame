import CatanDefs
import os
import cmd

# Main Program
if __name__ == '__main__':
	CatanDefs.cls()
	print ''
	print '            --Welcome to the Island of Catan!--'
	print ''
	print ''
	print '     Use text commands to explore this beautiful place!'
	print '             There is adventure at every step!'
	print ''
	print '     Be mindful, though, as there are also many things'
	print '           here that could harm or even kill you.'
	print ''
	print '       If you get lost, remember to consult your map.'
	print ''
	print ''
	print ''
	print '                     In Catanian Lore,'
	print '    it is rumored whoever possesses the Magic of Catan'
	print '               will be Lord of the island.'
	print ''
	print ''
	print '                        Good Luck!'
	print ''
	print ''
	raw_input('>Press enter to continue...')
	CatanDefs.cls()
	CatanDefs.hexName(CatanDefs.location)
	CatanDefs.explore().cmdloop()
	print 'Fare Thee Well!'
