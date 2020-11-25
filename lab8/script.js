"use strict";

var expect = chai.expect;

function sum(x,y) {
	return x+y;
}

licz();

function cyfry(napis){
	napis = napis.split('');
	var suma = 0;
	for (var i=0; i < napis.length; i++){
		if (Number.isInteger(Number(napis[i]))){
			suma = suma + Number(napis[i]);
		}
	}
	return suma;
}


function litery(napis){
	napis = napis.split('');
	var suma = 0;
	for (var i=0; i < napis.length; i++){
		if (!Number.isInteger(Number(napis[i]))){
			suma++;
		}
	}
	return suma;
}


function licz(){
	var suma = 0;
	while(true){
		var napis = window.prompt("Wpisz coś");
		if (napis === null){
			break;
		}
		suma += cyfry(napis);
		console.log(cyfry(napis) + ' ' + litery(napis) + ' ' + suma);
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
