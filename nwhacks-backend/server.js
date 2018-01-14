var express = require('express'); //import express framework
var mongodb = require('mongodb');
var mydb;
var pdb;
var idb;

var app = express() //app is using the express framework
var uri = 'mongodb://chickenlittle:butter@ds255797.mlab.com:55797/population_db';

var generalJSON = [];
var specializedJSON = [];

var cfenv = require("cfenv")//

var appEnv = cfenv.getAppEnv() 
// start the server on the given port and binding host, and print
// url to server when it starts

app.listen(appEnv.port, '0.0.0.0', function() {
    console.log("server starting on " + appEnv.url)
});
mongodb.MongoClient.connect(uri, function(err, db) {
  
  if(err) throw err;
  console.log("success");
  /*
   * First we'll add a few songs. Nothing is required to create the 
   * songs collection; it is created automatically when we insert.
   */
  mydb = db.db('population_db');
  pdb = mydb.collection('population_db');
  idb = mydb.collection('individual_db')
   console.log("connect success!!!!");
} );

app.get('/', function(req, res){
  console.log('CALLED')
  res.send('HI');//image should be a url
})

app.get('/api/UpdateQ', function(req, res){
  res.set("Access-Control-Allow-Origin", "*");
  console.log('CALLED update')

//Extract last 5 entries from individual_db
idb.find({}).limit(5).toArray(function (err, docs) {

  //Use child_process to run a Python script --> does inference based on last 5 entries in individual DB
  var spawn = require("child_process").spawn;
  var process = spawn('python', ['VitalsLSTM.py', 'infer', docs, 'model.json', 'model.h5']);

  //Listen for output from python script --> if output is not null, generate new DB entry
  process.stdout.on('data', function (data) {
    console.log('done')
    return res.json(data);
  }, this);

  console.log('hello')

});

/*
pdb.find( {Classification:3}).limit(10).toArray(function(err, docs) {
  return res.json(docs)
}, this);
*/
})