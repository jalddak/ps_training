import Foundation

let array = readLine()!.split(separator: " ").map{Int($0)!}

let X = array[1]

let A = readLine()!.split(separator: " ").map{Int($0)!}

for i in A{
    if i < X{
        print(i, terminator: " ")
    }
}
