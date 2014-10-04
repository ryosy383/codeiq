#選んだ開発言語:Julia
#出力結果:356400
#「実行速度とメモリ消費量、どちらを重視して最適化したか？」: 実行速度

vec = Int64[]
for n0 = 1:31
  for n1 = 1:31
    for n2 = 1:31
      for n3 = 1:31
        for n4 = 1:31
          push!(vec, n0*n1*n2*n3*n4)
        end
      end
    end
  end
end
println(int(median(vec)))

