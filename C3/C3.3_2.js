/*
  Модуль С3.3
  Задание 2
    Написать функцию, которая принимает в качестве аргументов строку и объект, 
    а затем проверяет есть ли у переданного объекта свойство с данным именем. 
    Функция должна возвращать true или false.
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
    console.log("Man lives on earth")
  }
}

Object.setPrototypeOf(man, human);

function hasProperty(str, obj) {
  return str in obj;
}

console.log(hasProperty("test", man));
console.log(hasProperty("sex", man));
