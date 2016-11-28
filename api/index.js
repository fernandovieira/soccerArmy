var Glue = require('glue');
var options = {
  relativeTo: __dirname 
};

Glue.compose(require('./config/manifest.json'), options, function (err, server) {
  server.start(function (err) {
    console.log("It´s working !!!")
  });
});
