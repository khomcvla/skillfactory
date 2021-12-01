/*
  Модуль С3.5
  Задание 5
    Переписать консольное приложение из предыдущего юнита на классы.
*/

class Thing {
  constructor(name, power) {
    this.name = name;
    this.power = power;
  }
  
  on() { console.log(`${this.name} is ACTIVATED`); }
  off() { console.log(`${this.name} is DEACTIVATED`); }
}

class Iron extends Thing {
  constructor(name, weight, power) {
    super(name, power);
    this.weight = weight;
  }
  
  print() { console.log(`${this.name} info:\n1) weight - ${this.weight}\n2) power - ${this.power}`); }
}

class Phone extends Thing {
  constructor(name, brand, model, power) {
    super(name, power);
    this.brand = brand;
    this.model = model;
  }
  
  print() { console.log(`${this.name} info:\n1) brand - ${this.brand}\n2) model - ${this.model}\n3) power - ${this.power}`); }
}

const iron = new Iron("Iron", 5, 220);
const phone = new Phone("Phone", "iPhone", "11 Max Pro", 5);

iron.print();
iron.on();
iron.off();

phone.print();
phone.on();
phone.off();
