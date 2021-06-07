function main()
    grid = [readline() for _ in 1:20]
    push!(grid, "#"^10)
    println(stderr, grid)
    for col in 1:10
        row = 1
        while grid[row][col] == '.'
            row += 1
        end
        if row < 5
            continue
        end
        if all(
            count(isequal('#'), grid[prev_row]) == 9
            for prev_row in (row-4):(row-1)
        )
            return "BOOM $col"
        end
    end
    "NOPE"
end


main() |> println