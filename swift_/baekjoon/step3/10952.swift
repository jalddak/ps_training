import Foundation

var A = 1
var B = 1
while true{
    let array = readLine()!.split(separator: " ").map{Int($0)!}
    A = array[0]
    B = array[1]
    if A != 0 && B != 0{
        print(A+B)
    }
    else{
        break
    }
}
