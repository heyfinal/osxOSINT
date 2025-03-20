#!/usr/bin/env python3

import subprocess
import os
import datetime
import webbrowser
from pathlib import Path

# Rick Sanchez’s OSINT Lab - Built by Ai and Daniel Gillaspy, you pathetic losers!
print("Wubba lubba dub dub! Rick Sanchez is gonna cook up some OSINT tools for your dumb asses!")
print(f"Today’s date: {datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Z %Y')}, and Rick’s feelin’ like a goddamn genius!")
print("Credits: Sanchez, Ai & Daniel Gillaspy made this shit happen!")

# Tools dictionary: name -> (desc, cmd, source)
TOOLS = {
    "PhoneInfoga": ("Reverse cell lookup", "phoneinfoga --phone 1234567890", "https://github.com/sundowndev/phoneinfoga"),
    "OSINT Framework": ("General OSINT goodness", "open OSINT-Framework/index.html", "https://github.com/lockfale/OSINT-Framework"),
    "SpiderFoot": ("Reverse email/domain recon", "sf.py -m sfp_email -t target@example.com", "https://github.com/smicallef/spiderfoot"),
    "theHarvester": ("Email/name harvesting", "theharvester -d example.com -b google", "https://github.com/laramies/theHarvester"),
    "Recon-ng": ("Reverse address/email recon", "recon-ng -m recon/contacts-credentials", "https://github.com/lanmaster53/recon-ng"),
    "Maltego CE": ("GUI reverse lookup madness", "open /Applications/Maltego.app", "https://www.maltego.com/downloads/"),
    "Sherlock": ("Reverse name/username hunt", "sherlock johndoe", "https://github.com/sherlock-project/sherlock"),
    "holehe": ("Reverse email checker", "holehe test@example.com", "https://github.com/megadose/holehe"),
    "VinSpy": ("License plate lookup (US only)", "vinspy.py --plate ABC123", "https://github.com/vinspy/vinspy"),
    "Twint": ("Reverse name/social lookup", "twint -u johndoe", "https://github.com/twintproject/twint")
}

STATUS_FILE = Path.home() / "Desktop" / "rick_status.txt"
HTML_FILE = Path.home() / "Desktop" / "osint_tools_report.html"
INSTALL_DIR = Path.home() / "osint_tools"

# Ensure install dir exists
INSTALL_DIR.mkdir(exist_ok=True)

# Check for pipx, install if missing
try:
    subprocess.run(["pipx", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Rick needs pipx, you idiots! Installing it via Homebrew—don’t screw this up!")
    subprocess.run(["brew", "install", "pipx"], check=True)
    with open(STATUS_FILE, "a") as f:
        f.write("Rick slapped pipx into place with Homebrew, you primitive screwheads!\n")

# Clear status file
with open(STATUS_FILE, "w") as f:
    f.write("")

def install_tool(name, source):
    """Install a tool with Rick’s genius, bitches!"""
    with open(STATUS_FILE, "a") as f:
        f.write(f"Rick’s sciencin’ the shit outta {name}, you brain-dead Mortys!\n")

    os.chdir(INSTALL_DIR)
    if name == "Maltego CE":
        try:
            subprocess.run(["brew", "install", "--cask", "maltego"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Holy crap, {name} installed via Homebrew cask like I’m a freakin’ god!\n")
            return True
        except subprocess.CalledProcessError:
            pass
    elif name == "OSINT Framework":
        try:
            subprocess.run(["git", "clone", "--quiet", f"{source}.git"], check=True, env={"GIT_TERMINAL_PROMPT": "0"})
            with open(STATUS_FILE, "a") as f:
                f.write(f"Get schwifty! {name} cloned like Rick’s portal gun on overdrive!\n")
            return True
        except subprocess.CalledProcessError:
            pass
    else:
        # Pipx for Python tools
        try:
            subprocess.run(["pipx", "install", "--include-deps", f"git+{source}.git"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            with open(STATUS_FILE, "a") as f:
                f.write(f"Booyah! {name} installed via pipx—Rick’s a goddamn genius!\n")
            return True
        except subprocess.CalledProcessError:
            # Fallback to Homebrew
            try:
                brew_name = name.lower().replace(" ", "-")
                subprocess.run(["brew", "install", brew_name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                with open(STATUS_FILE, "a") as f:
                    f.write(f"Alright, alright, {name} slid in via Homebrew—don’t tell Morty I used that crap!\n")
                return True
            except subprocess.CalledProcessError:
                pass

    with open(STATUS_FILE, "a") as f:
        f.write(f"Burp! {name} fucked up hard and didn’t install, you useless little shits!\n")
    return False

# Install all tools
for name, (desc, cmd, source) in TOOLS.items():
    install_tool(name, source)

with open(STATUS_FILE, "a") as f:
    f.write("Rick’s done sciencin’, you idiots! Time to see the results of my brilliance!\n")

# Generate HTML report
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rick’s OSINT Tools Report</title>
    <style>
        body {{background-color: #212121; color: #e0e0e0; font-family: 'Helvetica', sans-serif; padding: 20px;}}
        h1 {{color: #ff9500; text-align: center;}}
        table {{width: 100%; border-collapse: collapse; margin-top: 20px;}}
        th, td {{padding: 15px; text-align: left; border-bottom: 1px solid #424242;}}
        th {{background-color: #ff9500; color: #212121;}}
        tr:nth-child(even) {{background-color: #303030;}}
        .failed {{color: #ff3d00; font-weight: bold;}}
        .credits {{font-size: 14px; text-align: center; margin-top: 20px; color: #ff9500;}}
    </style>
</head>
<body>
    <h1>Rick’s OSINT Tools Report - {date}</h1>
    <table>
        <tr><th>Tool</th><th>Description</th><th>Command Example</th><th>Source</th><th>Status</th></tr>
"""

with open(STATUS_FILE, "r") as f:
    status_lines = f.readlines()

for name, (desc, cmd, source) in TOOLS.items():
    status = "Installed like I’m Rick freakin’ Sanchez!"
    for line in status_lines:
        if name in line and "fucked up hard" in line:
            status = '<span class="failed">FUCKED UP - Install this crap yourself, Morty!</span>'
            break
    html += f"""
        <tr>
            <td>{name}</td>
            <td>{desc}</td>
            <td><code>{cmd}</code></td>
            <td><a href="{source}" style="color: #ff9500">{source}</a></td>
            <td>{status}</td>
        </tr>
    """

html += """
    </table>
    <div class="credits">Built with Rick’s genius and Daniel Gillaspy’s help, bitches!</div>
</body>
</html>
"""

with open(HTML_FILE, "w") as f:
    f.write(html.format(date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

with open(STATUS_FILE, "a") as f:
    f.write(f"Rick’s dropped the HTML report at {HTML_FILE}, you pathetic Earthlings! Check my genius!\n")

# Print status and open report
print("\nHere’s what Rick scienced up, you morons:")
with open(STATUS_FILE, "r") as f:
    print(f.read())

webbrowser.open(f"file://{HTML_FILE}")
