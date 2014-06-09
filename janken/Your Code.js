"use strict";

/*
PlayerName="ryosy383"
【感想・作戦・工夫した点など】
ランダムが使用できないので、数学関数を使用して乱数に近い値と、再帰を利用しました。
一定の確率でグーを出して、ポイントを稼ぐようにしました。
*/

var count = 0;
function play(h)　{

  var last = h[1][h[1].length - 1];
  count++;
  
  //一定の確率でグーを出す(ランダムが使用できないので、数学関数を使用して出力を一意にする)
  if ( ( parseInt(( Math.PI * count  * Math.sqrt(count) ) * 10 )% 7 ) == 1 ) {
    return "G";
  }
  
  count++;
  
  // G:0, C:1, P:2
  switch( parseInt(( Math.PI * count * Math.sqrt(count) )*10) % 3 ) {
    case 0:
      if ( last == "P" ) {
        //新しい手が直前の手に負けたら再帰
        return play(h);
      }
      return "G";
    case 1:
      if ( last == "G" ) {
        return play(h);
      }
      return "C";
    case 2:
      if ( last == "C" ) {
        return play(h);
      }
      return "P";
  }  
}

// イベントを受け取り、グーチョキパーのどれを出すかを返信するための仕組みです。
self.addEventListener('message', function(e) {
  self.postMessage( play(e.data.split(",")) );
}, false);
