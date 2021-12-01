/*
  Модуль С3.4
  Задание 4
    Реализовать следующее консольное приложение подобно примеру, который разбирался в видео. 
    Реализуйте его на прототипах. Определить иерархию электроприборов. 
    Включить некоторые в розетку. Посчитать потребляемую мощность. 
    Таких приборов должно быть, как минимум, два (например, настольная лампа и компьютер). 
    Выбрав прибор, подумайте, какими свойствами он обладает.
*/

function Thing(name) {
  this.name = name;
  this.on = function() {
    console.log(`${this.name} is ACTIVATED`);
  }
  this.off = function() {
    console.log(`${this.name} is DEACTIVATED`);
  }
}

function Iron(weight, power) {
  this.weight = weight;
  this.power = power;
  this.print = function() {
    console.log(`${this.name} info:\n1) weight - ${this.weight}\n2) power - ${this.power}`);
  }
}

function Phone(brand, model, power) {
  this.brand = brand;
  this.model = model;
  this.power = power;
  this.print = function() {
    console.log(`${this.name} info:\n1) brand - ${this.brand}\n2) model - ${this.model}\n3) power - ${this.power}`);
  }
}

Iron.prototype = new Thing("Iron");
Phone.prototype = new Thing("Phone");

const iron = new Iron(5, 220);
const phone = new Phone("iPhone", "11 Max Pro", 5);

iron.print();
iron.on();
iron.off();

phone.print();
phone.on();
phone.off();
