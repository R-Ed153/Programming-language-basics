//convert celsius to fahrenheit
//nth Fibonacci number
//Christmas carol "The twelve days of Christmas"

fn main() {
    println!("Hello, world!");
    let series: u32 = 5;
    let test_celsius_temp: f64 = 32.7;

    println!(
        "{test_celsius_temp}\u{00B0} to fahrenheit = {:.2}\u{00B0}",
        celsius_to_fahrenheit(test_celsius_temp)
    );
    println!("The {series}th_fibonacci is {}", nth_fibonacci(series));
}

fn celsius_to_fahrenheit(temp: f64) -> f64 {
    temp * 1.8 + 32.0
}

fn nth_fibonacci(n: u32) -> u32 {
    let mut first = 0;
    let mut second = 1;
    let mut result = 5;

    for _i in 0..n {
        result = first + second;
        first = second;
        second = result;
    }
    result
}
