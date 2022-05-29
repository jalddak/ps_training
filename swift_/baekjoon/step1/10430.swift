import Foundation

let array = readLine()!.split(separator: " ").map{Int($0)!}
let A = array[0]
let B = array[1]
let C = array[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
