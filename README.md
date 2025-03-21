
# OSX OSINT Auto Installer

![OSINT Tools](https://img.shields.io/badge/OSINT-Tools-green)

Welcome to the OSX OSINT Auto Installer! This script is designed to automatically install and configure a suite of OSINT (Open-Source Intelligence) tools on macOS. Built with a touch of Rick Sanchez's genius, this script will have your OSINT tools up and running in no time.

## Table of Contents
- [Features](#features)
- [Tools Installed](#tools-installed)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Automated installation of popular OSINT tools.
- Generates an HTML report of the installed tools.
- Provides example commands for each tool.

## Tools Installed

| Tool            | Description                      | Command Example                           | Source                                          |
|-----------------|----------------------------------|-------------------------------------------|-------------------------------------------------|
| PhoneInfoga     | Reverse cell lookup              | `phoneinfoga --phone 1234567890`          | [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) 
| OSINT Framework | General OSINT goodness           | `open OSINT-Framework/index.html`         | [OSINT Framework](https://github.com/lockfale/OSINT-Framework) 
| SpiderFoot      | Reverse email/domain recon       | `sf.py -m sfp_email -t target@example.com`| [SpiderFoot](https://github.com/smicallef/spiderfoot) 
| theHarvester    | Email/name harvesting            | `theharvester -d example.com -b google`   | [theHarvester](https://github.com/laramies/theHarvester) 
| Recon-ng        | Reverse address/email recon      | `recon-ng -m recon/contacts-credentials`  | [Recon-ng](https://github.com/lanmaster53/recon-ng) 
| Maltego CE      | GUI reverse lookup madness       | `open /Applications/Maltego.app`          | [Maltego](https://www.maltego.com/downloads/)    
| Sherlock        | Reverse name/username hunt       | `sherlock johndoe`                        | [Sherlock](https://github.com/sherlock-project/sherlock) 
| holehe          | Reverse email checker            | `holehe test@example.com`                 | [holehe](https://github.com/megadose/holehe)     
| VinSpy          | License plate lookup (US only)   | `vinspy.py --plate ABC123`                | [VinSpy](https://github.com/vinspy/vinspy)       
| Twint           | Reverse name/social lookup       | `twint -u johndoe`                        | [Twint](https://github.com/twintproject/twint)   

## Installation

To install these tools, simply clone the repository and run the `osxOSINT.py` script.

```bash
git clone https://github.com/heyfinal/osxOSINT.git
cd osxOSINT
chmod +x osxOSINT.py
./osxOSINT.py
```

## Usage

 install
 ```bash
chmod +x osxOSINT.py
./osxOSINT.py
```

Once the script has finished running, it will generate an HTML report on your Desktop named `osint_tools_report.html`. The report will provide the installation status and example commands for each tool.


```bash
open ~/Desktop/osint_tools_report.html
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

**This project is not licenced & offers not warrenty. Use & modify as you deem fit.**
---

Built with Rick Sanchez's genius and Daniel Gillaspy's help, you pathetic Earthlings!


[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/danielgillaspy?igsh=MWRjeXJnOXo5aXhkYg%3D%3D&utm_source=qr)
[![Email](https://img.shields.io/badge/Email-daniel@gillaspy.me-blue?style=for-the-badge&logo=gmail&logoColor=white)](mailto:daniel@gillaspy.me)
