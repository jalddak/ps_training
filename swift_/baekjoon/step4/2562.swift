import Foundation

var max_value = 0
var max_index = 0

for i in 1...9{
    let value = Int(readLine()!)!
    max_value = max(max_value, value)
    if max_value == value {
        max_index = i
    }
}
print(max_value)
print(max_index)
