# java fragment


          import java.util.stream.IntStream;

          private List<String> generatePasswordList() {
            int numPasswords = flags.get(GENERATED_PASSWORD_COUNT);
            int passwordLength = (int) Math.ceil(Math.log10(numPasswords));
            return IntStream.range(0, numPasswords)
                .mapToObj(i -> String.format("%0" + passwordLength + "d", i))
                .collect(Collectors.toList());
          }


# run the code

    kotlinc gen_list.kt -d hello.jar
