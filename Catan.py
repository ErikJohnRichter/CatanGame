import CatanDefs
import os
import cmd

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

# Main Program
if __name__ == '__main__':
	cls()
	print 'Welcome to Catan!'
	print ''
	CatanDefs.hexName(CatanDefs.location)
	CatanDefs.explore().cmdloop()
	print 'Fare Thee Well!'
