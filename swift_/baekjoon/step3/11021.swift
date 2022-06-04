import Foundation

let N = Int(readLine()!)!

for i in 1...N{
    let array = readLine()!.split(separator: " ").map{Int($0)!}
    let A = array[0]
    let B = array[1]
    print("Case #\(i): \(A+B)")
}
