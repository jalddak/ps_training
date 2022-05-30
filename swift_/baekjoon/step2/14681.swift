import Foundation

let x = Int(readLine()!)!
let y = Int(readLine()!)!

if x > 0 {
    if y > 0{
        print(1)
    }else if y < 0{
        print(4)
    }
}else if x < 0{
    if y > 0{
        print(2)
    }else if y < 0{
        print(3)
    }
}
