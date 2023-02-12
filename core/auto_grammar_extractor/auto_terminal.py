from pathlib import Path
from talon import Context, Module, actions
from .extract_grammar import main, SupportedTypes

mod = Module()


@mod.action_class
class Actions:

    def extract_grammar_from_terminal_history():
        """"""
        main(Path(f'~/.bash_history').expanduser(), SupportedTypes.terminal)


ctx = Context()
ctx.matches = '\napp: gnome_terminal\n'
terminal_keywords = {}
mod.list('vocabulary', desc='additional vocabulary words')
automatically_generated_mapping = {'gedit': 'gedit', 'gedit rego': 'gedit rego.', 'gedit rego sh': 'gedit rego.sh',
                                   'chmod': 'chmod', 'chmod x': 'chmod +x ', 'chmod x rego': 'chmod +x rego.',
                                   'chmod x rego sh': 'chmod +x rego.sh', 'sudo  rego': 'sudo ./rego.', 'sudo': 'sudo',
                                   'sudo  rego sh': 'sudo ./rego.sh', 'sudo apt': 'sudo apt ',
                                   'sudo apt install': 'sudo apt install ',
                                   'sudo apt install thunderbird': 'sudo apt install thunderbird', 'run sh': './run.sh',
                                   'run': 'run', 'sudo apt install git': 'sudo apt install git ',
                                   'sudo apt install git build': 'sudo apt install git build-',
                                   'cd  talon': 'cd .talon/', 'cd': 'cd', 'cd  talonuser': 'cd .talon/user/',
                                   'cd talon': 'cd talon-', 'cd talon grammar': 'cd talon-grammar/',
                                   'git status': 'git status', 'git': 'git',
                                   'sudo apt install regolith': 'sudo apt install regolith-',
                                   'sudo apt install regolith look': 'sudo apt install regolith-look-',
                                   'sudo apt install  anydesk': 'sudo apt install ./anydesk_',
                                   'sudo apt install  anydesk     amd': 'sudo apt install ./anydesk_6.2.1-1_amd6',
                                   'poetry': 'poetry', 'sudo apt install curl': 'sudo apt install curl',
                                   'poetry add': 'poetry add ', 'poetry add django': 'poetry add Django',
                                   'cd pycharmprojects': 'cd PycharmProjects/',
                                   'cd pycharmprojectsmyfirstdjango': 'cd PycharmProjects/myFirstDjango/',
                                   'sudo apt install python': 'sudo apt install python3',
                                   'sudo apt install python distutils': 'sudo apt install python3-distutils',
                                   'sudo apt install python apt': 'sudo apt install python3-apt',
                                   'sudo apt update': 'sudo apt update', 'sudo apt upgrade': 'sudo apt upgrade',
                                   'sudo apt remove': 'sudo apt remove ',
                                   'sudo apt remove python': 'sudo apt remove python3',
                                   'sudo apt remove python distutils': 'sudo apt remove python3-distutils',
                                   'cd django': 'cd django/', 'pip install': 'pip install ', 'pip': 'pip',
                                   'pip install django': 'pip install django', 'python': 'python',
                                   'python  m': 'python -m ', 'python  m pip': 'python -m pip ',
                                   'python  m pip install': 'python -m pip install ',
                                   'python  m pip install django': 'python -m pip install django',
                                   'pip install distutils': 'pip install distutils',
                                   'poetry add numpy': 'poetry add numpy', 'python manage': 'python manage.',
                                   'python manage py': 'python manage.py ',
                                   'python manage py test': 'python manage.py test', 'poetry shell': 'poetry shell',
                                   'sudo add': 'sudo add-', 'sudo add apt': 'sudo add-apt-',
                                   'sudo add apt repository': 'sudo add-apt-repository ',
                                   'sudo add apt repository ppa': 'sudo add-apt-repository ppa:',
                                   'python   version': 'python3 --version',
                                   'cd pycharmprojectsmydjangopoetry': 'cd PycharmProjects/myDjangoPoetry/',
                                   'django': 'django', 'django admin': 'django-admin ',
                                   'django admin startproject': 'django-admin startproject ',
                                   'django admin startproject my': 'django-admin startproject my_',
                                   'python manage py runserver': 'python manage.py runserver ',
                                   'python manage py startapp': 'python manage.py startapp ',
                                   'python manage py startapp pages': 'python manage.py startapp pages',
                                   'ifconfig': 'ifconfig', 'pip manage': 'pip manage.',
                                   'pip manage py': 'pip manage.py ',
                                   'pip manage py makemigrations': 'pip manage.py makemigrations ',
                                   'pip manage py makemigrations pages': 'pip manage.py makemigrations pages',
                                   'python manage py makemigrations': 'python manage.py makemigrations ',
                                   'python manage py migrate': 'python manage.py migrate>',
                                   'python manage py createsuperuser': 'python manage.py createsuperuser',
                                   'firewall': 'firewall', 'firewall cmd': 'firewall-cmd ',
                                   'firewall cmd   list': 'firewall-cmd --list-',
                                   'firewall cmd   list ports': 'firewall-cmd --list-ports', 'sudo ufw': 'sudo ufw ',
                                   'sudo ufw status': 'sudo ufw status ',
                                   'sudo ufw status verbose': 'sudo ufw status verbose',
                                   'poetry add guiicorn': 'poetry add guiicorn',
                                   'poetry add gunicorn': 'poetry add gunicorn', 'gunicorn': 'gunicorn',
                                   'gunicorn my': 'gunicorn my_', 'gunicorn my project': 'gunicorn my_project.',
                                   'gunicorn my project wsgi': 'gunicorn my_project.wsgi',
                                   'python manage py check': 'python manage.py check ',
                                   'python manage py check   deploy': 'python manage.py check --deploy',
                                   'python manage py flush': 'python manage.py flush',
                                   'cd djangoblogposts': 'cd djangoBlogPosts/',
                                   'django admin startproject mydjango': 'django-admin startproject myDjango ',
                                   'python manage py startapp blog': 'python manage.py startapp blog'}
mod.list('terminal_keywords', desc='Automatically extracted key words from terminal files')
ctx.lists['self.terminal_keywords'] = dict(automatically_generated_mapping, **terminal_keywords)
ctx.lists['user.vocabulary'] = dict(automatically_generated_mapping, **terminal_keywords)


@mod.capture(rule='{self.terminal_keywords}+')
def terminal_keywords(m) -> str:
    return ''.join(m.terminal_keywords_list)
