# pythonDesignPatterns
This repository holds the implementation of various Design Patterns using Python

A. Creational
Creational patterns are ones that create objects for you, rather than having you instantiate objects directly. This gives your program more flexibility in deciding which objects need to be created for a given case.

1. Abstract factory pattern groups object factories that have a common theme.
2. Builder pattern constructs complex objects by separating construction and representation.
3. Factory method pattern creates objects without specifying the exact class to create.
4. Prototype pattern creates objects by cloning an existing object.
5. Singleton pattern restricts object creation for a class to only one instance.

B. Structural
These concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.

1. Adapter allows classes with incompatible interfaces to work together by wrapping its own interface around that of an already existing class.
2. Bridge decouples an abstraction from its implementation so that the two can vary independently.
3. Composite composes zero-or-more similar objects so that they can be manipulated as one object.
4. Decorator dynamically adds/overrides behaviour in an existing method of an object.
5. Facade provides a simplified interface to a large body of code.
6. Flyweight reduces the cost of creating and manipulating a large number of similar objects.
7. Proxy provides a placeholder for another object to control access, reduce cost, and reduce complexity.

C. Behavioral
Most of these design patterns are specifically concerned with communication between objects.

1. Chain of responsibility delegates commands to a chain of processing objects.
2. Command creates objects which encapsulate actions and parameters.
3. Interpreter implements a specialized language.
4. Iterator accesses the elements of an object sequentially without exposing its underlying representation.
5. Mediator allows loose coupling between classes by being the only class that has detailed knowledge of their methods.
6. Memento provides the ability to restore an object to its previous state (undo).
7. Observer is a publish/subscribe pattern which allows a number of observer objects to see an event.
8. State allows an object to alter its behavior when its internal state changes.
9. Strategy allows one of a family of algorithms to be selected on-the-fly at runtime.
10. Template method defines the skeleton of an algorithm as an abstract class, allowing its subclasses to provide concrete behavior.
11. Visitor separates an algorithm from an object structure by moving the hierarchy of methods into one object.

Reference : wikipedia
