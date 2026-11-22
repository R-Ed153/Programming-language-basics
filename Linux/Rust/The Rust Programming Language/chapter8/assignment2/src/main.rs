fn main() {
    println!("Hello, world!");
    let test_string = String::from("testString");
    let a_test_string = String::from("aTestSting");

    println!(
        "test_string to pig_latin: {}",
        convert_to_pig_latin(&test_string)
    );
    println!(
        "a_test_string to pig_latin: {}",
        convert_to_pig_latin(&a_test_string)
    );
}

fn starts_with_a_vowel(raw_string: &str) -> bool {
    let vowel_list: [char; 5] = ['a', 'e', 'i', 'o', 'u'];
    let first_char = match raw_string.chars().next() {
        Some(first_char) => first_char.to_ascii_lowercase(),
        None => panic!("String is empty"),
    };
    for vowel in vowel_list {
        if first_char == vowel {
            return true;
        }
    }
    false
}

fn convert_to_pig_latin(raw_string: &str) -> String {
    let mut result = raw_string.to_string() + "-";
    if starts_with_a_vowel(raw_string) {
        result = result + "hay";
        return result;
    } else {
        let first_char = result.remove(0);
        result.push_str(&first_char.to_string());
        result = result + "ay";
    }
    result
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_starts_with_a_vowel() {
        assert_eq!(starts_with_a_vowel("testString"), false);
        assert_eq!(starts_with_a_vowel("aTestSting"), true);
    }
}
