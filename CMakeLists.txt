cmake_minimum_required(VERSION 3.5)
project(neo_simulation2)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch
  configs
  maps
  worlds
  robots
  rviz
  components
  models
  scripts
  DESTINATION share/${PROJECT_NAME})

ament_package()
