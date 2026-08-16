// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from br2_tracking_msgs:msg/PanTiltCommand.idl
// generated code does not contain a copyright notice

#include "br2_tracking_msgs/msg/detail/pan_tilt_command__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_br2_tracking_msgs
const rosidl_type_hash_t *
br2_tracking_msgs__msg__PanTiltCommand__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x8f, 0x02, 0x8a, 0xa7, 0xaf, 0x5f, 0x02, 0xb1,
      0x76, 0x25, 0x88, 0xbb, 0x18, 0xf8, 0x90, 0xeb,
      0xd5, 0x56, 0x87, 0x06, 0xc3, 0xa8, 0x48, 0xf2,
      0x35, 0xda, 0x51, 0xef, 0xa5, 0x40, 0xee, 0x9c,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char br2_tracking_msgs__msg__PanTiltCommand__TYPE_NAME[] = "br2_tracking_msgs/msg/PanTiltCommand";

// Define type names, field names, and default values
static char br2_tracking_msgs__msg__PanTiltCommand__FIELD_NAME__pan[] = "pan";
static char br2_tracking_msgs__msg__PanTiltCommand__FIELD_NAME__tilt[] = "tilt";

static rosidl_runtime_c__type_description__Field br2_tracking_msgs__msg__PanTiltCommand__FIELDS[] = {
  {
    {br2_tracking_msgs__msg__PanTiltCommand__FIELD_NAME__pan, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {br2_tracking_msgs__msg__PanTiltCommand__FIELD_NAME__tilt, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
br2_tracking_msgs__msg__PanTiltCommand__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {br2_tracking_msgs__msg__PanTiltCommand__TYPE_NAME, 36, 36},
      {br2_tracking_msgs__msg__PanTiltCommand__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 pan\n"
  "float64 tilt";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
br2_tracking_msgs__msg__PanTiltCommand__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {br2_tracking_msgs__msg__PanTiltCommand__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 25, 25},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
br2_tracking_msgs__msg__PanTiltCommand__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *br2_tracking_msgs__msg__PanTiltCommand__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
