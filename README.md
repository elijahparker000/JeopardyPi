# JeopardyPi

## How to run flask GUI with electron
### Install flask
```
pip install flask
```
To test it, you can navigate to the flask_test directory and run app.py and the terminal should provide you with a link you can open in your browser to see the GUI. Next, we want to run that GUI in a window rather than a browser.

### Install Node.js
Install Node.js from nodejs.org
Next, navigate to the jeopardy-electron directory and run these three commands:
```
npm init -y
```
```
npm install electron
```
```
npm start
```
You should see the same GUI as before but this time in a window! 
If you run into any issues just copy and paste these instructions into ChatGPT and tell it where you're having trouble. 



## Important PyQt5 commands:

Converting resources file into .py file so python can use them
```
pyrcc5 -o resources_rc.py resources.qrc
```

Converting .ui files generated by QtDesigner into .py files
```
pyuic5 -o output_file.py input_file.ui
```



