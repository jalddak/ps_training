import Foundation

var array = readLine()!.split(separator: " ").map{Int($0)!}
var dict = [Int:Int]()

for i in array{
    if let _ = dict[i]{
        dict[i]! += 1
    }
    else{
        dict[i] = 1
    }
}
var max_value = 0
var max_value_key = Int()
var max_key = 0

for (key, value) in dict{
    if max_value < value{
        max_value = value
        max_value_key = key
    }
    if max_key < key{
        max_key = key
    }
}

if max_value == 3{
    print(10000 + max_value_key * 1000)
}
else if max_value == 2{
    print(1000 + max_value_key * 100)
}
else{
    print(max_key * 100)
}
