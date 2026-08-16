#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "br2_tracking_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__br2_tracking_msgs__msg__PanTiltCommand() -> *const std::ffi::c_void;
}

#[link(name = "br2_tracking_msgs__rosidl_generator_c")]
extern "C" {
    fn br2_tracking_msgs__msg__PanTiltCommand__init(msg: *mut PanTiltCommand) -> bool;
    fn br2_tracking_msgs__msg__PanTiltCommand__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<PanTiltCommand>, size: usize) -> bool;
    fn br2_tracking_msgs__msg__PanTiltCommand__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<PanTiltCommand>);
    fn br2_tracking_msgs__msg__PanTiltCommand__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<PanTiltCommand>, out_seq: *mut rosidl_runtime_rs::Sequence<PanTiltCommand>) -> bool;
}

// Corresponds to br2_tracking_msgs__msg__PanTiltCommand
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PanTiltCommand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pan: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub tilt: f64,

}



impl Default for PanTiltCommand {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !br2_tracking_msgs__msg__PanTiltCommand__init(&mut msg as *mut _) {
        panic!("Call to br2_tracking_msgs__msg__PanTiltCommand__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for PanTiltCommand {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { br2_tracking_msgs__msg__PanTiltCommand__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { br2_tracking_msgs__msg__PanTiltCommand__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { br2_tracking_msgs__msg__PanTiltCommand__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for PanTiltCommand {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for PanTiltCommand where Self: Sized {
  const TYPE_NAME: &'static str = "br2_tracking_msgs/msg/PanTiltCommand";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__br2_tracking_msgs__msg__PanTiltCommand() }
  }
}


