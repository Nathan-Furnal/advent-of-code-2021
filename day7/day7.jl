using Statistics

data = parse.(Int, split(readline(joinpath(@__DIR__, "input.txt")), ","))

# Part 1

cost1(arr, val) = sum(abs.(arr .- val))
println(cost1(data, convert(Int, median(data))))

# Part 2

gauss_sum(dist) = dist .* (dist .+ 1) ./ 2
cost2(arr, val) = sum(gauss_sum(abs.(arr .- val)))

c1 = cost2(data, round(mean(data) - 1/2))
c2 = cost2(data, round(mean(data) + 1/2))
println(convert(Int, min(c1, c2)))
