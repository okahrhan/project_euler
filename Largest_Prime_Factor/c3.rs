use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Usage: {} <number>", args[0]);
        process::exit(1);
    }

    let number: u64 = match args[1].parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Please provide a valid number");
            process::exit(1);
        }
    };

    let mut largest_number = -1;
    let mut i: u64 = 2;

    while i <= number / 2 {
        if number % i == 0 {
            let mut is_prime = true;
            let mut j: u64 = 2;
            while j <= i / 2 {
                if i % j == 0 {
                    is_prime = false;
                    break;
                }
                j += 1;
            }
            if is_prime {
                largest_number = i as i64;
            }
        }
        i += 1;
    }

    if largest_number == -1 {
        largest_number = number as i64;
    }

    println!("{}", largest_number);
}
