#CodeIQ: cielavenir���񂩂�̖��
#�y���K���o�zDetect Music Key ��
#
#author: @ryosy383
#ENV:ruby 1.9.3-p448, Ubuntu 12.04LTS
#�n����
#C D E F G A B
#0 2 4 5 7 9 11
tone = ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"]
major = [0, 2, 4, 5, 7, 9, 11]

scales = []
#���ׂĂ̒��������߂�
for i in 0...tone.size do
  ret = tone.rotate(i)
  scales << major.map{|r| ret[r]}
end
file = File.open("data.in")

T = file.gets.to_i
while T > 0
  x = file.gets.to_i #�g��Ȃ�����
  targets = file.gets.chomp.split(" ")
  result = scales.reject {|scale| targets.map{|r| scale.include?(r)}.include?(false) }
  puts result.empty? ? "invalid" : result.map{|r| r.first}.join(" ")
  T -= 1
end