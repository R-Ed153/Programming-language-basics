fn main() {
    println!("Hello, world!");
    //another_function();
    //another_function2(6);
    print_labeled_measurement(56, 'J');
    let y = {
        let x = 3;
        x + 1
    };
    println!("The value of y is: {y}");
}

fn another_function() {
    println!("Another function.");
}

fn another_function2(x: i32) {
    println!("The value of x is: {x}");
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
