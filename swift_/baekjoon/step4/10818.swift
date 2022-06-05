import Foundation

let N = Int(readLine()!)!

let array = readLine()!.split(separator: " ").map{Int($0)!}

var sorted_array = array.sorted()
print("\(sorted_array[0]) \(sorted_array[sorted_array.count-1])")
