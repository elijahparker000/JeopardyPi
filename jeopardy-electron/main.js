const { app, BrowserWindow, screen, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');
const http = require('http');

let controlWindow;
let playerWindow;
let flaskProcess;

function createWindows() {
  const displays = screen.getAllDisplays();
  
  const playerDisplay = displays[0];
  const controlDisplay = displays[1] || displays[0];

  controlWindow = new BrowserWindow({
    width: controlDisplay.size.width,
    height: controlDisplay.size.height,
    x: controlDisplay.bounds.x,
    y: controlDisplay.bounds.y,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  playerWindow = new BrowserWindow({
    width: playerDisplay.size.width,
    height: playerDisplay.size.height,
    x: playerDisplay.bounds.x,
    y: playerDisplay.bounds.y,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  const retryInterval = 500;
  const maxRetries = 20;
  let retries = 0;

  const tryLoading = () => {
    if (retries >= maxRetries) {
      console.error('Failed to connect to Flask server');
      return;
    }

    http.get('http://localhost:5000', (res) => {
      if (res.statusCode === 200) {
        controlWindow.loadURL('http://localhost:5000/');
        playerWindow.loadURL('http://localhost:5000/title_video_p');

        controlWindow.setMenuBarVisibility(false);
        controlWindow.on('closed', function () {
          controlWindow = null;
        });

        playerWindow.setMenuBarVisibility(false);
        playerWindow.on('closed', function () {
          playerWindow = null;
        });

      } else {
        retries++;
        setTimeout(tryLoading, retryInterval);
      }
    }).on('error', () => {
      retries++;
      setTimeout(tryLoading, retryInterval);
    });
  };

  tryLoading();
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

  createWindows();
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
  if (controlWindow === null || playerWindow === null) {
    createWindows();
  }
});

// Handle the navigation request from the control window
ipcMain.on('navigate-player', (event, url) => {
  if (playerWindow) {
    playerWindow.loadURL(url);
  }
});
