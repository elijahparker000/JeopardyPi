const { app, BrowserWindow, screen, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');

let mainWindow;
let secondWindow;

function createWindow() {
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;

  const aspectRatio = 16 / 9;
  let windowWidth = width;
  let windowHeight = width / aspectRatio;

  if (windowHeight > height) {
    windowHeight = height;
    windowWidth = height * aspectRatio;
  }

  mainWindow = new BrowserWindow({
    width: windowWidth,
    height: windowHeight,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadURL('http://localhost:5000');
  mainWindow.setAspectRatio(aspectRatio);
  mainWindow.setMenuBarVisibility(false);
  //mainWindow.maximize();

  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

function createSecondWindow() {
  const displays = screen.getAllDisplays();
  const externalDisplay = displays.find((display) => display.bounds.x !== 0 || display.bounds.y !== 0);

  if (externalDisplay) {
    const { width, height } = externalDisplay.workAreaSize;

    const aspectRatio = 16 / 9;
    let windowWidth = width;
    let windowHeight = width / aspectRatio;

    if (windowHeight > height) {
      windowHeight = height;
      windowWidth = height * aspectRatio;
    }

    secondWindow = new BrowserWindow({
      x: externalDisplay.bounds.x,
      y: externalDisplay.bounds.y,
      width: windowWidth,
      height: windowHeight,
      frame: false,
      webPreferences: {
        nodeIntegration: true,
        contextIsolation: false
      }
    });

    secondWindow.loadURL('http://localhost:5000/second');
    secondWindow.setAspectRatio(aspectRatio);
    secondWindow.setMenuBarVisibility(false);
    secondWindow.maximize();

    secondWindow.on('closed', function () {
      secondWindow = null;
    });
  } else {
    console.error('No external display found');
  }
}

app.on('ready', () => {
  const flaskAppPath = path.join(__dirname, '../flask_test/app.py');
  exec(`python ${flaskAppPath}`, (err, stdout, stderr) => {
    if (err) {
      console.error(`exec error: ${err}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
  createWindow();
  createSecondWindow();
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});

ipcMain.on('message', (event, arg) => {
  if (secondWindow) {
    secondWindow.webContents.send('message', arg);
  }
});
