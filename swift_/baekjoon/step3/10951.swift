import Foundation

var A = 1
var B = 1
while true{
    if let input = readLine(){
        let array = input.split(separator: " ").map{Int($0)!}
        A = array[0]
        B = array[1]
        print(A+B)
    }
    else{
        break
    }
}
