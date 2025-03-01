import java.io.File
import kotlin.random.Random

fun main() {
    val words = mutableListOf<String>()
    //mutableListOf("p?ygoda;sz/rz/ż;rz;12;6", "mi?d;ó/u;ó;5;4", "p?czoła;rz/ż/sz;sz;6;2", "g?ra;u/ó;ó;10;2")
    val listOfWords = MutableList(0) { mutableListOf<String>() }
    val chosenWords = MutableList(0) { mutableListOf<String>() }

    val fileName = "slowa.txt"
    val file = File(fileName)
    file.forEachLine {
        words.add(it)
    }

    print("Podaj liczbę słów do powtórzenia: ")
	val numberOfWords = readln().toInt()
    
    for (word in words) {
        var cleanWord = word.split(";").toMutableList()
        
        //var allAnswers = cleanWord[3].toDouble()
        //var trueAnswers = cleanWord[4].toDouble()
        
        //cleanWord.add((trueAnswers / allAnswers).toString())
        
        listOfWords.add(cleanWord)
    }
    
    for (i in 1..numberOfWords) {
        var frac = 1.0
        var idx = 0
        for ((index, word) in listOfWords.withIndex()) {
            var rand = Random.nextDouble()
            var allAnswers = word[3].toDouble()
            var trueAnswers = word[4].toDouble()
            
            if (frac > rand - (trueAnswers / allAnswers) ) {
                frac = trueAnswers / allAnswers
                idx = index
            }
        }
        
        chosenWords.add(listOfWords[idx])
        listOfWords.removeAt(idx)
    }
    
    //println(chosenWords)
    
    while (chosenWords.isNotEmpty()) {
        var len = chosenWords.size
        var i = (0..len-1).random()
        
        println(chosenWords[i][0])
        println(chosenWords[i][1])
    
        chosenWords[i][3] = (chosenWords[i][3].toInt()+1).toString()
    
        var answer = readln()
        if (answer == chosenWords[i][2]) {
            println("Dobrze!\n")
            chosenWords[i][4] = (chosenWords[i][4].toInt()+1).toString()
            listOfWords.add(chosenWords[i])
            chosenWords.removeAt(i)
        } else {
            println("Źle!\n")
        }
    }
    
    println("Brawo! Odpowiedziano na wszystkie pytania.")
    
    file.writeText("")
    for (word in listOfWords){
        var lastIndex = word.size-1
        for ((index, element) in word.withIndex()) {
            file.appendText("$element")
            if (index != lastIndex) file.appendText(";")
        }
        file.appendText("\n")
    }
    
    //println(listOfWords)
    
}
