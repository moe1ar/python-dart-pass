abstract class Animals {
  printName();
  printSound();
}

class Dog extends Animals {
  @override
  printName() {
    print("Dog");
  }

  @override
  printSound() {
    print("dog sound");
  }
}

class Cat extends Animals {
  @override
  printName() {
    print("Cat");
  }

  @override
  printSound() {
    print("cat sound");
  }
}

class Cow extends Animals {
  @override
  printName() {
    print("Cow");
  }

  @override
  printSound() {
    print("cow sound");
  }
}

main() {
  Dog dog = Dog();
  dog.printName();
  dog.printSound();

  Cat cat = Cat();
  cat.printName();
  cat.printSound();

  Cow cow = Cow();
  cow.printName();
  cow.printSound();
}
