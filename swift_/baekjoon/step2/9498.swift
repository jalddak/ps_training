import Foundation

//  90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F

let score = Int(readLine()!)!
switch score{
case 90...100: print("A")
case 80...89: print("B")
case 70...79: print("C")
case 60...69: print("D")
default:
    print("F")
}
