#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to br2_tracking_msgs__msg__PanTiltCommand

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::PanTiltCommand::default())
  }
}

impl rosidl_runtime_rs::Message for PanTiltCommand {
  type RmwMsg = super::msg::rmw::PanTiltCommand;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pan: msg.pan,
        tilt: msg.tilt,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      pan: msg.pan,
      tilt: msg.tilt,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pan: msg.pan,
      tilt: msg.tilt,
    }
  }
}


