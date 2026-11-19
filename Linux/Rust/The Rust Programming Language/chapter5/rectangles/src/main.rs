#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let width1 = 30;
    let height1 = 50;
    let scale = 2;

    println!(
        "The area of the rectangle1 is {} square pixels",
        area(width1, height1)
    );

    let rect2 = (30, 50);
    println!(
        "The area of the rectangle2 is {} square pixels",
        area2(rect2)
    );

    let rect3 = Rectangle {
        width: dbg!(30 * scale),
        height: 50,
    };
    println!(
        "The area of the rectangle3 is {} square pixels",
        area3(&rect3)
    );
    println!("rect3 is {:#?}", rect3);
    dbg!(&rect3);
    println!("{}",rect3.area());

    let square = Rectangle::square(3);
    println!("Square area: {:#?}", square.area());
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}

fn area2(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}

fn area3(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
