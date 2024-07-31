// main.js
const { app, BrowserWindow } = require('electron')
const path = require('path')
const { exec } = require('child_process')

let mainWindow

function createWindow () {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  mainWindow.loadURL('http://localhost:5000')

  mainWindow.on('closed', function () {
    mainWindow = null
  })
}

app.on('ready', () => {
  exec('python ../flask_test/app.py', (err, stdout, stderr) => {
    if (err) {
      console.error(`exec error: ${err}`)
      return
    }
    console.log(`stdout: ${stdout}`)
    console.error(`stderr: ${stderr}`)
  })
  createWindow()
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})
