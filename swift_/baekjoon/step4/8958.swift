import Foundation

let N = Int(readLine()!)!

for _ in 1...N{
    var score = 0
    var before = 0
    let quiz = readLine()!
    for i in quiz{
        if i == "O"{
            before += 1
            score += before
        }
        else{
            before = 0
        }
    }
    print(score)
}

