listOfPeople = []
listofInstruments = ["drums", "vocals", "guitar1", "guitar2", "bass", "keyboard1", "keyboard2"]

class person(object):
	def __init__(self, is_bd, is_wl, instruments, is_new = False):
		self.canBeBandDirector = is_bd
		self.canBeWorshipLeader = is_wl
		self.instruments = instruments #how do you wanna structure this?
		self.isNew = is_new

	def set_two_month_availability(self, calendar):
		self.calendar = 0

class worship(object):
	#this is the class for one worship session
	instrument1Player = "nil"
	instrument1 = "nil" 
	bandDirector = "nil"
	worsipLeader = "nil"
	def __init__(self, date):
		self.date = date
		#what data structure should date be in

	#getters and setters for performers
	def setInstrument1(self, person, instrument):
		if instrument in person.instruments:
			self.instrument1Player = person
			self.instrument1 = instrument
		else:
			print("error")

	def getInstrument1:
		print(instrument1Player, " playing ", instrument1)

	#repeat for the rest
	def checkready(self):
		if worshipLeader == "nil" || bandDirector = "nil":
			return False
		elseif instrument1 == nil:
			return False
		else:
			print ("abc bla bla")
			return True

class calendar(object):
	def __init__(self, num_weeks, start_date):
		pass 
		#need to figure a way to define all the slots
		#two sessions per week
		#each week's date is previous date + 7
		#we can use excel's date processor

def parseDate(date):
	return 0
	#converts date from excel to DDMMYYYY

jerroldSoh = person(False, False, ["drums", "vocals", "guitar1", "bass"], is_new = True) #skilled musician

