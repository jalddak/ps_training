import Foundation

let N = Int(readLine()!)!

let digit: Double = pow(10, 3) // 10의 3제곱

for _ in 1...N{
    let array = readLine()!.split(separator: " ").map{Int($0)!}
    var sum = 0
    for i in 1...array[0]{
        sum += array[i]
    }
    let mean = Double(sum) / Double(array[0])
    var up = 0.0
    for i in 1...array[0]{
        if Double(array[i]) > mean{
            up += 1.0
        }
    }
    print("\(String(format: "%.3f", round(up / Double(array[0]) * 100.0 * digit) / digit))%")
}

