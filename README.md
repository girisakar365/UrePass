
![GitHub repo size](https://img.shields.io/github/repo-size/girisakar365/UrePass?color=gren&style=flat-square)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/girisakar365/UrePass?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/girisakar365/UrePass?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/girisakar365/UrePass?style=flat-square)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyqt5?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyqt5?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/girisakar365/UrePass?color=%234285F4&style=flat-square)

<img src="https://github.com/girisakar365/UrePass/blob/master/Screenshort/2.png?raw=true#gh-dark-mode-only" width=905 height=400 align=left/> 

<img src="https://github.com/girisakar365/UrePass/blob/master/Screenshort/1.png?raw=true#gh-light-mode-only" width=905 height=400 align=left> 

##### A Windows Based Password Manager.

`UrePass` is simple windows OS based password storing and managing application. It is a work-in-progress project that allows user to store and organize passwords.
<br>

### Disclaimer
This is <b>just a side hobby</b> project to learn and unwind my personal skills on different aspects of a software development upto deployment stage. I therefore <b><u>request the visiters NOT to see it as a production ready software or so on.</b></u>

## Table of Content:
|S.N | Topics|  
|----| ---- | 
| 1. |[Getting Started with UrePass](https://github.com/girisakar365/UrePass/blob/master/README.md#getting-stared-with-urepass)|
| 2. |[Flow of Files](https://github.com/girisakar365/UrePass/blob/master/README.md#flow-of-files)|
| 3. |[Contirbuting](https://github.com/girisakar365/UrePass/blob/master/README.md#contributing)|
| 4. |[App Teasure](https://github.com/girisakar365/UrePass/blob/master/README.md#app-teasure)|
| 5. |[Installation](https://github.com/girisakar365/UrePass/blob/master/README.md#installation)|
| 6. |[Issues](https://github.com/girisakar365/UrePass/blob/master/README.md#issues)|
| 7. |[Updates](https://github.com/girisakar365/UrePass/blob/master/README.md#updates)|
| 8. |[License](https://github.com/girisakar365/UrePass/blob/master/README.md#license)|

## Getting Stared with UrePass

You may clone the repo as you do normally. But the following versions must be fulfilled.

1. `Python >= 3.7`
2. `Pyqt5 >= 5.6`
3. `Cryptography >= 30.5.0.0`

## Flow of Files

<img src="https://github.com/girisakar365/UrePass/blob/master/Screenshort/Code%20base.png?raw=true" align=left\>
<br><br>

All the subfiles of `FrontEnd` have landed on `Ui` and all the subfile of BackEnd have landed on `Bridge`. However, some files class of `src` file needs to be imported on `Bridge` to extract necessary widget(Frames). Class of `DB` needs to imported on `Frontend` inorder to initialize the DB and check any faulty startups and fix it.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are <b>greatly appreciated</b>.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag `enhancement`. `Don't forget to give the project a star!`

#### Steps:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b branchName/fileName`)
3. Commit your Changes (`git commit -m 'changes made'`)
4. Push to the Branch (`git push origin branchName/fileName`)
5. Open a Pull Request

## App Teasure:
![image](https://github.com/girisakar365/UrePass/blob/master/Screenshort/Screenshot%202023-05-07%20004002.png?raw=true)

As shown above UrePass is a very simplistic yet a `strong password manager` with `great encruyption-decryption method`. It has a very `simplisitic yet appealing UI design`


## Installation
The installation process of this app is very simple. You just need to visit the link <b><u>[here](https://github.com/girisakar365/UrePass/blob/master/Installation.md)</b></u>. which will direct you to the drive. Download the installer and run the installation and you are done!

`Note: This a work-in-progress project. Thus, their might be some possible bugs in the application. Ready to depoly product will be approved soon!`

## Issues

`#RG-UA001` -> `issue: #1`
1. User token not recognized --> `Resolved`
2. Failed User login sessions --> `Resolved`
3. Failed to empty `current user` feild (DB) --> `Resolved`

## Updates

- To be done:
    1. `Introduce Dark mode`.
    2. `Add keybindings`.
    3. `Add more features to menu bar`

## License

Distributed under `Sakar Giri Production` License.
For more details please check `License.md` file <b><u>[here](https://github.com/girisakar365/UrePass/blob/master/LICENSE.md) </b></u>
