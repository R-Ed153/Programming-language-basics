fn main() {
    let my_string = String::from("hello world");
    let word = first_word(&my_string[0..6]);
    println!("&String slice [0..6]: {word}");
    let word = first_word(&my_string[..]);
    println!("&String slice [..]: {word}");

    let word = first_word(&my_string);
    println!("&String [..]: {word}");

    let my_string_literal = "hello world";
    let word = first_word(&my_string_literal[0..6]);
    println!("&String literal [0..6]: {word}");
    let word = first_word(&my_string_literal[..]);
    println!("&String literal [..]: {word}");
    let word = first_word(my_string_literal);
    println!("&String literal: {word}");
}

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}
