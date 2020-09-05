"use strict";

const express = require("express");
const bodyParser = require("body-parser");

class App {
    constructor() {
        this.app = express();
        this.setMiddleWare();
        this.setStatic();
        this.setRouting();
        //this.setViewEngine();
    }
    setStatic() {
        //this.app.use('/css', express.static('css'));
        //this.app.use('/images', express.static('images'));
        //this.app.use('/js', express.static('js'));
        //this.app.use('/fonts', express.static('fonts'));
    }
    setRouting() {
        this.app.get('', (req, res) => {
            res.render('index.html');
        });
        //this.app.use('/emissions', emissions_1.emissionsRouter);
        //this.app.use('/login', login_1.loginRouter);
        //this.app.use('/data-input', datainput_1.dataInputRouter);
    }
    setMiddleWare() {
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: false }));
    }
}

app = new App();
const port =3520;
app.lesten(port, ()=>{
    console.log("Express listening on port : ", port);
})