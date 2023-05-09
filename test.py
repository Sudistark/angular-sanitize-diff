import os

# get all angular version list after 1.2.20 only


versions = os.popen('npm view angular versions').read().split('\n')

# format the above array properly

for i in range(0, len(versions)):
    versions[i] = versions[i].replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace(" ", "")


# loop through versions and download this file https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/1.8.3/angular-sanitize.js

#I want to do a diff between all the versions so I will do it with github one by one

for i in range(0, len(versions)):
        os.system('wget https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/' + versions[i] + '/angular-sanitize.js')
        os.system("git add .")
        os.system("git commit -m 'angular-sanitize.js version " + versions[i] + "'")
        os.system("git push")
        #delay 3sec
        os.system("sleep 3")
        

