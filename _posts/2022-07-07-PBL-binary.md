---
toc: true
layout: post
description: PBL BInary File
categories: [markdown, Week 13]
title: PBL Binary File
---

### Hack #1 - Click the below button to randomly generate a number and convert to Binary, Hex, Decimal and Octal.

<button name="button" onclick="getRandomBinaryHack1()" style="background-color:green; border-color:blue; color:white">Generate the next random number to convert!!!</button>
<br/>

<p id="randomBinary" style="background-color:yellow; color:black">Binary.</p>
<p id="randomDecimal" style="background-color:red; color:black">Decimal.</p>
<p id="randomOctal" style="background-color:green; color:black">Octal.</p>
<p id="randomHex" style="background-color:orange; color:black">Hex.</p>
<br/><br/><br/><br/>
### Hack #2 - Click the below button to randomly generate a number and convert to hex, decimal to set color.
<button name="button" onclick="getRandomBinaryHack2()" style="background-color:green; border-color:blue; color:white">Generate the next random number to change color!!!</button>
<br/>
<p id="colorBox" style="background-color:purple; color:black">The Color changes</p>
<p id="colorBoxHex"></p>
<br/><br/><br/><br/>
### Hack #3 - Click the below buttons to flip the bits and convert to diffetent formats.
<button name="button" onclick="displayBits()" style="background-color:green; border-color:blue; color:white">Display Bits to flip!!!</button>
<p id="randomBinaryP" style="background-color:orange; color:black">Binary.</p>
<p id="randomHexP" style="background-color:orange; color:black">Hex.</p>
<p id="randomDecimalP" style="background-color:orange; color:black">Decimal.</p>
<p id="randomOctalP" style="background-color:orange; color:black">Octal.</p>

<table style="width:100%">
  <tr>
    <td><button id="tbit7" onclick="bitToggle(7)" >Toggle</button></td>
    <td><button id="tbit6" onclick="bitToggle(6)" >Toggle</button></td>
    <td><button id="tbit5" onclick="bitToggle(5)" >Toggle</button></td>
    <td><button id="tbit4" onclick="bitToggle(4)" >Toggle</button></td>
    <td><button id="tbit3" onclick="bitToggle(3)" >Toggle</button></td>
    <td><button id="tbit2" onclick="bitToggle(2)" >Toggle</button></td>
    <td><button id="tbit1" onclick="bitToggle(1)" >Toggle</button></td>
    <td><button id="tbit0" onclick="bitToggle(0)" >Toggle</button></td>
    
  </tr>
  <tr>
    <td id="bit0">1</td>
    <td id="bit1">0</td>
    <td id="bit2">1</td>
    <td id="bit3">1</td>
    <td id="bit4">0</td>
    <td id="bit5">1</td>
    <td id="bit6">1</td>
    <td id="bit7">0</td>
  </tr>
</table>

<script>
// this function is called upon button click
function getRandomBinaryHack1() {
	var time = new Date().getMilliseconds(); //get current time
	var random = time % 100; // get the value < 100
	var val = random;					       

    document.getElementById("randomBinary").innerHTML = "Binary: " + random.toString(2); 
    document.getElementById("randomDecimal").innerHTML = "Decimal: " + random.toString(10); 
    document.getElementById("randomOctal").innerHTML = "Octal: " + random.toString(8); 
    document.getElementById("randomHex").innerHTML = "Hexadecimal: 0x" + random.toString(16);
	
}
						       
// this function is called upon button click
function getRandomBinaryHack2() {
	var time = new Date().getMilliseconds(); //get current time
	var val = time % 100; // get the value < 100
	var hex = val.toString(16);
	
	// Set color					     
    document.getElementById("colorBox").style.backgroundColor = `rgb(${val}, ${val}, ${val})`;
    document.getElementById("colorBox").innerHTML = "Color Code: rgb(" + val + "," + val + "," + val + ")";
    document.getElementById("colorBoxHex").innerHTML = "Hex#" + hex + hex + hex;
}
						       
var gDecimal = 14;
function displayBits() {
    //decimal = 10; //101
    var binary = "";
    //document.write("Hello, Coding Ground!");
    //while (decimal > 0) {
    decimal = gDecimal;
    for (i = 7; i > -1; i--) {
       bitid = "bit" + i;
       
       if (decimal & 1) {
          binary = "1" + binary;
          document.getElementById(bitid).innerHTML = "1";
       } else {
          binary = "0" + binary;
          document.getElementById(bitid).innerHTML = "0";
       }
       decimal = decimal >> 1;
    }
   document.getElementById("randomBinaryP").innerHTML = "Binary: " + binary;
   document.getElementById("randomHexP").innerHTML = "Hexadecimal: 0x" +gDecimal.toString(16);
   document.getElementById("randomOctalP").innerHTML = "Octal: " + gDecimal.toString(8);
   document.getElementById("randomDecimalP").innerHTML = "Decimal: " + gDecimal.toString(10);
}
function bit_test(num, bit){
    return ((num>>bit) % 2 != 0)
}

function bit_set(num, bit){
    return num | 1<<bit;
}

function bit_clear(num, bit){
    return num & ~(1<<bit);
}

function bitToggle(bit){
    num = gDecimal;
    gDecimal = bit_test(num, bit) ? bit_clear(num, bit) : bit_set(num, bit);
    //gDecimal = bit_set(num, bit);
    displayBits();
	document.getElementById("randomDecimalP").innerHTML = "Decimal: " + gDecimal.toString(10);
    return decimal;
}
	
</script>


```
Here is my logic to convert decimal to binary
− Create an empty string and a decimal number.
− Iterate through the decimal number while it is greater than 0.
− To get the last bit of the decimal number, perform bitwise & operation of 1 with decimal number. If the last bit is 1, append “1” in the front of the binary string. Otherwise, append ‘0’ in the front of the binary string.
− Remove the last bit from the decimal number using the right shift operator.
Example 
decimal = 5; //101
while (decimal > 0) {
   if (decimal & 1) {
      binary = "1" + binary;
   } else {
      binary = "0" + binary;
   }
   decimal = decimal >> 1;
}
```