path = "input1.txt"

# Part 1

println(sum(diff(parse.(Int, readlines(path))) .> 0))

# Part 2

arr = parse.(Int, readlines(path))

sum(arr[i] < arr[i+3] for i in eachindex(arr) if i+3 <= length(arr))
