use std::collections::HashSet;
use std::fs;

fn paradox(
    grid: &Vec<Vec<char>>,
    row: usize,
    col: usize,
    obstacle_row: usize,
    obstacle_col: usize,
) -> bool {
    let rows = grid.len() as isize;
    let cols = grid[0].len() as isize;

    let directions = [
        (-1, 0), // up
        (0, 1),  // right
        (1, 0),  // down
        (0, -1), // left
    ];

    // `row` and `col` are signed while moving, so the saved state must use
    // the same coordinate type.
    let mut seen: HashSet<(isize, isize, usize)> = HashSet::new();
    let mut direction: usize = 0;
    let mut row = row as isize;
    let mut col = col as isize;

    loop {
        if !seen.insert((row, col, direction)) {
            return true;
        }

        let dr = row + directions[direction].0;
        let dc = col + directions[direction].1;

        if dr < 0 || dr >= rows || dc < 0 || dc >= cols {
            return false;
        }

        let hits_original_obstacle = grid[dr as usize][dc as usize] == '#';
        let hits_new_obstacle = dr as usize == obstacle_row && dc as usize == obstacle_col;

        if hits_original_obstacle || hits_new_obstacle {
            direction = (direction + 1) % 4;
        } else {
            row = dr;
            col = dc;
        }
    }
}

fn main() {
    let data: String = fs::read_to_string("input.txt").expect("Failed to read from input.txt");

    let grid: Vec<Vec<char>> = data
        .lines()
        .map(|row| row.chars().map(|ch| ch.to_ascii_lowercase()).collect())
        .collect();

    let rows: usize = grid.len();
    let cols: usize = grid[0].len();

    let mut start_row: usize = 0;
    let mut start_col: usize = 0;

    for row in 0..rows {
        for col in 0..cols {
            if grid[row][col] == '^' {
                start_row = row;
                start_col = col;
                break;
            }
        }
    }

    let mut res: i32 = 0;

    for row in 0..rows {
        for col in 0..cols {
            if row == start_row && col == start_col {
                continue;
            }

            if grid[row][col] != '.' {
                continue;
            }

            if paradox(&grid, start_row, start_col, row, col) {
                res += 1;
            }
        }
    }

    println!("Number of dirrection position of obstacles {}", res)
}
