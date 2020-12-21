var expect = require('chai').expect;
var module = require('../sync.js');


describe('The checkExistance() function', function() {
  
  it('Returns - File: <file\'s content>, if that file exists', function() {
    expect(module("testFile.txt")).to.equal("File:\nFile content for the test.");
  });
  it('Returns - Directory, if that directory exists', function() {
    expect(module("out")).to.equal("Directory");
  });
  it('Returns - Not found, if that file or directory does not exist', function() {
    expect(module("nananana")).to.equal("Not found");
  });
});