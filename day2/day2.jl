path = "input2.txt"

arr_split = map(split, readlines(path))
commands = first.(arr_split)
values = parse.(Int, last.(arr_split))

# Part 1

function submarine_depth()
    h_pos = depth = 0
    dict = Dict("up" => -1, "down" => 1)
    for (c, v) in zip(commands, values)
        if c == "forward"
            h_pos += v
        else
            depth += dict[c] * v
        end
    end
    return h_pos * depth
end


print(submarine_depth())    


# Part 2

function submarine_depth2()
    h_pos = depth = aim = 0
    dict = Dict("up" => -1, "down" => 1)
    for (c, v) in zip(commands, values)
        if c == "forward"
            h_pos += v
            depth += aim * v
        else
            aim += dict[c] * v
        end
    end
    return h_pos * depth
end

print(submarine_depth2())
