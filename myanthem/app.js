var fs = require('fs');
var express = require('express');
var app = module.exports.app = express();
var server = require('http').createServer(app);
var io = require('socket.io').listen(server);
var port = process.env.PORT || 3000;
var PythonShell = require('python-shell');

server.listen(port);

app.use('/public', express.static('public'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) { 

  socket.on('buttonPush', function (response) {
    PythonShell.run('../sample.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
    });
  });

  function handleError(error) {
    console.log(error);
  }

});
