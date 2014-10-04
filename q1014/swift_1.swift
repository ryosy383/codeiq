//
//  main.swift
//  CaseTest
//
//  Created by 大津 真 on 2014/08/06.
//  Copyright (c) 2014年 大津 真. All rights reserved.
//

import Foundation

// ＊問1
var month: Int = 3

switch month {
    case 12, 1, 2:
        println(String(month) + "月は冬です")
        break
    
    case 3, 4, 5:
        println(String(month) + "月は春です")
        break
    
    case 6, 7, 8:
        println(String(month) + "月は夏です")
        break
    
    case 9, 10, 11:
        println(String(month) + "月は秋です")
        break
    
    
    default:
        println("月の値は1から12である必要があります")
        break
    
    
}


// ＊問2
var filename: String = "sample.html"

switch filename.pathExtension {
    case "html", "htm":
        println(filename + "はHTMLファイルです")
        break
    
    case "txt":
        println(filename + "はテキストファイルです")
        break
    
    case "swift":
        println(filename + "はSwiftファイルです")
        break
    
    default:
        println("不明なファイル形式です")
        break
}


// ＊問3
var age: Int = 19

switch age {
    case 0...19:
        println(String(age) + "才は未成年です")
        break
    
    case 20:
        println(String(age) + "はちょうど成人です。")
        break
    
    case let age where age >= 21:
        println(String(age) + "は成人です")
        break
    
    default:
        println("年齢の値が不適切です")
        break
}

