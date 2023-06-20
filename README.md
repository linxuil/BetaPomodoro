## 1. General info
The project "PomoWave" is a Pomodoro timer implementation written in Python.\
I use this Pomodoro timer for work.

This timer is created to incorporate two distinctive features:
1. Quick startup:\
Many Pomodoro timers take a long time to start up due to dependencies.\
However, this timer is designed to launch quickly.
2. Time ticking sound:\
The ticking sound of a clock helps me stay focused and keep track of time,\
especially when I get distracted.

## 2. Downloading the Repository
To download the repository, you have a few options

### 2.1. Clone the Repository via git
If you have Git installed on your system, you can clone the repository using\
the following command in your terminal or command prompt:
```bash
$ REPO_URL='https://github.com/linxuil/pomow.git&&\
git clone "${REPO_URL}" 'pomow'
```
This will create a local copy of the repository on your machine.

### 2.2. Download as ZIP file
Alternatively, you can download the repository as a ZIP file.\
Simply navigate to the repository's page here and click on the "Code" button.\
Then select "Download ZIP" to save the ZIP file to your computer.\
After downloading, extract the contents of the ZIP file to access the repository files.

## 3. Usage
### 3.1. Without install module
Try use python script via cmd without install:
```bash
$ cd pomow
$ ./pomow
```
### 3.2. PIP module istall
You can install via `pip` in venv:
```bash
$ cd pomow

# Install venv if needed
$ sudo apt install python3-venv

# Create and activate venv in directory "venv"
$ VENV_DIR_NAME='venv'&&\
python3 -m venv "${VENV_DIR_NAME}"&&\
source venv/bin/activate

# Install module
$ pip install -e .

# Try use console command
$ pomow
```
Then you need exit from venv
```
$ deactivate
```

<!-- CONTRIBUTING -->
## 4. Contributing

If you have a suggestion that would make this better,\
please fork the repo and create a pull request.\
You can also simply open an issue with the tag "enhancement".\
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YouFeature`)
3. Write any changes in code
4. Add changes to index (`git add -A`)
5. Commit your Changes (`git commit -m 'You description'`)
6. Push to the Branch (`git push origin feature/YouFeature`)
7. Open a Pull Request on github

## 5. License

Distributed under the MIT License. See `LICENSE.md` for more information.

## 6. Contact

linxuil - linxuil.g@gmail.com

Project Link: [https://github.com/linxuil/pomow](https://github.com/linxuil/pomow)
