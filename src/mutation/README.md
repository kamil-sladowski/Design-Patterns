1. Navigate to directory with calculator.py and test_calculator.py files
2. Clone and install MutPy library:
```
    $ git clone https://github.com/mutpy/mutpy
    $ cd mutpy/
    $ python3 setup.py install
```
3. Execute tests Mutation tests on provided files
```
$ bin/mut.py --target ../calculator.py --unit-test ../test_calculator.py --show-mutants
```
4. Output will present generated mutants and summary