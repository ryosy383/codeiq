ワンライナーでテキスト処理
https://codeiq.jp/ace/hayakawa_atsushi/q856


■解答
問1. Speciesの列を表示させなさい。
コマンド:
$ awk -F "," 'FNR == 1 {print}' iris.csv
出力結果:
"","Sepal.Length","Sepal.Width","Petal.Length","Petal.Width","Species"

問2. 行ごとにSepal.LengthとSepal.Widthの合計を求めなさい。
コマンド:
$ awk -F "," 'BEGIN{printf "row\t:\tSepal.Length+Sepal.Width\n"} NR>1{sum = $2+$3;printf ("%s\t:\t%.1f\n", $1, sum)}' iris.csv
出力結果:
row	:	Sepal.Length+Sepal.Width
"1"	:	8.6
"2"	:	7.9
"3"	:	7.9
"4"	:	7.7
"5"	:	8.6
"6"	:	9.3
"7"	:	8.0
"8"	:	8.4
"9"	:	7.3
"10"	:	8.0
"11"	:	9.1
"12"	:	8.2
"13"	:	7.8
"14"	:	7.3
"15"	:	9.8
"16"	:	10.1
"17"	:	9.3
"18"	:	8.6
"19"	:	9.5
"20"	:	8.9
"21"	:	8.8
"22"	:	8.8
"23"	:	8.2
"24"	:	8.4
"25"	:	8.2
"26"	:	8.0
"27"	:	8.4
"28"	:	8.7
"29"	:	8.6
"30"	:	7.9
"31"	:	7.9
"32"	:	8.8
"33"	:	9.3
"34"	:	9.7
"35"	:	8.0
"36"	:	8.2
"37"	:	9.0
"38"	:	8.5
"39"	:	7.4
"40"	:	8.5
"41"	:	8.5
"42"	:	6.8
"43"	:	7.6
"44"	:	8.5
"45"	:	8.9
"46"	:	7.8
"47"	:	8.9
"48"	:	7.8
"49"	:	9.0
"50"	:	8.3
"51"	:	10.2
"52"	:	9.6
"53"	:	10.0
"54"	:	7.8
"55"	:	9.3
"56"	:	8.5
"57"	:	9.6
"58"	:	7.3
"59"	:	9.5
"60"	:	7.9
"61"	:	7.0
"62"	:	8.9
"63"	:	8.2
"64"	:	9.0
"65"	:	8.5
"66"	:	9.8
"67"	:	8.6
"68"	:	8.5
"69"	:	8.4
"70"	:	8.1
"71"	:	9.1
"72"	:	8.9
"73"	:	8.8
"74"	:	8.9
"75"	:	9.3
"76"	:	9.6
"77"	:	9.6
"78"	:	9.7
"79"	:	8.9
"80"	:	8.3
"81"	:	7.9
"82"	:	7.9
"83"	:	8.5
"84"	:	8.7
"85"	:	8.4
"86"	:	9.4
"87"	:	9.8
"88"	:	8.6
"89"	:	8.6
"90"	:	8.0
"91"	:	8.1
"92"	:	9.1
"93"	:	8.4
"94"	:	7.3
"95"	:	8.3
"96"	:	8.7
"97"	:	8.6
"98"	:	9.1
"99"	:	7.6
"100"	:	8.5
"101"	:	9.6
"102"	:	8.5
"103"	:	10.1
"104"	:	9.2
"105"	:	9.5
"106"	:	10.6
"107"	:	7.4
"108"	:	10.2
"109"	:	9.2
"110"	:	10.8
"111"	:	9.7
"112"	:	9.1
"113"	:	9.8
"114"	:	8.2
"115"	:	8.6
"116"	:	9.6
"117"	:	9.5
"118"	:	11.5
"119"	:	10.3
"120"	:	8.2
"121"	:	10.1
"122"	:	8.4
"123"	:	10.5
"124"	:	9.0
"125"	:	10.0
"126"	:	10.4
"127"	:	9.0
"128"	:	9.1
"129"	:	9.2
"130"	:	10.2
"131"	:	10.2
"132"	:	11.7
"133"	:	9.2
"134"	:	9.1
"135"	:	8.7
"136"	:	10.7
"137"	:	9.7
"138"	:	9.5
"139"	:	9.0
"140"	:	10.0
"141"	:	9.8
"142"	:	10.0
"143"	:	8.5
"144"	:	10.0
"145"	:	10.0
"146"	:	9.7
"147"	:	8.8
"148"	:	9.5
"149"	:	9.6
"150"	:	8.9


問3. Sepal.Lengthの列の合計を求めなさい。
コマンド: $ awk -F "," 'NR>1{sum += $2} END{print sum}' iris.csv
出力結果:
876.5

問4. setosa,versicolor,virginicaがそれぞれ何レコードあるかを求めなさい。
コマンド: awk -F "," 'BEGIN{ setosa=0;versicolor=0;virginica=0 } NR>1{if($6~"setosa")setosa++;if($6~"versicolor")versicolor++;if($6~"virginica")virginica++;} END {printf ("setosa:%d versicolor:%d virginica:%d\n", setosa, versicolor, virginica)}' iris.csv
出力結果:
setosa:50 versicolor:50 virginica:50

問5. setosa,versicolor,virginicaごとにSepal.Lengthの合計を求めなさい。
コマンド: awk -F "," 'BEGIN{ setosa=0;versicolor=0;virginica=0 } NR>1{if($6~"setosa")setosa+=$2;if($6~"versicolor")versicolor+=$2;if($6~"virginica")virginica+=$2;} END {printf ("setosa:%.1f versicolor:%.1f virginica:%.1f\n", setosa, versicolor, virginica)}' iris.csv
出力結果:
setosa:250.3 versicolor:296.8 virginica:329.4

問6. setosa,versicolor,virginicaごとにSepal.Lengthの平均を求めなさい。
コマンド: awk -F "," 'BEGIN{ setosa=0;versicolor=0;virginica=0;rows=0; } NR>1{rows++;if($6~"setosa")setosa+=$2;if($6~"versicolor")versicolor+=$2;if($6~"virginica")virginica+=$2;} END {printf ("setosa:%f versicolor:%f virginica:%f\n", setosa/rows, versicolor/rows, virginica/rows)}' iris.csv
出力結果:
setosa:1.668667 versicolor:1.978667 virginica:2.196000

問7. setosa,versicolor,virginicaごとにSepal.Lengthの最小値を求めなさい。
コマンド: awk -F "," 'BEGIN{ setosa=nan;versicolor=nan;virginica=nan;} NR>1{if($6~"setosa" && (setosa == nan || setosa>$2))setosa=$2;if($6~"versicolor" && (versicolor == nan || versicolor>$2))versicolor=$2;if($6~"virginica" && (virginica == nan || virginica>$2))virginica=$2;} END {printf ("setosa:%.1f versicolor:%.1f virginica:%.1f\n", setosa, versicolor, virginica)}' iris.csv
出力結果:
setosa:4.3 versicolor:4.9 virginica:4.9

