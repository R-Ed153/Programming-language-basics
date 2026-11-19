fn main() {
    let s = takes_ownership("test");
    let x = makes_copy(5);

    println!("{s}")

}

fn takes_ownership(some_string: &str)-> String{
    println!("{some_string}");
    let result = String::from("Edmund");
    result
}

fn makes_copy(some_integer: i32) -> (){
    let result= String::from("Munene");
    //&result
}