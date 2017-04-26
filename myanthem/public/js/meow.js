var socket = io();

function myAnthem() {
  socket.emit('buttonPush');
}
