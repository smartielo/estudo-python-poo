# Python OOP Studies

A small learning repository for practicing **Object-Oriented Programming (OOP) in Python**.

The examples are organized by class date and exercise. They cover core OOP concepts such as abstract classes, inheritance, method overriding, decorators, and automated tests with `pytest`.

## What is inside?

```text
.
├── aula10-09/                 # Abstract classes and geometric figures
│   ├── run.py
│   └── run2.py
├── aula17-09/                 # Space for class exercises and tests
│   └── test.py
├── exercicio-revisao/         # Notification exercise
│   ├── notificacao.py
│   └── tests/
│       └── test_notificacao.py
├── exercicios/                # Additional practice exercises
│   ├── ex1/
│   ├── ex2/
│   └── ex3/
└── conteudos-prova/           # Study material for the exam
```

## Concepts practiced

- Abstract base classes with `ABC` and `@abstractmethod`
- Inheritance and constructor reuse with `super()`
- Polymorphism through different implementations of the same method
- Decorators with `functools.wraps`
- Encapsulation of shared behavior in base classes
- Unit testing with `pytest`

## Getting started

Make sure Python 3.10+ is installed, then clone the repository and open its directory:

```bash
git clone <repository-url>
cd estudo-python-poo
```

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the test dependency:

```bash
python -m pip install pytest
```

## Run the notification example

The notification exercise demonstrates a shared abstract contract implemented by e-mail and SMS notifications. A decorator logs the beginning and end of each send operation.

```bash
python exercicio-revisao/notificacao.py
```

## Run the tests

Run the test suite from the exercise directory so that the local module can be imported directly:

```bash
cd exercicio-revisao
python -m pytest
```

The tests check notification delivery, displayed data, and the rule that the abstract `Notificacao` class cannot be instantiated directly.

## Learning goal

This repository is intentionally simple: each folder is a focused experiment that makes it easier to connect Python syntax with OOP design principles. As the exercises evolve, the examples can be refactored into more complete and reusable applications.