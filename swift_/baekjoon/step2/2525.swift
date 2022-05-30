import Foundation

let array = readLine()!.split(separator: " ").map{Int($0)!}
var hour = array[0]
var minute = array[1]
let after = Int(readLine()!)!

minute += after
hour += minute / 60
minute %= 60

if hour > 23{
    hour -= 24
}

print("\(hour) \(minute)")
