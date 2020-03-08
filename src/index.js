const {app, BrowserWindow, Menu} = require('electron');

const url = require('url');
const path = require('path');

let mainWindow
let newObjectWindow

/**Este condicional hace que esta parte del codigo solo se ejecute cuando la
 * aplicacion se encuentra en etapa de desarrollo
 */
if(process.env.NODE_ENV !== 'production'){
    /**Este modulo nos permite que los cambiaos que hagamos en nuestro proyecto
     * lo podamos visualizar en tiempo real
     */
    require('electron-reload')(__dirname, {
        electron: path.join(__dirname, '../node_modules', '.bin', 'electron')
    });
}

/**Este es el evento que al iniciar la aplicacion se ejecuta
 * y asi crear todo lo que podemos ver en la ventana
 */
app.on('ready', () => {
    //creando una nueva ventana
    mainWindow = new BrowserWindow({
        title: 'Cannis',
        icon: path.join(__dirname, 'assets/img/icons8-jake-48.png'),
        webPreferences: {
            nodeIntegration: true
        },
    })
    //cargando 
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'views/index.html'),
        protocol: 'file',
        slashes: true
    }))

    //Creando un menu de aplicacion custrom
    const mainMenu = Menu.buildFromTemplate(templateMenu);
    Menu.setApplicationMenu(mainMenu);

    //Cerrar la toda la aplicacion cuando se cierra la ventana principal
    mainWindow.on('close', () => {
        app.quit();
    })

});

//Estructura para el menu de aplocacion
const templateMenu = [
    {
        label: 'File',
        submenu: [
            {
                label: 'New Object',
                accelerator: 'Ctrl+O',
                click(){
                    createNewObjectWindow();
                }
            },
            {
                label: 'Remove ALL Products',
                click(){

                }
            },
            {
                label: 'Exit',
                accelerator: process.platform == 'darwin' ? 'command+Q' : 'Ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]
    },
];

function createNewObjectWindow(){
    newObjectWindow = new BrowserWindow({
        width: 400,
        height: 300,
        title: 'Add a New Object'
    });
    newObjectWindow.setMenu(null);
    newObjectWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'views/newObjectWindow.html'),
        protocol: 'file',
        slashes: true
    }));
    newObjectWindow.on('close', () => {
        newObjectWindow = null;
    })
}

//Añadiendo el nombre al inicio del menu en MacOS
if(process.platform === 'darwin'){
    templateMenu.unshift({
        label: app.getName()
    });
}

//Añadiendo opciones de desarrollador en etapas de desarrollo
if(process.env.NODE_ENV !== 'production'){
    templateMenu.push({
        label: 'DevTools',
        submenu: [
            {
                label: 'Show/Hide Dev Tools',
                accelerator: 'Ctrl+D',
                click(item, focusedWindow){
                    focusedWindow.toggleDevTools();
                }
            },
            {
                role: 'reload'
            }
        ]
    });
}