//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

const assert = require('assert');

describe('GET /', function () {
      it('Variables from source code', function (done) {
            server
                  .get('/')
                  .expect('Content-Type', /html/)
                  .end(function (err, res){
                        if (err) throw (err);
                        assert(res.body, '<h1>1 + 2 = 3</h1>');
                        done();
                  })
      });
});

describe('GET /add/x/y', function () {
      it('Variables from URL', function (done) {
            server
                  .get('/add/6/8')
                  .expect('Content-Type', /html/)
                  .end(function (err, res) {
                        if (err) throw (err);
                        assert(res.body, '<h1>6 + 7 = 14</h1>');
                        done();
                  })
      })
});