# Link

https://stackoverflow.com/questions/60922349/undefined-reference-to-a-function-c


# Finding


g++ main.cpp gives this error

        Undefined symbols for architecture x86_64:
          "requestVariables(short, short, short)", referenced from:
              _main in main-bc7261.o
        ld: symbol(s) not found for architecture x86_64

but `g++ -c main.cpp` won't
