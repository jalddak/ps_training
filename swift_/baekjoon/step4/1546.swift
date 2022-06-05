import Foundation

let N = Double(readLine()!)!
let array = readLine()!.split(separator: " ").map{Double($0)!}

let max_value = array.max()!
var new_sum = 0.0

for i in array{
    new_sum += i / max_value * 100
}
print(new_sum/N)
