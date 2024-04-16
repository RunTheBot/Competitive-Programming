use std::io::{self, BufRead};

fn build(elements: &Vec<i64>, num_elements: usize, segtree: &mut Vec<i64>) {
    for i in 0..num_elements {
        segtree[num_elements + i] = elements[i];
    }
    for i in (0..num_elements - 1).rev() {
        segtree[i] = segtree[2 * i] + segtree[2 * i + 1];
    }
}

fn update(index: usize, val: i64, num_elements: usize, segtree: &mut Vec<i64>) {
    let mut idx = index + num_elements;
    segtree[idx] = val;
    while idx > 1 {
        idx /= 2;
        segtree[idx] = segtree[2 * idx] + segtree[2 * idx + 1];
    }
}

fn query_tree(mut left: usize, mut right: usize, num_elements: usize, segtree: &Vec<i64>) -> i64 {
    left += num_elements;
    right += num_elements;
    let mut sum = 0;
    while left < right {
        if left & 1 == 1 {
            sum += segtree[left];
            left += 1;
        }
        if right & 1 == 1 {
            right -= 1;
            sum += segtree[right];
        }
        left /= 2;
        right /= 2;
    }
    sum
}

fn main() {
    println!("This is rust!");
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let first_line = lines.next().unwrap().unwrap();
    let mut split = first_line.split_whitespace();
    let num_elements: usize = split.next().unwrap().parse().unwrap();
    let queries: usize = split.next().unwrap().parse().unwrap();

    let second_line = lines.next().unwrap().unwrap();
    let elements: Vec<i64> = second_line.split_whitespace().map(|x| x.parse().unwrap()).collect();

    let mut segtree: Vec<i64> = vec![0; 2 * num_elements];
    build(&elements, num_elements, &mut segtree);

    for _ in 0..queries {
        let query_line = lines.next().unwrap().unwrap();
        let mut query_split = query_line.split_whitespace();
        let query_type = query_split.next().unwrap();
        if query_type == "S" {
            let left: usize = query_split.next().unwrap().parse().unwrap();
            let right: usize = query_split.next().unwrap().parse().unwrap();
            println!("{}", query_tree(left - 1, right, num_elements, &segtree));
        } else {
            let index: usize = query_split.next().unwrap().parse().unwrap();
            let value: i64 = query_split.next().unwrap().parse().unwrap();
            update(index - 1, value, num_elements, &mut segtree);
        }
    }
}
