# DiscordBot
Simple bot for youtube videos and various

Discord Python Bot Start
Prerequesites:
	Python 3.8 or higher

Installation:
	*Note: I encorage first read all the installation instructions before starting to follow them, they are some
	important things to take on consideration.
	
	Depending the SO you can follow these steps:
		Linux:
			Regular text support you can get the library from PyPI:
				python3 -m pip install -U discord.py
			Voice support you should use *discord.py[voice]* insted of *discord.py*
				python3 -m pip install -U discord.py[voice]
				
				*NOTE: requisit voice
					On Linux environments, installing voice requires getting the following dependencies:
						libffi
						libnacl
						python3-dev
					For Debian-based system you can use the following command:
						apt install libffi-dev libnacl-dev python3-dev
				
			*Note: Virtual Environments (OPTIONAL)
				Sometimes you want use a different version of libraries than the ones installed on the system
				A more in-depth tutorial is found on *Virtual Environments and Packages*.
			
				Quick and easy steps are:
					Go to your project’s working directory:
						$ cd your-bot-source
						$ python3 -m venv bot-env
					Activate the virtual environment:
						$ source bot-env/bin/activate
					Then you can use pip as usual:
						$ pip install -U discord.py
					
			
		Windows:
			Regular text support you can get it using the following command:
				py -3 -m pip install -U discord.py
			Voice support you should use *discord.py[voice]* insted of *discord.py*
				py -3 -m pip install -U discord.py[voice]
			
			*Note: Virtual Environments (OPTIONAL)
				Sometimes you want use a different version of libraries than the ones installed on the system
				A more in-depth tutorial is found on *Virtual Environments and Packages*.
			
				Quick and easy steps are:
					Go to your project’s working directory:
						$ cd your-bot-source
						$ python3 -m venv bot-env
					Activate the virtual environment:
						$ bot-env\Scripts\activate.bat
					Then you can use pip as usual:
						$ pip install -U discord.py
	
	*Extra Note: discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. 
		It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. 
		If this is not possible, then consider disabling the privileged intents instead.
			Go to https://discord.com/developers/applications
			Navigate to your application
			to the Bot section
			Scroll down and enable SERVER MEMBERS INTENT


	
	
	
	
	
	
	
DOCUMENTATION URL CONSULTED:
	- https://discordpy.readthedocs.io/en/stable/#getting-started
		* Prerequesites and installations: https://discordpy.readthedocs.io/en/stable/intro.html#installing
			* Virtual Environments and packages: https://docs.python.org/3/tutorial/venv.html
		* https://discordpy.readthedocs.io/en/stable/quickstart.html
		* Documentation: https://discordpy.readthedocs.io/en/stable/api.html