struct User{
    active: bool,
    username: String,
    email: String,
    sign_in_count : u64,
}

struct Color(i32,i32,i32);
struct Point(i32,i32,i32);



fn main() {
    let mut user1 = User{
        active: true,
        username: String::from("Edmund Munene"),
        email: String::from("edmundmunene@gmail.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("r.munene@students.jkuat.ac.ke");

    let black = Color(0,0,0);
    let origin = Point(0,0,0);
}

fn build_user(email: String, username: String) -> User{
    //init shortcut (only when function parameter is similar to struct field)
    User{
        active: true,
        username,
        email,
        sign_in_count:1,
    }
}
