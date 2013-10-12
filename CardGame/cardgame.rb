#!ruby
#- - - - environment
#Ruby: 1.9.3-p448 OS: Ubuntu 12.04LTS
#- - - -
# CodeIQ
# カードゲームの役を判定する
# トランプを使ったカードゲームの役を判定するプログラムを書いて下さい。
#
#■問題
#
#トランプで行うカードゲームがあります。
#このゲームには7種類の「役」があり、いずれかの「役」ができると終了となります。
#役ができているかどうか、それはどの役なのかを判定するプログラムを書いて下さい。
#
#資料の中には手札の情報が1万件入っています。それぞれの役が何件あるのかを答えていただきます。
#
suit_numbers = ["S", "H", "D", "C"]
rank_numbers = ["0", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
an = sdt = dt = sctp = ctp = stp = tp = 0 
File.foreach("data.txt") do |str|
  cards = str.chomp.split(",")
  card_hash = Hash.new{ |h,k| h[k]=[] }
  cards.each do |card|
    card_hash[suit_numbers.index(card[0])].push(rank_numbers.index(card[1...card.length]))
  end
  ranks = []
  suits = []
  card_hash.each do |suit, rank|
    suits.push(suit)
    ranks += rank
  end

  if ranks.uniq.count == 2
    pair = ranks.select {|r| r == ranks.uniq.first}.count
    an += 1 if pair == 4 || pair == 2
    suits.uniq.count == 3 ? sdt += 1 : dt += 1 if pair == 3
  end

  if ranks.uniq.count == 3 && 
      ranks.select {|r| r == ranks.uniq.first}.count == 2 && 
      ranks.select {|r| r == ranks.uniq[1]}.count == 2
    s = true
    c = false
    for i in 1...suits.uniq.count do
      s = false if card_hash[suits.uniq[i - 1]].sort != card_hash[suits.uniq[i]].sort
    end
    a0, a1, a2  = ranks.uniq.sort
    c = true if (a1 - a0 == 1 && a2 - a1 == 1) || (a0 == 1 && a1 == 12 && a2 == 13)     
    sctp += 1 if s && c
    ctp += 1 if !s && c
    stp += 1 if s && !c
    tp += 1 if !s && !c
  end  
end
puts "An:#{an},sDT:#{sdt},DT:#{dt},scTP:#{sctp},cTP:#{ctp},sTP:#{stp},TP:#{tp}"

# Output:
# An:333,sDT:22,DT:444,scTP:11,cTP:666,sTP:555,TP:7777
#

