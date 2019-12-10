#!/usr/bin/python3

let = 97

while (let < 123):
    if let == 101 or let == 113:
        let += 1
    print("{:c}".format(let), end="")
    let += 1
