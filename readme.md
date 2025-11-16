# Password Checker (Python)

A simple password-checking tool written in Python.
It evaluates password strength based on length and the presence of uppercase letters, lowercase letters, digits and special characters among others.

---

## Features

- Checks for minimum password length
- Detects:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
  - Patterns
  - Entropy
- Feedback describing why a password passes or fails

---

## Installation

Clone the repository:
```bash
git clone https://github.com/1Invicta/password_checker_py.git
cd password_checker_py
```

---

## Usage

#### Default

Run the password checker with CLI user interface:
```bash
python -m password_checker_py
```


#### Command-Line arguments

Check version:
```bash
python -m password_checker_py --version
```
or
```bash
python -m password_checker_py -v
```

Check a password:
```bash
python -m password_checker_py --password [password] --check-mode [1-3]
```
or
```bash
python -m password_checker_py -p [password] -cm [1-3]
```

Generate a password:
```bash
python -m password_checker_py --generate --check-mode [1-3]
```
or
```bash
python -m password_checker_py -g -cm [1-3]
```

Output results (in JSON format):
```bash
python -m password_checker_py -g -cm 2 --output
```
or
```bash
python -m password_checker_py -g -cm 2 -o
```

---

## Planned improvements

This is an evolving project. Upcoming updates may include:
* More rigorous password rules
* Improved CLI experience
* Possibly ports to C#, C and/or C++ later on

---

## About the project

I like to prototype tools in Python before moving to lower-level languages.
This project is part of my goal to build a larger "developer toolkit" over time.

---

## License

This project is licensed uder the Apache 2.0.
See the LICENSE file for details.
