import Foundation

let A = Int(readLine()!)!
let B = Int(readLine()!)!
let C = Int(readLine()!)!

let mult = A * B * C

let string_m = String(mult)
var dict_m = [Int:Int]()
for i in string_m{
    let int_value = Int(String(i))!
    if let _ = dict_m[int_value]{
        dict_m[int_value]! += 1
    }
    else{
        dict_m[int_value] = 1
    }
}
for i in 0...9{
    if let check = dict_m[i]{
        print(check)
    }
    else{
        print(0)
    }
}
