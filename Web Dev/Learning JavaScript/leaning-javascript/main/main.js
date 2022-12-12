//so it doesn't do silly things
"use strict";

function giveMeYourName() {
  //prompt makes an input box pop up
  //the first part is the text, and the second is the default that is already in the text box
  let name = prompt("What is your name?", "John");
  let enjoyment = confirm(
    `Hello There ${name}. Are you enjoying your time here?`
  );
  if (enjoyment == true) {
    alert(
      "That is.... Good. Next, I need you to answer me a few more questions"
    );
  } else {
    alert("Well, that is a shame, isn't it?");
    alert("Goodbye");
    window.close();
  }
}

function addition() {
  let num1 = prompt("First Number");
  let num2 = prompt("Second Number");
  if ((num1 = (9 && num2 == 10) || (num1 == 10 && num2 == 9))) {
    alert("21!");
  } else {
    alert(+num1 + +num2);
  }
}

function justTheNonsense() {
  //makes pop-up
  alert("I'm JavaScript!");

  //logs to the dev console
  console.log("This is using an external js file");

  //sets variables
  let name = "John";
  let admin = " ";

  //sets the var admin to the same as name
  admin = name;

  //"prints" the value of the var admin
  alert(admin);

  //sets the var planetName to 'Earth'
  let planetName = "Earth";

  //sets the var siteVisitor to 'John'
  let siteVisitor = "John";

  //the backticks replacing the quotation marks give added functionality, allowing for displaying expressions or variables
  alert(`And the result is ${1 + 3}`);

  //confirm creates a modal box, with a 'Cancel', and an 'OK' button
  //pressing 'Cancel' gives the value false, and 'OK' gives true
  let isHuman = confirm("Are you a human?");
  alert(isHuman);

  let a = 2;
  let b = 3;

  let result = a + b < 4 ? "Below" : "Over";
}

function nameOfJavascript() {
  let ans = prompt('What is the "offical" name of Javascript?', "");
  if (ans == "ECMAScript") {
    alert("Right!");
  } else {
    alert("Didn't know? ECMAScript!");
  }
}

function numberChecker() {
  let num = prompt("Please enter a number, between -100 and -100", "0");
  if (num > 0) {
    alert("1");
  } else if (num < 0) {
    alert("-1");
  } else if (num == 0) {
    alert("0");
  }
}

function officeHours() {
  let isWeekend = confirm("Is it the weekend? [OK for yes, Cancel for no]")
  let hour = prompt("What is the hour in 24hr format?", "");

  if (hour >= 9 && hour <= 17 && isWeekend != false) {
    alert("The office is open!");
  } else {
    alert("Sorry, the office is shut");
  }
}

function ageChecker() {
  let age = prompt("What is your age?", "")

  if (age >= 14 && age <= 90) {
    alert("Your age is between 14 and 90!")
  }
}
