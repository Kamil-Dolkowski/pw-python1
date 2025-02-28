
fun main() {
	val numberOfWords = readln().toInt()
    val words = listOf("p?ygoda;sz/rz/ż;rz;12;6", "mi?d;ó/u;ó;5;4")
    val listOfWords = MutableList(0) { listOf<String>() }
    val chosenWords = MutableList(0) { listOf<String>() }
    
    for ((index, word) in words.withIndex()) {
        //println("$index $word")
        var cleanWord = words[index].split(";")
        //var options = cleanWord[1].split("/")
        listOfWords.add(cleanWord)
    }
    
    //println(listOfWords[0])
    
    for (i in 1..numberOfWords) {
        var frac = 1 
        var idx = 0
        for ((index, word) in listOfWords.withIndex()) {
            var allAnswers = word[3].toInt()
            var trueAnswers = word[4].toInt()
            
            if (frac < trueAnswers / allAnswers) {
                frac = trueAnswers / allAnswers
                idx = index
            }
            
        }
        
        chosenWords.add(listOfWords[idx])
    }
    
    println(chosenWords)
    
}
