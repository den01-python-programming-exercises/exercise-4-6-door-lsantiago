class Door:
	def __init__(self):
		pass
	
	def knock(self):
		return "Who's there?"

def main():
	alexander = Door()
	print(alexander.knock())
	print(alexander.knock())

if __name__ == '__main__':
	main()
