import java.util.stream.*;


fun generateKeywordList() {
    val numKeywords = 100000.0
    val passwordLength = Math.ceil(Math.log10(numKeywords))
    return IntStream.range(0, numKeywords)
        .mapToObj(i -> String.format("%0" + passwordLength + "d", i))
        .collect(Collectors.toList());
  }


fun main(args: Array<String>) {
    println(generateKeywordList())
}
