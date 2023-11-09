const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow

let mainWindow = null

app.on('window-all-closed',()=>{
	app.quit()
})

app.on('ready',()=>{
	//call python
	const subpy 	= require('child_process').spawn('python',['./core/app.py'])
	const req 		= require('request-promise')
	const mainAddr	= 'http://localhost:1337'

	const openWindow = ()=>{
		mainWindow = new BrowserWindow({
			width:800,height:600,
			webPreferences: {
			  nodeIntegration: false,
			  preload: './preload.js'
    		}
		})
		mainWindow.loadURL(mainAddr)
		mainWindow.on('closed',()=>{
			mainWindow = null,
			subpy.kill('SIGINT')
		})
	}

	const startUp = ()=>{
		req(mainAddr).then((htmlString)=>{
			console.log('Server Started!')
			openWindow()
		}).catch((err)=>{
			startUp()
		})
	}

	startUp()
})