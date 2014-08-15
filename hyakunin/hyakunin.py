#百人一首 https://codeiq.jp/ace/thisweek_masuipeo/q646

# -*- coding: shift-jis -*-
import csv
 
class Trie:
    class Node:
        def __init__(self, x, bros = None, child = None):
            self.data = x
            self.bros = bros
            self.child = child
 
        # 子を求める
        def get_child(self, x):
            child = self.child
            while child:
                if child.data == x: break
                child = child.bros
            return child
 
        # 子を挿入する
        def set_child(self, x):
            child = Trie.Node(x, self.child)
            self.child = child
            return child
 
        # 子を削除する
        def del_child(self, x):
            child = self.child
            if child.data == x:
                self.child = child.bros
                return True
            else:
                while child.bros:
                    if child.bros.data == x:
                        child.bros = child.bros.bros
                        return True
                    child = child.bros
            return False
 
        # 節を巡回する (ジェネレータ)
        def traverse(self, leaf):
            if self.data == leaf:
                yield []
            else:
                child = self.child
                while child:
                    for x in child.traverse(leaf):
                        yield [self.data] + x
                    child = child.bros
 
    def __init__(self, x = None):
        self.root = Trie.Node(None)  # header
        self.leaf = x
 
    # 探索
    def search(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if not node: return False
        # check leaf
        return node.get_child(self.leaf) is not None
 
    # 挿入
    def insert(self, seq):
        node = self.root
        for x in seq:
            child = node.get_child(x)
            if not child:
                child = node.set_child(x)
            node = child
        # check leaf
        if not node.get_child(self.leaf):
            node.set_child(self.leaf)
 
    # 削除
    def delete(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if not node: return False
        # delete leaf
        return node.del_child(self.leaf)
 
    # 巡回 (高階関数版)
    def traverse_h(self, func):
        def traverse_node(node, buff):
            if node.data == self.leaf:
                func(buff)
            else:
                child = node.child
                while child:
                    traverse_node(child, buff + [node.data])
                    child = child.bros
        #
        node = self.root.child
        while node:
            traverse_node(node, [])
            node = node.bros
 
    # 巡回 (ジェネレータ版)
    def traverse(self):
        node = self.root.child
        while node:
            for x in node.traverse(self.leaf):
                yield x
            node = node.bros
 
    # 共通接頭辞を持つデータを求める
    def common_prefix(self, seq):
        node = self.root
        buff = []
        for x in seq:
            buff.append(x)
            node = node.get_child(x)
            if not node: return
        node = node.child
        while node:
            for x in node.traverse(self.leaf):
                yield buff + x
            node = node.bros
 
if __name__ == '__main__':
    def generator_len(g):
        return sum(1 for x in g)
    
    csvfile = open("hyakunin.csv")
    arr = [[column for column in row] for row in csv.reader(csvfile)]
    del arr[0]
    
    up_t = Trie()
    down_t = Trie()
    up = []
    down = []
    for a in arr:
        up_t.insert(a[3])
        down_t.insert(a[4])
        up.append(str(a[3]))
        down.append(str(a[4]))
    
 
    #上の句と下の句を別々に求める:
    answer_up = 0
    answer_down = 0
    print "番号", "上の句を一に決める文字数", "下の句を一に決める文字数", "上の句", "下の句"
    for j in range(0,len(up)):
 
        c = ""
        cost = float("inf")
        for x in range(0,len(up[j])/2):
            c = c + str(up[j][x*2]+up[j][x*2+1])
            if generator_len(up_t.common_prefix(c)) == 1:
                if x < cost:
                    cost = x
                    break
        answer_up = answer_up + x + 1
        c = ""
        cost = float("inf")
        for y in range(0,len(down[j])/2):
            c = c + str(down[j][y*2]+down[j][y*2+1])
            if generator_len(down_t.common_prefix(c)) == 1:
                if y < cost:
                    cost = y
                    break
        answer_down = answer_down + y + 1
        print j+1, x + 1, y + 1, up[j], down[j]
    print "合計", answer_up, answer_down, answer_up + answer_down
 
#  番号 上の句を一に決める文字数 下の句を一に決める文字数 上の句 下の句
# 1 3 7 あきのたのかりほのいほのとまをあらみ わかころもてはつゆにぬれつつ
# 2 3 4 はるすきてなつきにけらししろたへの ころもほすてふあまのかくやま
# 3 2 3 あしひきのやまとりのをのしたりをの なかなかしよをひとりかもねむ
# 4 2 2 たこのうらにうちいててみれはしろたへの ふしのたかねにゆきはふりつつ
# 5 2 2 おくやまにもみちふみわけなくしかの こゑきくときそあきはかなしき
# 6 2 2 かささきのわたせるはしにおくしもの しろきをみれはよそふけにける
# 7 3 2 あまのはらふりさけみれはかすかなる みかさのやまにいてしつきかも
# 8 3 3 わかいほはみやこのたつみしかそすむ よをうちやまとひとはいふなり
# 9 3 4 はなのいろはうつりにけりないたつらに わかみよにふるなかめせしまに
# 10 2 2 これやこのゆくもかへるもわかれては しるもしらぬもあふさかのせき
# 11 6 4 わたのはらやそしまかけてこきいてぬと ひとにはつけよあまのつりふね
# 12 3 1 あまつかせくものかよひちふきとちよ をとめのすかたしはしととめむ
# 13 2 3 つくはねのみねよりおつるみなのかわ こひそつもりてふちとなりぬる
# 14 2 4 みちのくのしのふもちすりたれゆゑに みたれそめにしわれならなくに
# 15 6 7 きみかためはるののにいててわかなつむ わかころもてにゆきはふりつつ
# 16 2 3 たちわかれいなはのやまのみねにおふる まつとしきかはいまかへりこむ
# 17 2 2 ちはやふるかみよもきかすたつたかは からくれなゐにみつくくるとは
# 18 1 2 すみのえのきしによるなみよるさへや ゆめのかよひちひとめよくらむ
# 19 4 3 なにはかたみしかきあしのふしのまも あはてこのよをすくしてよとや
# 20 2 7 わひぬれはいまはたおなしなにはなる みをつくしてもあはむとそおもふ
# 21 3 2 いまこむといひしはかりになかつきの ありあけのつきをまちいてつるかな
# 22 1 2 ふくからにあきのくさきのしをるれは むへやまかせをあらしといふらむ
# 23 2 4 つきみれはちちにものこそかなしけれ わかみひとつのあきにはあらねと
# 24 2 2 このたひはぬさもとりあへすたむけやま もみちのにしきかみのまにまに
# 25 3 4 なにしおははあふさかやまのさねかつら ひとにしられてくるよしもかな
# 26 1 8 をくらやまみねのもみちはこころあらは いまひとたひのみゆきまたなむ
# 27 3 3 みかのはらわきてなかるるいつみかは いつみきとてかこひしかるらむ
# 28 3 3 やまさとはふゆそさびしさまさりける ひとめもくさもかれぬとおもへは
# 29 4 1 こころあてにおらはやおらむはつしもの おきまとはせるしらきくのはな
# 30 3 2 ありあけのつれなくみえしわかれより あかつきはかりうきものはなし
# 31 6 2 あさほらけありあけのつきとみるまてに よしののさとにふれるしらゆき
# 32 3 3 やまかはにかせのかけたるしからみは なかれもあへぬもみちなりけり
# 33 2 2 ひさかたのひかりのとけきはるのひに しつこころなくはなのちるらむ
# 34 2 3 たれをかもしるひとにせむたかさこの まつもむかしのともならなくに
# 35 3 3 ひとはいさこころもしらすふるさとは はなそむかしのかににほひける
# 36 2 3 なつのよはまたよひなからあけぬるを くものいつこにつきやとるらむ
# 37 2 1 しらつゆにかせのふきしくあきののは つらぬきとめぬたまそちりける
# 38 3 3 わすらるるみをはおもはすちかひてし ひとのいのちのをしくもあるかな
# 39 3 3 あさちふのをののしのはらしのふれと あまりてなとかひとのこひしき
# 40 2 2 しのふれといろにいてにけりわかこひは ものやおもふとひとのとふまて
# 41 2 3 こひすてふわかなはまたきたちにけり ひとしれすこそおもひそめしか
# 42 4 1 ちきりきなかたみにそてをしほりつつ すゑのまつやまなみこさしとは
# 43 2 2 あひみてののちのこころにくらふれは むかしはものをおもはさりけり
# 44 2 3 あふことのたえてしなくはなかなかに ひとをもみをもうらみさらまし
# 45 3 2 あはれともいふへきひとはおもほえて みのいたつらになりぬへきかな
# 46 2 2 ゆらのとをわたるふなひとかちをたえ ゆくへもしらぬこひのみちかな
# 47 2 5 やへむくらしけれるやとのさひしきに ひとこそみえねあきはきにけり
# 48 3 2 かせをいたみいはうつなみのおのれのみ くたけてものをおもふころかな
# 49 3 2 みかきもりゑしのたくひのよるはもえ ひるはきえつつものをこそおもへ
# 50 6 3 きみかためおしからさりしいのちさへ なかくもかなとおもひけるかな
# 51 2 1 かくとたにえやはいふきのさしもくさ さしもしらしなもゆるおもひを
# 52 2 3 あけぬれはくるるものとはしりなから なほうらめしきあさほらけかな
# 53 3 2 なけきつつひとりぬるよのあくるまは いかにひさしきものとかはしる
# 54 3 3 わすれしのゆくすゑまてはかたけれは けふをかきりのいのちともかな
# 55 2 2 たきのおとはたえてひさしくなりぬれと なこそなかれてなほきこえけれ
# 56 3 8 あらさらむこのよのほかのおもひてに いまひとたひのあふこともかな
# 57 1 3 めくりあひてみしやそれともわかぬまに くもかくれにしよはのつきかけ
# 58 3 2 ありまやまゐなのささはらかせふけは いてそよひとをわすれやはする
# 59 2 2 やすらはてねなましものをさよふけて かたふくまてのつきをみしかな
# 60 3 2 おほえやまいくののみちのとほけれは またふみもみすあまのはしたて
# 61 2 3 いにしへのならのみやこのやへさくら けふここのへににほひぬるかな
# 62 2 2 よをこめてとりのそらねははかるとも よにあふさかのせきはゆるさし
# 63 3 3 いまはたたおもひたえなむとはかりを ひとつてならていふよしもかな
# 64 6 2 あさほらけうちのかはきりたえたえに あらはれわたるせせのあしろき
# 65 2 3 うらみわひほさぬそてたにあるものを こひにくちなむなこそをしけれ
# 66 2 3 もろともにあはれとおもへやまさくら はなよりほかにしるひともなし
# 67 3 2 はるのよのゆめはかりなるたまくらに かひなくたたむなこそをしけれ
# 68 4 3 こころにもあらてうきよになからへは こひしかるへきよはのつきかな
# 69 3 2 あらしふくみむろのやまのもみちはは たつたのかはのにしきなりけり
# 70 1 3 さひしさにやとをたちいててなかむれは いつくもおなしあきのゆふくれ
# 71 2 2 ゆうされはかとたのいなはおとつれて あしのまろやにあきかせそふく
# 72 2 2 おとにきくたかしのはまのあたなみは かけしやそてのぬれもこそすれ
# 73 2 1 たかさこのをのへのさくらさきにけり とやまのかすみたたすもあらなむ
# 74 2 2 うかりけるひとをはつせのやまおろしよ はけしかれとはいのらぬものを
# 75 4 3 ちきりおきしさせもかつゆをいのちにて あはれことしのあきもいぬめり
# 76 6 3 わたのはらこきいててみれはひさかたの くもゐにまかふおきつしらなみ
# 77 1 2 せをはやみいわにせかるるたきかはの われてもすゑにあはむとそおもふ
# 78 3 2 あはちしまかよふちとりのなくこゑに いくよねさめぬすまのせきもり
# 79 3 2 あきかせにたなひくくものたえまより もれいつるつきのかけのさやけさ
# 80 3 4 なかからむこころもしらすくろかみの みたれてけさはものをこそおもへ
# 81 1 2 ほとときすなきつるかたをなかむれは たたありあけのつきそのこれる
# 82 2 2 おもひわひさてもいのちはあるものを うきにたへぬはなみたなりけり
# 83 5 2 よのなかよみちこそなけれおもひいる やまのおくにもしかそなくなる
# 84 3 2 なからへはまたこのころやしのはれむ うしとみしよそいまはこひしき
# 85 2 1 よもすからものおもふころはあけやらぬ ねやのひまさへつれなかりけり
# 86 3 2 なけけとてつきやはものをおもはする かこちかほなるわかなみたかな
# 87 1 1 むらさめのつゆもまたひぬまきのはに きりたちのほるあきのゆふくれ
# 88 4 7 なにはえのあしのかりねのひとよゆゑ みをつくしてやこひわたるへき
# 89 2 2 たまのをよたえなはたえねなからへは しのふることのよはりもそする
# 90 2 1 みせはやなをしまのあまのそてたにも ぬれにそぬれしいろはかはらす
# 91 2 4 きりきりすなくやしもよのさむしろに ころもかたしきひとりかもねむ
# 92 3 5 わかそてはしほひにみえぬおきのいしの ひとこそしらねかわくまもなし
# 93 5 3 よのなかはつねにもかもななきさこく あまのおふねのつなてかなしも
# 94 2 2 みよしののやまのあきかせさよふけて ふるさとさむくころもうつなり
# 95 3 3 おほけなくうきよのたみにおほふかな わかたつそまにすみそめのそて
# 96 3 2 はなさそふあらしのにはのゆきならて ふりゆくものはわかみなりけり
# 97 2 2 こぬひとをまつほのうらのゆふなきに やくやもしほのみもこかれつつ
# 98 3 2 かせそよくならのをかはのゆふくれは みそきそなつのしるしなりける
# 99 3 3 ひともをしひともうらめしあちきなく よをおもふゆゑにものおもふみは
# 100 2 3 ももしきやふるきのきはのしのふにも なほあまりあるむかしなりけり
# 合計 270 276 546
