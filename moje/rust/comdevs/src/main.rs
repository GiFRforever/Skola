//input list of numbers, for each number find their divisers and print them

//importing the io library
fn main() {
    use std::io;
    let mut input = String::new();
    println!("Enter a list of numbers, separated by space");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut numbers: Vec<i32> = Vec::new();
    for number in input.split_whitespace() {
        numbers.push(number.parse::<i32>().unwrap());
    }
    for number in numbers {
        println!("Divisors of {} are: ", number);
        for i in 1..number {
            if number % i == 0 {
                print!("{} ", i);
            }
        }
        println!("");
    }
}