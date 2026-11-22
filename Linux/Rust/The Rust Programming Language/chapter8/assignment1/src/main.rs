use std::io;
use std::collections::HashMap;

fn main() {
    let mut vec: Vec<i32> = vec![];
    println!("Enter integers (one-by-one) to get their median and mode");
    loop {
        let mut user_input: String = String::new();
        io::stdin()
            .read_line(&mut user_input)
            .expect("Failed to read line");
        user_input = match user_input.trim() {
            "q" => {
                break;
            }
            value => String::from(value),
        };

        match user_input.parse() {
            Ok(num) => {
                vec.push(num);
            }
            Err(_) => {
                println!("Please enter a valid number or enter 'q' to finish entering numbers.");
                continue;
            }
        };
        println!("{:#?}",vec);
    }
    let vec_median = median(& mut vec);

    println!("The median value of the vector is {}", vec_median);
    println!("The mode value of the vector is {:#?}", mode(&vec));

}

fn median(vec:& mut Vec<i32>)->f64{
    vec.sort();
    let result = if vec.len() % 2 == 1 { 
        vec[vec.len()/2] as f64 }
        else {
        (vec[vec.len()/2] + vec[vec.len()/2 - 1]) as f64/2.0
    };
    result
}

fn mode(vec:& Vec<i32>)->Vec<i32>{
    let mut vector_map = HashMap::new();
    let mut max_value: i32 = 0;
    let mut result: Vec<i32> = vec![];

    for item in vec{
        let count = vector_map.entry(item).or_insert(0);
        *count += 1;
    }

    for (_key,value) in &vector_map{
        if *value >= max_value{
            max_value = *value;            
    }}
    for (key,value) in &vector_map{
        if *value == max_value{
            result.push(**key);
        }}
    result
}    
