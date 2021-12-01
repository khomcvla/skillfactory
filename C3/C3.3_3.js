/*
  Модуль С3.3
  Задание 3
    Написать функцию, которая создает пустой объект, но без прототипа.
*/

function newObjectNullProto() {
  return Object.create(null);
}

const obj = newObjectNullProto();
console.log(obj.prototype === undefined);
