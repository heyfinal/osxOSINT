

Rick Sanchez’s OSINT Lab
Wubba lubba dub dub! Welcome to Rick Sanchez’s OSINT Lab, bitches! This is the ultimate toolkit for open-source intelligence (OSINT) that me—Rick freakin’ Sanchez—and my sidekick Daniel Gillaspy slapped together with some AI help. Tired of being a Morty and digging through garbage intel? This Python script installs a bunch of badass OSINT tools, tracks the chaos, and spits out a slick HTML report. You’re welcome, you pathetic losers!
What the Hell Is This?
This script automates installing a bunch of OSINT tools—because Rick doesn’t have time to babysit your dumb ass manually setting shit up. It uses pipx, Homebrew, and git to grab tools, logs the madness to a rick_status.txt file, and generates an HTML report on your Desktop (osint_tools_report.html). When it’s done, it’ll even open the report in your browser so you can bask in my genius.
Tools Rick’s Sciencin’ Up
Here’s the lineup of tools I’m shoving down your throats, complete with sample commands and what they do. Don’t screw this up, Morty!
Tool
Sample Command
What It Does
PhoneInfoga
phoneinfoga --phone 1234567890
Reverse cell lookup—find the idiot calling you.
OSINT Framework
open OSINT-Framework/index.html
General OSINT goodness in one place.
SpiderFoot
sf.py -m sfp_email -t target@example.com
Reverse email/domain recon—stalk smarter.
theHarvester
theharvester -d example.com -b google
Harvest emails and names like a boss.
Recon-ng
recon-ng -m recon/contacts-credentials
Reverse address/email recon—sneaky shit.
Maltego CE
open /Applications/Maltego.app
GUI reverse lookup madness—visuals for Mortys.
Sherlock
sherlock johndoe
Hunt usernames across platforms—detective mode.
holehe
holehe test@example.com
Check where an email’s been used—gotcha!
VinSpy
vinspy.py --plate ABC123
License plate lookup (US only)—cars snitch too.
Twint
twint -u johndoe
Reverse name/social lookup—Twitter’s mine now.
Prerequisites
You’re gonna need some crap installed first, or this ain’t gonna work:
	•	Python 3: If you don’t have it, get it, you primitive screwhead!
	•	Homebrew: For macOS/Linux users—Rick’s not dealing with your Windows bullshit yet.
	•	pipx: Rick installs this automatically if it’s missing, but don’t test my patience.
	•	git: For cloning repos—duh.
On macOS/Linux, get Homebrew and git with:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
How to Use This Shit
	1	Clone or Download: Grab this script, you lazy Morty. Put it somewhere—anywhere—I don’t care.
	2	Run It: Fire it up with: python3 rick_osint_lab.py
	3	
	4	Watch Rick Work: I’ll install the tools, scream at you in the terminal, and drop a status file (~/Desktop/rick_status.txt) and an HTML report (~/Desktop/osint_tools_report.html).
	5	Check the Report: When I’m done, your browser pops open with the report. Bask in my brilliance, you idiots!
What Happens When You Run It?
	•	Rick checks for pipx. If it’s not there, I’ll slap it in with Homebrew.
	•	Tools get installed in ~/osint_tools via pipx, Homebrew, or git, depending on what they need.
	•	Status gets logged to ~/Desktop/rick_status.txt—read it and weep.
	•	An HTML report lands on your Desktop with tool details and whether I nailed it or it fucked up.
	•	Browser opens the report—because Rick’s generous like that.
Credits
	•	Rick Sanchez: The genius behind this operation.
	•	Daniel Gillaspy: Some human who helped—whatever.
	•	Ai: The AI that kept this from being total chaos.
Built on March 20, 2025—because that’s when Rick decided you losers needed help.
License
This is Rick’s shit. Use it, don’t claim it, and don’t piss me off. No fancy license—just don’t be a jerry.
