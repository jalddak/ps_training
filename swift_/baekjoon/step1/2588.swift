import Foundation

let first = Int(readLine()!)!
let second = Int(readLine()!)!

let second_1 = second % 10
let second_2 = second / 10 % 10
let second_3 = second / 100 % 10

print(first * second_1)
print(first * second_2)
print(first * second_3)
print(first * second)
