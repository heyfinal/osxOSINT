Here is the updated `README.md` file including the source and popular commands for each tool:

```md
# osxOSINT

## Description

`osxOSINT` is an autoinstaller for macOS compatible OSINT (Open Source Intelligence) tools. This script automates the installation and setup of several powerful OSINT tools, making it easier for users to perform reconnaissance and gather information.

## Features

- Automated installation of various OSINT tools
- Generates a detailed HTML report of the installation status
- Provides command examples and source links for each tool

## Tools Included

- **PhoneInfoga**: Reverse cell lookup
  - **Source**: [PhoneInfoga](https://github.com/sundowndev/phoneinfoga)
  - **Popular Command**: `phoneinfoga --phone 1234567890`

- **OSINT Framework**: General OSINT goodness
  - **Source**: [OSINT Framework](https://github.com/lockfale/OSINT-Framework)
  - **Popular Command**: `open OSINT-Framework/index.html`

- **SpiderFoot**: Reverse email/domain recon
  - **Source**: [SpiderFoot](https://github.com/smicallef/spiderfoot)
  - **Popular Command**: `sf.py -m sfp_email -t target@example.com`

- **theHarvester**: Email/name harvesting
  - **Source**: [theHarvester](https://github.com/laramies/theHarvester)
  - **Popular Command**: `theharvester -d example.com -b google`

- **Recon-ng**: Reverse address/email recon
  - **Source**: [Recon-ng](https://github.com/lanmaster53/recon-ng)
  - **Popular Command**: `recon-ng -m recon/contacts-credentials`

- **Maltego CE**: GUI reverse lookup madness
  - **Source**: [Maltego CE](https://www.maltego.com/downloads/)
  - **Popular Command**: `open /Applications/Maltego.app`

- **Sherlock**: Reverse name/username hunt
  - **Source**: [Sherlock](https://github.com/sherlock-project/sherlock)
  - **Popular Command**: `sherlock johndoe`

- **holehe**: Reverse email checker
  - **Source**: [holehe](https://github.com/megadose/holehe)
  - **Popular Command**: `holehe test@example.com`

- **VinSpy**: License plate lookup (US only)
  - **Source**: [VinSpy](https://github.com/vinspy/vinspy)
  - **Popular Command**: `vinspy.py --plate ABC123`

- **Twint**: Reverse name/social lookup
  - **Source**: [Twint](https://github.com/twintproject/twint)
  - **Popular Command**: `twint -u johndoe`

## Installation

See Steps below.

### Prerequisites

- macOS
- Homebrew
- Python 3.x

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/heyfinal/osxOSINT.git
    cd osxOSINT
    ```

2. Make the script executable:

    ```bash
    chmod +x osxOSINT.py
    ```

3. Run the script:

    ```bash
    ./osxOSINT.py
    ```

The script will ensure that `pipx` is installed via Homebrew if it's not already present. It will then proceed to install the listed OSINT tools, generating a status report and an HTML report on your desktop.

## Usage

Once installed, you can use the tools with the provided command examples. Refer to the source links for detailed documentation on each tool.

## Report

The script generates an HTML report `osint_tools_report.html` on your desktop, summarizing the installation status of each tool.

## Credits

- Built by Ai and Daniel Gillaspy
- Inspired by Rick Sanchez’s OSINT Lab

## License

This project is not licenced & provides no warrenty.
```

Feel free to customize this `README.md` file to better fit your needs.
