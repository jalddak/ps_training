import Foundation

var set = Set<Int>()

for _ in 1...10{
    let N = Int(readLine()!)!
    let remain = N % 42
    set.insert(remain)
}
print(set.count)
