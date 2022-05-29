import Foundation

let array = readLine()!.split(separator: " ").map{Float64($0)!}
print(array[0] / array[1])
