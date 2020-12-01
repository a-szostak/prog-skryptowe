"use strict";

var sumaTotal = 0;
main();

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}



function cyfry(napis){
	napis = napis.split('');
	var sumaCyfr = 0;
	for (var i=0; i < napis.length; i++){
		if (Number.isInteger(Number(napis[i]))){
			sumaCyfr = sumaCyfr + Number(napis[i]);
		}
	}
	return sumaCyfr;
}


function litery(napis){
	napis = napis.split('');
	var sumaLiter = 0;
	for (var i=0; i < napis.length; i++){
		if (!Number.isInteger(Number(napis[i]))){
			sumaLiter++;
		}
	}
	return sumaLiter;
}


function suma(napis){
	napis = napis.split('');
	for (var i=0; i < napis.length; i++){
		if (Number.isInteger(Number(napis[i]))){
			sumaTotal = sumaTotal + Number(napis[i]);
		}
		else{
			break;
		}
	}
	return sumaTotal;
}


function main(){
	var napis = window.prompt("Wpisz coś");
	while(napis != null){
		suma(napis);
		console.log(cyfry(napis) + ' ' + litery(napis) + ' ' + sumaTotal);
		napis = window.prompt("Wpisz coś");
	}
}

describe('The sum() function', function() {
 it('Returns 4 for 2+2', function() {
   expect(sum(2,2)).to.equal(4);
 });
 it('Returns 0 for -2+2', function() {
   expect(sum(-2,2)).to.equal(0);
 });
});

describe('The cyfry() function', function() {
	it('Returns 15 for "12345"', function() {
	  expect(cyfry('12345')).to.equal(15);
	});
	it('Returns 0 for "aaaaaaa"', function() {
		expect(cyfry('aaaaaaa')).to.equal(0);
	  });
	it('Returns 11 for "aaa146"', function() {
	  expect(cyfry('aaa146')).to.equal(11);
	});
	it('Returns 6 for "213bb"', function() {
		expect(cyfry('213bb')).to.equal(6);
	  });
	it('Returns 0 for ""', function() {
		expect(cyfry('')).to.equal(0);
	  });
   });


   describe('The litery() function', function() {
	it('Returns 0 for "12345"', function() {
		expect(litery('12345')).to.equal(0);
	  });
	  it('Returns 7 for "aaaaaaa"', function() {
		  expect(litery('aaaaaaa')).to.equal(7);
		});
	  it('Returns 3 for "aaa146"', function() {
		expect(litery('aaa146')).to.equal(3);
	  });
	  it('Returns 2 for "213bb"', function() {
		  expect(litery('213bb')).to.equal(2);
		});
	  it('Returns 0 for ""', function() {
		  expect(litery('')).to.equal(0);
		});
	 });


  describe('The suma() function', function() {
	it('Returns 15 for "12345"', function() {
		sumaTotal = 0;
		expect(suma('12345')).to.equal(15);
	  });
	  it('Returns 0 for "aaaaaaa"', function() {
		sumaTotal = 0;
		  expect(suma('aaaaaaa')).to.equal(0);
		});
	  it('Returns 0 for "aaa146"', function() {
		sumaTotal = 0;
		expect(suma('aaa146')).to.equal(0);
	  });
	  it('Returns 6 for "213bb"', function() {
		sumaTotal = 0;
		  expect(suma('213bb')).to.equal(6);
		});
	  it('Returns 0 for ""', function() {
		sumaTotal = 0;
		  expect(suma('')).to.equal(0);
		});
	 });
