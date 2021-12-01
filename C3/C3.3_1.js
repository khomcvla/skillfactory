/*
  Модуль C3.3
  Задание 1
    Написать функцию, которая принимает в качестве аргумента объект 
    и выводит в консоль все ключи и значения только собственных свойств. 
    Данная функция не должна возвращать значение.
*/

const human = {
  planet: "Earth",
  printHuman: function() {
    console.log("Human lives on earth")
  }
}

const man = {
  sex: "Man",
  printMan: function() {
    console.log("Human lives on earth")
  }
}

Object.setPrototypeOf(man, human);

function printOwnProp(obj) {
  for (let p in obj) {
    if (obj.hasOwnProperty(p)) console.log(p);
  }
}

printOwnProp(man);
