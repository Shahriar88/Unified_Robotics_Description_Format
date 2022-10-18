# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:21:40 2022
http://www.mymodelrobot.appspot.com/5629499534213120

https://scikit-robot.readthedocs.io/en/latest/examples/index.html
https://scikit-robot.readthedocs.io/en/latest/reference/coordinates.html


@author: shahriar

pip install skrobot==1.0.13
"""


import skrobot
import numpy as np
from time import sleep

class urdf_view:
    
    def __init__(self,file_name = "six_axis_robot_arm.urdf"):
        self.robot_model = skrobot.models.urdf.RobotModelFromURDF(urdf_file=file_name)
        self.n_joints=len(self.robot_model.joint_list)
        #>>>
        self.viewer = skrobot.viewers.TrimeshSceneViewer(resolution=(640, 480))
        self.viewer.add(self.robot_model)
        self.viewer.show()
        sleep(0.1)
        self.viewer.set_camera(angles=[np.deg2rad(90), 0, 0],distance=1.5)
        self.viewer.redraw()
        
        for link in self.robot_model.link_list:
            print(link.name)
        
        for joint in self.robot_model.joint_list:
            print(joint.name)
        
        #robot_model.js_1_2.joint_angle(0.5)
        #robot_model.js_1_2.joint_angle()
        #robot_model.js_6_7.joint_angle(0.5)
        #robot_model.js_9_10.joint_angle(1.57)
    
    
    #>>>>>>>>>>>>>>>>>>>>>>>>    
    def deg_to_rad(self,deg):
        return np.deg2rad(deg)
    
    def rad_to_deg(self,rad):
        return np.rad2deg(rad)
        
    #>>>>>>>>>>>>>>>>>>>>>>>
    def get_joint_angle_rad(self,joint_id):
        return self.robot_model.joint_list[joint_id].joint_angle()
        
    def set_joint_angle_rad(self,joint_id,angle_rad):
        self.robot_model.joint_list[joint_id].joint_angle(angle_rad)  
        self.viewer.redraw()
            #>>>
    def get_joint_angle_deg(self,joint_id):
        temp=self.get_joint_angle_rad(joint_id)
        return self.rad_to_deg(temp)
        
    #>>>>>>>>>>>>>>>>>>>>>>>>
    def get_joints_angles_rad(self):
        joints=[]
        for i in self.robot_model.joint_list:
            joints.append(i)
        return joints
        
    def set_joints_angles_rad(self,angles_rad_array):
        for i in range(self.n_joints):
            self.robot_model.joint_list[i].joint_angle(angles_rad_array[i])
            self.viewer.redraw()
            #>>>        
    def get_joints_angles_deg(self):
        joints=[]
        for i in self.robot_model.joint_list:
            joints.append(i)
        return self.rad_to_deg(joints)
        
    #>>>>>>>>>>>>>>>>>>>>>>>>
    


if __name__ == "__main__":
    mycobot=urdf_view()
    mycobot.set_joint_angle_rad(3, 1.57)
    sleep(5)
    angles=[.2,.1,.4,.6,.1,1.57]
    mycobot.set_joints_angles_rad(angles)
    
    
    
