from talon import Context, Module, actions

ctx = Context()
# Context matching
ctx.matches = r"""
app: gnome_terminal
"""
mod = Module()
terminal_keywords = {}
mod.list('vocabulary', desc='additional vocabulary words')
automatically_generated_mapping = {'sudo apt': 'sudo apt ', 'sudo': 'sudo', 'sudo apt update': 'sudo apt update',
                                   'sudo apt upgrade': 'sudo apt upgrade', 'docker': 'docker',
                                   'docker login': 'docker login ', 'docker login srv': 'docker login srv-',
                                   'docker login srv builder': 'docker login srv-builder.',
                                   'docker login srv builder fkie': 'docker login srv-builder.fkie.',
                                   'sudo snap': 'sudo snap ', 'sudo snap install': 'sudo snap install ',
                                   'sudo snap install spotify': 'sudo snap install spotify',
                                   'sudo apt install': 'sudo apt install ',
                                   'sudo apt install docker': 'sudo apt install docker.',
                                   'sudo apt install docker io': 'sudo apt install docker.io ',
                                   'sudo apt install docker io docker': 'sudo apt install docker.io docker-',
                                   'sudo apt install regolith': 'sudo apt install regolith-',
                                   'sudo apt install regolith desktop': 'sudo apt install regolith-desktop',
                                   'chmodsudo': 'chmodsudo', 'chmodsudo groupadd': 'chmodsudo groupadd ',
                                   'chmodsudo groupadd docker': 'chmodsudo groupadd docker',
                                   'sudo groupadd': 'sudo groupadd ', 'sudo groupadd docker': 'sudo groupadd docker',
                                   'sudo usermod': 'sudo usermod ', 'sudo usermod  ag': 'sudo usermod -aG ',
                                   'sudo usermod  ag docker': 'sudo usermod -aG docker ', 'newgrp': 'newgrp',
                                   'newgrp docker': 'newgrp docker', 'chmod': 'chmod', 'sudo reboot': 'sudo reboot',
                                   'sudo snap install bitwarden': 'sudo snap install bitwarden', 'cat etc': 'cat /etc/',
                                   'cat': 'cat', 'cat etcenvironment': 'cat /etc/environment', 'spotify': 'spotify',
                                   'sudo apt install gnome': 'sudo apt install gnome-',
                                   'sudo apt install gnome tweaks': 'sudo apt install gnome-tweaks', 'ls  l': 'ls -l ',
                                   'ls': 'ls', 'apt install': 'apt install ', 'apt': 'apt',
                                   'apt install regolith': 'apt install regolith-',
                                   'apt install regolith look': 'apt install regolith-look-',
                                   'sudo apt install regolith look': 'sudo apt install regolith-look-',
                                   'nautilus': 'nautilus ', 'touch': 'touch', 'touch user': 'touch user_',
                                   'touch user conf': 'touch user_conf', 'sudo install': 'sudo install ',
                                   'sudo install htop': 'sudo install htop',
                                   'sudo apt install htop': 'sudo apt install htop',
                                   'sudo snap install telegram': 'sudo snap install telegram-',
                                   'sudo snap install telegram desktop': 'sudo snap install telegram-desktop',
                                   'ssh srv': 'ssh srv-', 'ssh': 'ssh', 'ssh srv jumphost': 'ssh srv-jumphost-',
                                   'poetry': 'poetry', 'poetry update': 'poetry update ', 'pip install': 'pip install ',
                                   'pip': 'pip', 'pip install snakeviz': 'pip install snakeviz', 'snakeviz': 'snakeviz',
                                   'snakeviz needs': 'snakeviz needs_',
                                   'snakeviz needs profiling': 'snakeviz needs_profiling.',
                                   'snakeviz needs profiling prof': 'snakeviz needs_profiling.prof',
                                   'generate': 'generate', 'generate server': './generate_server.',
                                   'generate server sh': './generate_server.sh', 'docker compose': 'docker-compose ',
                                   'docker compose build': 'docker-compose build ',
                                   'docker compose push': 'docker-compose push ',
                                   'sudo apt install obs': 'sudo apt install obs-',
                                   'sudo apt install obs studio': 'sudo apt install obs-studio',
                                   'cd language': 'cd language_', 'cd': 'cd',
                                   'cd language detection': 'cd language_detection_',
                                   'cd language detection connector': 'cd language_detection_connector/',
                                   'docker pull': '\\docker pull ', 'docker pull python': 'docker pull python:',
                                   'cd  language': 'cd  language_', 'cd  language detection': 'cd  language_detection_',
                                   'cd  language detection connector': 'cd  language_detection_connector/',
                                   'python': 'python',
                                   'python updatefeaturesnochangeno': 'python3 updateFeaturesNoChangeNo\\',
                                   'docker logs': 'docker logs ', 'docker logs raat': 'docker logs raat-',
                                   'docker logs raat language': 'docker logs raat-language-',
                                   'docker logs raat language detection': 'docker logs raat-language-detection ',
                                   'docker logs  f': 'docker logs -f ', 'docker logs  f raat': 'docker logs -f raat-',
                                   'docker logs  f raat language': 'docker logs -f raat-language-',
                                   'docker logs   tail': 'docker logs --tail ',
                                   'docker logs   tail raat': 'docker logs --tail 1raat-',
                                   'docker logs   tail raat language': 'docker logs --tail 1raat-language-',
                                   'docker logs   tail  raat': 'docker logs --tail 1 raat-',
                                   'docker logs   tail  raat language': 'docker logs --tail 1 raat-language-',
                                   'sudo apt install arandr': 'sudo apt install arandr',
                                   'docker build': 'docker build ', 'chmod x': 'chmod +x ',
                                   'chmod x build': 'chmod +x build.', 'chmod x build bat': 'chmod +x build.bat',
                                   'build': 'build', 'build bat': './build.bat', 'docker   version': 'docker --version',
                                   'docker compose build annotation': 'docker-compose build annotation_',
                                   'cd annotation': 'cd annotation_', 'cd annotation server': 'cd annotation_server/',
                                   'poetry add': 'poetry add ', 'poetry add flask': 'poetry add flask_',
                                   'poetry add flask testing': 'poetry add flask_testing', 'poetry lock': 'poetry lock',
                                   'python build': 'python3 build.', 'python build py': 'python3 build.py',
                                   'poetry run': 'poetry run ', 'poetry run python': 'poetry run python ',
                                   'poetry run python build': 'poetry run python build.',
                                   'poetry run python build py': 'poetry run python build.py',
                                   'poetry install': 'poetry install ',
                                   'poetry install   with': 'poetry install --with ',
                                   'poetry install   with dev': 'poetry install --with dev',
                                   'docker compose up': 'docker-compose up ',
                                   'docker compose up annotation': 'docker-compose up annotation',
                                   'docker compose push annotation': 'docker-compose push annotation',
                                   'ping https': 'ping https:', 'ping': 'ping', 'curl https': 'curl https:',
                                   'curl': 'curl', 'cd annotation connector': 'cd annotation_connector/',
                                   'chmod x generate': 'chmod +x generate_',
                                   'chmod x generate clients': 'chmod +x generate_clients.',
                                   'chmod x generate clients xsh': 'chmod +x generate_clients.xsh',
                                   'generate clients': './generate_clients.',
                                   'generate clients xsh': './generate_clients.xsh', 'ssh ubuntu': 'ssh ubuntu@',
                                   'cd build': 'cd build_', 'cd build all': 'cd build_all/',
                                   'docker compose build   parallel': 'docker-compose build --parallel',
                                   'cd search': 'cd search_', 'cd search connector': 'cd search_connector/',
                                   'snap search': 'snap search ', 'snap': 'snap',
                                   'snap search vmware': 'snap search vmware ',
                                   'snap search vmware horizon': 'snap search vmware horizon',
                                   'docker kill': 'docker kill ', 'xonsh': 'xonsh', 'xonsh   v': 'xonsh --v',
                                   'xonsh  v': 'xonsh -v', 'docker images': 'docker images ',
                                   'docker images  grep': 'docker images | grep ',
                                   'docker images  grep fkie': 'docker images | grep fkie_',
                                   'docker images  grep fkie text': 'docker images | grep fkie_text',
                                   'cd raat': 'cd raat2', 'cd raat search': 'cd raat-search/',
                                   'docker compose up raat': 'docker-compose up raat-',
                                   'docker compose up raat search': 'docker-compose up raat-search',
                                   'docker login repo': 'docker login repo-',
                                   'docker login repo manager': 'docker login repo-manager.',
                                   'docker login repo manager fkie': 'docker login repo-manager.fkie.',
                                   'run sh': './run.sh ', 'run': 'run', 'cd  talon': 'cd .talon/',
                                   'cd  talonuser': 'cd .talon/user/', 'cd downloads': 'cd Downloads/',
                                   'cd downloadstalon': 'cd Downloads/talon-',
                                   'cd downloadstalon linux': 'cd Downloads/talon-linux-', 'talon': './talon/',
                                   'talonrun': 'talonrun', 'talonrun sh': './talon/run.sh',
                                   'cd downloadstalon linuxtalon': 'cd Downloads/talon-linux/talon/',
                                   'sudo cp': 'sudo cp ', 'sudo cp  r': 'sudo cp -R ',
                                   'sudo cp  r talon': 'sudo cp -R talon/',
                                   'sudo cp  r talon usr': 'sudo cp -R talon/ /usr/',
                                   'sudo cp  r talon usrlib': 'sudo cp -R talon/ /usr/lib/',
                                   'sudo cp  r talon usrlibpython': 'sudo cp -R talon/ /usr/lib/python3',
                                   'ps aux': 'ps aux ', 'ps': 'ps', 'ps aux  grep': 'ps aux | grep ',
                                   'ps aux  grep pyc': 'ps aux | grep pyc', 'run sh s': './run.sh &s',
                                   'docker compose build controller': 'docker-compose build controller',
                                   'docker ps': 'docker ps', 'docker stats': 'docker stats',
                                   'sudo apt install handbrake': 'sudo apt install handbrake',
                                   'cd raat searchsearch': 'cd raat-search/search_',
                                   'cd raat searchsearch connector': 'cd raat-search/search_connector/',
                                   'cd raat annotation': 'cd raat-annotation/',
                                   'cd raat annotationannotation': 'cd raat-annotation/annotation_',
                                   'docker image': 'docker image ', 'docker image ls': 'docker image ls ',
                                   'version': 'VERSION=', 'versionv': 'VERSION=v0', 'docker ls': 'docker ls',
                                   'docker container': 'docker container ',
                                   'docker container ls': 'docker container ls',
                                   'docker killversion': 'docker killVERSION=',
                                   'docker killversionv': 'docker killVERSION=v0', 'docker kill ee': 'docker kill ee7',
                                   'docker remove': 'docker remove ', 'docker remove version': 'docker remove VERSION=',
                                   'docker remove versionv': 'docker remove VERSION=v0', 'mkdir': 'mkdir',
                                   'mkdir projects': 'mkdir Projects', 'cd projects': 'cd Projects/',
                                   'cd sandbox': 'cd sandbox/', 'sandbox': 'sandbox', 'sandbox up': './sandbox up',
                                   'sandbox down': './sandbox down', 'docker image ls  grep': 'docker image ls | grep ',
                                   'docker image ls  grep data': 'docker image ls | grep data',
                                   'python  m': 'python3 -m ', 'python  m dataset': 'python3 -m dataset-',
                                   'python  m dataset package': 'python3 -m dataset-package',
                                   'xonsh main': 'xonsh main.', 'xonsh main xsh': 'xonsh main.xsh',
                                   'docker compose build  classifiy': 'docker-compose build  classifiy-',
                                   'docker compose build  annotation': 'docker-compose build  annotation_',
                                   'poetry add raat': 'poetry add raat-',
                                   'poetry add raat connector': 'poetry add raat-connector',
                                   'poetry add   source': 'poetry add --source ',
                                   'poetry add   source internal': 'poetry add --source internal ',
                                   'poetry add   source internal raat': 'poetry add --source internal raat-',
                                   'cd projectssandbox': 'cd Projects/sandbox/', 'sudo  sandbox': 'sudo ./sandbox ',
                                   'sudo  sandbox up': 'sudo ./sandbox up', 'sudo  sandbox down': 'sudo ./sandbox down',
                                   'sudo usermod  ag docker telegraf': 'sudo usermod -aG docker telegraf',
                                   'sandbox restart': './sandbox restart', 'poetry add uvicorn': 'poetry add uvicorn',
                                   'cd language detection server': 'cd language_detection_server_',
                                   'uvicorn': 'uvicorn', 'uvicorn main': 'uvicorn main:',
                                   'uvicorn mainapp': 'uvicorn main:app', 'uvicorn src': 'uvicorn src.',
                                   'uvicorn srcfkie': 'uvicorn src/fkie_',
                                   'uvicorn srcfkie language': 'uvicorn src/fkie_language_',
                                   'uvicorn srcfkie language detection': 'uvicorn src/fkie_language_detection/',
                                   'poetry add fastapi': 'poetry add fastapi[',
                                   'poetry add fastapi all': 'poetry add fastapi[all]', 'cd src': 'cd src/',
                                   'cd srcfkie': 'cd src/fkie_', 'cd srcfkie language': 'cd src/fkie_language_',
                                   'cd srcfkie language detection': 'cd src/fkie_language_detection/',
                                   'uvicorn fkie': 'uvicorn fkie_', 'uvicorn fkie language': 'uvicorn fkie_language_',
                                   'uvicorn fkie language detection': 'uvicorn fkie_language_detection.',
                                   'poetry add connexion': 'poetry add connexion', 'ls  l var': 'ls -l /var/',
                                   'ls  l varrun': 'ls -l /var/run/', 'ls  l varrundocker': 'ls -l /var/run/docker.',
                                   'ls  l varrundocker sock': 'ls -l /var/run/docker.sock', 'stat  c': 'stat -c ',
                                   'stat': 'stat', 'poetry add aiohttp': 'poetry add aiohttp ', 'tar  xvf': 'tar -xvf ',
                                   'tar': 'tar', 'tar  xvf python': 'tar -xvf Python-', 'cd python': 'cd Python-',
                                   'configure': 'configure', 'configure   enable': './configure --enable-',
                                   'configure   enable optimizations': './configure --enable-optimizations',
                                   'make altinstall': 'make altinstall', 'make': 'make', 'sudo make': 'sudo make ',
                                   'sudo make altinstall': 'sudo make altinstall', 'requirement': 'requirement',
                                   'requirement texts': '"requirement_texts"', 'language': '"language"',
                                   'poetry add aiohttp stomp': 'poetry add aiohttp stomp',
                                   'poetry add hunspell': 'poetry add hunspell', 'poetry add spacy': 'poetry add spacy',
                                   'poetry add six': 'poetry add six', 'docker build  t': 'docker build -t ',
                                   'docker build  t monolith': 'docker build -t monolith ', 'git branch': 'git branch ',
                                   'git': 'git', 'git branch  m': 'git branch -M ',
                                   'git branch  m main': 'git branch -M main', 'ls  la': 'ls -la', 'rm  r': 'rm -r ',
                                   'rm': 'rm', 'rm  r  git': 'rm -r .git/', 'rm  rf': 'rm -rf ',
                                   'rm  rf  git': 'rm -rf .git/', 'git init': 'git init',
                                   'cd raat staging': 'cd raat2_staging/', 'cd config': 'cd config/',
                                   'cd offline': 'cd offline/', 'sudo chown': 'sudo chown ',
                                   'sudo chown  r': 'sudo chown -R ', 'sudo chown  r jan': 'sudo chown -R jan:',
                                   'sudo chown  r janroot': 'sudo chown -R jan:root ',
                                   'sudo chown  r janroot offline': 'sudo chown -R jan:root offline/',
                                   'sudo apt install putty': 'sudo apt install putty-',
                                   'chmod x upload': 'chmod +x upload_',
                                   'chmod x upload linux': 'chmod +x upload_linux.',
                                   'chmod x upload linux sh': 'chmod +x upload_linux.sh', 'upload': 'upload',
                                   'upload linux': './upload_linux.', 'upload linux sh': './upload_linux.sh',
                                   'sudo apt install pscp': 'sudo apt install pscp',
                                   'sudo apt install putty tools': 'sudo apt install putty-tools',
                                   'chmod x deploy': 'chmod +x deploy.',
                                   'chmod x deploy linux': 'chmod +x deploy_linux.',
                                   'chmod x deploy linux cmd': 'chmod +x deploy_linux.cmd', 'deploy': 'deploy',
                                   'deploy linux': './deploy_linux.', 'deploy linux cmd': './deploy_linux.cmd',
                                   'cd etc': 'cd /etc/', 'cd etcdocker': 'cd /etc/docker/', 'sudo gedit': 'sudo gedit ',
                                   'sudo gedit daemon': 'sudo gedit daemon.',
                                   'sudo gedit daemon json': 'sudo gedit daemon.json',
                                   'cd etcsystemd': 'cd /etc/systemd/',
                                   'cd etcsystemdsystem': 'cd /etc/systemd/system/',
                                   'cd etcsystemdsystemdocker': 'cd /etc/systemd/system/docker.',
                                   'cd etcsystemdsystemdocker service': 'cd /etc/systemd/system/docker.service.',
                                   'cd etcsystemdsystemdocker service d': 'cd /etc/systemd/system/docker.service.d/',
                                   'sudo gedit override': 'sudo gedit override.',
                                   'sudo gedit override conf': 'sudo gedit override.conf', 'systemctl': 'systemctl',
                                   'systemctl daemon': 'systemctl daemon-',
                                   'systemctl daemon reload': 'systemctl daemon-reload',
                                   'systemctl restart': 'systemctl restart ',
                                   'systemctl restart docker': 'systemctl restart docker.',
                                   'systemctl restart docker service': 'systemctl restart docker.service',
                                   'poetry add pytest': 'poetry add pytest-',
                                   'poetry add pytest order': 'poetry add pytest-order',
                                   'chmod x clean': 'chmod +x clean.', 'chmod x clean sh': 'chmod +x clean.sh ',
                                   'chmod x clean sh start': 'chmod +x clean.sh start.',
                                   'chmod x clean sh start sh': 'chmod +x clean.sh start.sh', 'clean': 'clean',
                                   'clean sh': './clean.sh', 'gedit': 'gedit', 'gedit clean': 'gedit clean.',
                                   'gedit clean sh': 'gedit clean.sh', 'start': 'start', 'start sh': './start.sh',
                                   'sudo apt install openjdk': 'sudo apt install openjdk-', 'cd bin': 'cd bin/',
                                   'cd bintalon': 'cd bin/talon/', 'upload sh': './upload.sh',
                                   'deploy sh': './deploy.sh', 'chmod x deploy sh': 'chmod +x deploy.sh ',
                                   'chmod x deploy sh upload': 'chmod +x deploy.sh upload.',
                                   'chmod x deploy sh upload sh': 'chmod +x deploy.sh upload.sh',
                                   'cd talon': 'cd talon-', 'sudo apt install z': 'sudo apt install 7z',
                                   'sudo apt install p': 'sudo apt install p7',
                                   'sudo apt install pzip': 'sudo apt install p7zip-',
                                   'sudo apt install pzip full': 'sudo apt install p7zip-full',
                                   'exec uvicorn': 'exec uvicorn ', 'exec': 'exec',
                                   'exec uvicorn src': 'exec uvicorn src.',
                                   'exec uvicorn src api': 'exec uvicorn src.api.',
                                   'exec uvicorn src api endpoint': 'exec uvicorn src.api.endpoint:',
                                   'exec uvicorn src api endpointapp': 'exec uvicorn src.api.endpoint:app ',
                                   'cat classification': 'cat classification.',
                                   'cat classification tar': 'cat classification.tar.',
                                   'cat classification tar z': 'cat classification.tar.7z.',
                                   'uvicorn src api': 'uvicorn src.api.',
                                   'uvicorn src api endpoint': 'uvicorn src.api.endpoint:',
                                   'uvicorn src api endpointapp': 'uvicorn src.api.endpoint:app',
                                   'docker run': 'docker run ', 'docker run rabbitmq': 'docker run rabbitmq',
                                   'docker prune': 'docker prune', 'docker system': 'docker system ',
                                   'docker system prune': 'docker system prune',
                                   'z x classification': '7z x classification.', 'z': 'z',
                                   'z x classification tar': '7z x classification.tar.',
                                   'z x classification tar gz': '7z x classification.tar.gz.', 'man z': 'man 7z ',
                                   'man': 'man', 'man z x': 'man 7z x ',
                                   'man z x classification': 'man 7z x classification',
                                   'z e classification': '7z e classification.',
                                   'z e classification tar': '7z e classification.tar.',
                                   'z e classification tar z': '7z e classification.tar.7z.',
                                   'cd documents': 'cd Documents/', 'docker load': 'docker load ',
                                   'docker load  classification': 'docker load < classification_',
                                   'docker load  classification image': 'docker load < classification_image.',
                                   'rm classification': 'rm classification.',
                                   'rm classification tar': 'rm classification.tar.',
                                   'rm classification tar z': 'rm classification.tar.7z.', 'gedit t': 'gedit t',
                                   'cd something': 'cd Something', 'docker pull postgres': 'docker pull postgres:',
                                   'docker pull postgresalpine': 'docker pull postgres:alpine3',
                                   'docker image push': 'docker image push', 'docker pull redis': 'docker pull redis:',
                                   'cd talon linux': 'cd talon-linux-', 'chmod x nuke': 'chmod +x nuke_',
                                   'chmod x nuke docker': 'chmod +x nuke_docker.',
                                   'chmod x nuke docker sh': 'chmod +x nuke_docker.sh', 'nuke docker': './nuke_docker.',
                                   'nuke': 'nuke', 'nuke docker sh': './nuke_docker.sh', 'touch etc': 'touch /etc/',
                                   'touch etcdocker': 'touch /etc/docker/',
                                   'touch etcdockerdaemon': 'touch /etc/docker/daemon.',
                                   'touch etcdockerdaemon json': 'touch /etc/docker/daemon.json',
                                   'sudo touch': 'sudo touch ', 'sudo touch etc': 'sudo touch /etc/',
                                   'sudo touch etcdocker': 'sudo touch /etc/docker/',
                                   'sudo touch etcdockerdaemon': 'sudo touch /etc/docker/daemon.',
                                   'sudo touch etcdockerdaemon json': 'sudo touch /etc/docker/daemon.json',
                                   'sudo gedit etc': 'sudo gedit /etc/',
                                   'sudo gedit etcdocker': 'sudo gedit /etc/docker/',
                                   'sudo gedit etcdockerdaemon': 'sudo gedit /etc/docker/daemon.',
                                   'sudo gedit etcdockerdaemon json': 'sudo gedit /etc/docker/daemon.json',
                                   'sudo systemctl': 'sudo systemctl ',
                                   'sudo systemctl daemon': 'sudo systemctl daemon-',
                                   'sudo systemctl daemon reload': 'sudo systemctl daemon-reload',
                                   'sudo systemctl restart': 'sudo systemctl restart ',
                                   'sudo systemctl restart docker': 'sudo systemctl restart docker.',
                                   'docker pull rabbitmq': '\\docker pull rabbitmq:', 'iostat': 'iostat',
                                   'iotop': 'iotop', 'sudo apt install iotop': 'sudo apt install iotop',
                                   'sudo iotop': 'sudo iotop', 'iostat  d': 'iostat -d ', 'iostat  d t': 'iostat -d-t',
                                   'iostat  d  t': 'iostat -d -t ', 'iostat  d  t  m': 'iostat -d -t -m',
                                   'iostat interval': 'iostat interval ',
                                   'iostat interval   d': 'iostat interval 1 -d ',
                                   'iostat interval   d  t': 'iostat interval 1 -d -t ',
                                   'iostat interval   d  t  m': 'iostat interval 1 -d -t -m',
                                   'git checkout': 'git checkout ', 'git checkout  b': 'git checkout -b ',
                                   'git checkout  b release': 'git checkout -b release_',
                                   'git checkout  b release patch': 'git checkout -b release_patch',
                                   'docker image ls  grep b': 'docker image ls | grep 5b3',
                                   'poetry update raat': 'poetry update raat-',
                                   'poetry update raat connector': 'poetry update raat-connector',
                                   'git push': 'git push ', 'git push  u': 'git push -u ',
                                   'git push  u origin': 'git push -u origin ',
                                   'git push  u origin main': 'git push -u origin main', 'ls  a': 'ls -a',
                                   'cd user': 'cd user/', 'cd  git': 'cd .git/',
                                   'poetry update dataset': 'poetry update dataset-',
                                   'poetry update dataset package': 'poetry update dataset-package',
                                   'poetry update   remove': 'poetry update --remove-',
                                   'poetry update   remove untracked': 'poetry update --remove-untracked',
                                   'poetry install   remove': 'poetry install --remove-',
                                   'poetry install   remove untracked': 'poetry install --remove-untracked',
                                   'poetry install   sync': 'poetry install --sync', 'poetry remove': 'poetry remove ',
                                   'poetry remove dataset': 'poetry remove dataset-',
                                   'poetry remove dataset packag': 'poetry remove dataset-packag',
                                   'poetry remove dataset package': 'poetry remove dataset-package',
                                   'touch config': 'touch config', 'setxkbmap': 'setxkbmap',
                                   'setxkbmap us': 'setxkbmap us ', 'setxkbmap us  variant': 'setxkbmap us -variant ',
                                   'setxkbmap us  variant dvorak': 'setxkbmap us -variant dvorak',
                                   'setxkbmap de': 'setxkbmap de', 'chmod x extract': 'chmod +x extract_',
                                   'chmod x extract grammar': 'chmod +x extract_grammar.',
                                   'chmod x extract grammar py': 'chmod +x extract_grammar.py',
                                   'cd  talonusercore': 'cd .talon/user/core/',
                                   'cd  talonusercoreauto': 'cd .talon/user/core/auto_',
                                   'cd  talonusercoreauto grammar': 'cd .talon/user/core/auto_grammar_',
                                   'tail  f': 'tail -f ', 'tail': 'tail', 'tail  f extract': 'tail -f extract_',
                                   'tail  f extract grammar': 'tail -f extract_grammar.',
                                   'tail  f extract grammar py': 'tail -f extract_grammar.py ',
                                   'tail  f extract grammar py  n': 'tail -f extract_grammar.py -n ',
                                   'tail  f auto': 'tail -f auto_', 'tail  f auto grammar': 'tail -f auto_grammar.',
                                   'tail  f auto grammar py': 'tail -f auto_grammar.py ',
                                   'tail  f auto grammar py  n': 'tail -f auto_grammar.py -n ',
                                   'tail  f auto python': 'tail -f auto_python.',
                                   'tail  f auto python py': 'tail -f auto_python.py ',
                                   'tail  f auto python py  n': 'tail -f auto_python.py -n ', 'watch': 'watch',
                                   'watch  auto': 'watch  auto_', 'watch  auto python': 'watch  auto_python.',
                                   'watch  auto python py': 'watch  auto_python.py ',
                                   'watch  auto python py  n': 'watch  auto_python.py -n ', 'watch  n': 'watch -n ',
                                   'watch  n  tail': 'watch -n 1 tail ', 'watch  n  tail  f': 'watch -n 1 tail -f ',
                                   'watch  n  tail  f auto': 'watch -n 1 tail -f auto_',
                                   'watch  n  tail  f auto python': 'watch -n 1 tail -f auto_python.',
                                   'watch  n  tail  f auto python py': 'watch -n 1 tail -f auto_python.py',
                                   'sudo snap search': 'sudo snap search ',
                                   'sudo snap search python': 'sudo snap search python',
                                   'sudo apt install software': 'sudo apt install software-', 'sudo add': 'sudo add-',
                                   'sudo add apt': 'sudo add-apt-',
                                   'sudo add apt repository': 'sudo add-apt-repository ',
                                   'sudo add apt repository ppa': 'sudo add-apt-repository ppa:',
                                   'sudo apt install python': 'sudo apt install python3',
                                   'uvicorn src rest': 'uvicorn src.rest_',
                                   'uvicorn src rest api': 'uvicorn src.rest_api.',
                                   'uvicorn src rest api endpoint': 'uvicorn src.rest_api.endpoint:',
                                   'uvicorn src rest api endpointapp': 'uvicorn src.rest_api.endpoint:app ',
                                   'poetry add sse': 'poetry add sse-',
                                   'poetry add sse scarlette': 'poetry add sse-scarlette',
                                   'poetry add sse starlette': 'poetry add sse-starlette',
                                   'z  e annotation': '7z -e annotation.',
                                   'z  e annotation tar': '7z -e annotation.tar.',
                                   'z  e annotation tar z': '7z -e annotation.tar.7z.',
                                   'z e annotation': '7z e annotation.', 'z e annotation tar': '7z e annotation.tar.',
                                   'z e annotation tar z': '7z e annotation.tar.7z.',
                                   'docker load conet': 'docker load CONET_',
                                   'docker load  conet': 'docker load < CONET_', 'cd conet': 'cd CONET_',
                                   'cd conet annotation': 'cd CONET_Annotation/', 'rm annotation': 'rm annotation.',
                                   'rm annotation tar': 'rm annotation.tar.',
                                   'rm annotation tar z': 'rm annotation.tar.7z.', 'mkdir conet': 'mkdir CONET_',
                                   'mkdir conet annotation': 'mkdir CONET_Annotation', 'cd  conet': 'cd  CONET_',
                                   'cd  conet annotation': 'cd  CONET_Annotation/', 'clear': 'clear',
                                   'cd model': 'cd model_', 'cd model weights': 'cd model_weights/'}
mod.list('terminal_keywords', desc='Automatically extracted key words from terminal files')
ctx.lists['self.terminal_keywords'] = dict(automatically_generated_mapping, **terminal_keywords)
ctx.lists['user.vocabulary'] = dict(automatically_generated_mapping, **terminal_keywords)

@mod.capture(rule='{self.terminal_keywords}+')
def terminal_keywords(m) -> str:
    return ''.join(m.terminal_keywords_list)
