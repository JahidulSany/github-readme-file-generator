from InquirerPy import inquirer

# Collecting Content Data from Constructor
def collect_content_data(self):
    self.title = inquirer.text(message="Project Title: ").execute()
    self.desc = inquirer.text(message="Project Description: ").execute()
    self.install_instruct = inquirer.text(message="Installation Instructions: ").execute()
    self.usage_instruct  = inquirer.text(message="Usage Instructions: ").execute()
    licenses = ['MIT License', 'Apache License 2.0', 'GNU General Public License (GPL v3)', 'GNU Lesser General Public License (LGPL v3)', 'Mozilla Public License 2.0 (MPL 2.0)', 'Creative Commons Licenses (CC0, CC BY, etc.)', 'Unlicense']
    self.license = inquirer.rawlist(message="Select a license from the following list: ", default=1, choices=licenses).execute()
    self.author = inquirer.text(message="Author: ").execute()
    self.contact = inquirer.text(message="Contact: ").execute()