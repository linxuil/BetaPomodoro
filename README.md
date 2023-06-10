## 1. General info
This project is <!prj_name!> implementation for python.
I use this <!prj_name!> for:
<!...!>

## 2. Usage
### 2.1. Without install module
Try use python script via cmd without install:
```bash
$ cd <'prj_folder'>

<!...!>
```
### 2.2. PIP module istall
You can install via `pip` in venv:
```bash
# Pull repo
$ REPO_URL='https://github.com/linxuil/<!prj_name!>'&&\
git clone "${REPO_URL}" '<!prj_name!>'&&\
cd <!prj_name!>

# Install venv if needed
$ sudo apt install python3-venv

# Create and activate venv in directory "venv"
$ VENV_DIR_NAME='venv'&&\
python3 -m venv "${VENV_DIR_NAME}"&&\
source venv/bin/activate

# Install module
$ pip install -e .

# Try use console command
$ <!prj_name!> <!...!>
```
Then you need exit from venv
```
$ deactivate
```

<!-- CONTRIBUTING -->
## 3. Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YouFeature`)
3. Write any changes in code
4. Add changes to index (`git add -A`)
5. Commit your Changes (`git commit -m 'You description'`)
6. Push to the Branch (`git push origin feature/YouFeature`)
7. Open a Pull Request on github

## 4. License

Distributed under the MIT License. See `LICENSE.md` for more information.

## 5. Contact

linxuil - linxuil.g@gmail.com

Project Link: [https://github.com/linxuil/<!prj_name!>](https://github.com/linxuil/<!prj_name!>)
