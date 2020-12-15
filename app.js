const fs = require('fs')
const { exec } = require('child_process')
var express = require('express');
var app = express();
const bodyParser = require('body-parser');

app.get('/', function (req, res) {
   res.sendFile( __dirname + '/' + 'index.html' );
})

app.use(bodyParser.urlencoded({ extended: true }));
app.post('/test', function (req, res) {

	query = req.body.q
	allergens = req.body.a
	
   exec('python3 main.py \''+ query +'\' \''+allergens+'\' ', (error, stdout, stderr) => {
     var result = stdout

     res.send(result)

	});
})

var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log('Example app listening at http://%s:%s', host, port)
})