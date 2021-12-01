/* 
  Модуль C3.2
  Задание 0
    1. Создайте пустой объект; 
    2. Добавьте несколько свойств со значениями разных типов;
    3. Добавьте метод;
    4. Удалите одно из созданных свойств. 
*/

const weapon = {};

weapon.name = "Pistol";
weapon.ammo = 7;
weapon.isActive = true;
weapon.doShot = () => console.log("Pew! Pew! Pew!");

weapon.doShot();

console.log("----Before DELETE----");
for (prop in weapon) console.log(`weapon[${prop}] = ${weapon[prop]}`);

delete weapon.name;

console.log("-----After DELETE-----");
for (prop in weapon) console.log(`weapon[${prop}] = ${weapon[prop]}`);
