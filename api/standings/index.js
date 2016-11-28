exports.register = function (server, options, next) {

  server.route({
    path: '/standings/',
    method: 'GET',
    handler: require('./service.js')
  });

  next();

};

exports.register.attributes = {
  pkg: require('./package.json')
};
