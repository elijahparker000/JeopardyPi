const { app, BrowserWindow, screen, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');

let mainWindow;
let flaskProcess;

function createWindow() {
  const aspectRatio = 16 / 9;
  let windowWidth = 1280; // Specific width in pixels
  let windowHeight = windowWidth / aspectRatio;

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

app.on('ready', () => {
  const flaskAppPath = path.join(__dirname, '../flask_test/app.py');
  flaskProcess = exec(`python ${flaskAppPath}`, (err, stdout, stderr) => {
    if (err) {
      console.error(`exec error: ${err}`);
      return;
    }
  });

  flaskProcess.stdout.on('data', (data) => {
    console.log(`Flask: ${data}`);
  });

  flaskProcess.stderr.on('data', (data) => {
    console.error(`Flask: ${data}`);
  });

  flaskProcess.on('close', (code) => {
    console.log(`Flask process exited with code ${code}`);
  });

  createWindow();
});

app.on('window-all-closed', function () {
  if (flaskProcess) {
    flaskProcess.kill();
  }
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
