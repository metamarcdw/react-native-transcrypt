### Example of React Native with Python using Transcrypt and Component.py
This project is adapted to Python from the "The Complete React Native and Redux Course" course created by Stephen Grider

First install Python>=3.6/pip, NodeJS/npm>=5.2, and Git:  
`sudo pacman -S python-pip npm git`  
Next, clone the repo  
`git clone https://github.com/metamarcdw/react-native-transcrypt`  
Set up your React/Transcrypt environment:  
(Use of a virtual environment is recommended but not required)  
```
mkvirtualenv transcrypt
pip install git+https://github.com/qquick/transcrypt@67c8b9#egg=transcrypt
pip install git+https://github.com/metamarcdw/Component.py@master#egg=Component_py

cd react-native-transcrypt/
npm install
```
We can now compile with Transcrypt and run using Expo XDE
```
npm run watch  
```
Open your device simulator and connect using Expo XDE
