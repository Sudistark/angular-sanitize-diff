import os

# get all angular version list after 1.2.20 only

#versions = os.popen('npm view angular versions').read()
versions = ['1.2.20', '1.2.21', '1.2.22', '1.2.23', '1.2.27', '1.2.28', '1.2.29', '1.2.30', '1.2.31', '1.2.32', '1.3.0-rc.5', '1.3.0', '1.3.1', '1.3.2', '1.3.3', '1.3.4-build.3588', '1.3.4', '1.3.5', '1.3.6', '1.3.7', '1.3.8', '1.3.9', '1.3.10', '1.3.11', '1.3.12', '1.3.13', '1.3.14', '1.3.15', '1.3.16', '1.3.17', '1.3.18', '1.3.19', '1.3.20', '1.4.0-beta.0', '1.4.0-beta.1', '1.4.0-beta.2', '1.4.0-beta.3', '1.4.0-beta.4', '1.4.0-beta.5', '1.4.0-beta.6', '1.4.0-rc.0', '1.4.0-rc.1', '1.4.0-rc.2', '1.4.0', '1.4.1', '1.4.2', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7', '1.4.8', '1.4.9', '1.4.10', '1.4.11', '1.4.12', '1.4.13', '1.4.14', '1.5.0-beta.0', '1.5.0-beta.2', '1.5.0-rc.0', '1.5.0-rc.1', '1.5.0-rc.2', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.5', '1.5.6', '1.5.7', '1.5.8', '1.5.9', '1.5.10', '1.5.11', '1.6.0-rc.0', '1.6.0-rc.1', '1.6.0-rc.2', '1.6.0', '1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.6.5', '1.6.6', '1.6.7', '1.6.8', '1.6.9', '1.6.10', '1.7.0-rc.0', '1.7.0', '1.7.1', '1.7.2', '1.7.3', '1.7.4', '1.7.5', '1.7.6', '1.7.7', '1.7.8', '1.7.9', '1.8.0', '1.8.1', '1.8.2', '1.8.3']

# format the above array properly




# loop through versions and download this file https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/1.8.3/angular-sanitize.js

#I want to do a diff between all the versions so I will do it with github one by one

for i in range(0, len(versions)):
    print('wget https://cdnjs.cloudflare.com/ajax/libs/angular.js/' + versions[i] + '/angular-sanitize.js')
    os.system('wget https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/' + versions[i] + '/angular-sanitize.js')
    os.system("git add .")
    os.system("git commit -m 'angular-sanitize.js version " + versions[i] + "'")
    os.system("git push")
    #delay 3sec
    os.system("sleep 3")
        

