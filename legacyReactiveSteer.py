"""This doesn't work, its just here in case we feel like going back to it."""




        """WEEE! Reactive steering! This simply looks at how big the obstacle is
                and where it's at and steers away from it if it's in a collision course."""
        #Determine whether either point designated by the Tuple is within the straight-line
            #course of the robot
        left_x = obstacle[1]*math.sin(math.radians(obstacle[2]))
        right_x = obstacle[1]*math.sin(math.radians(obstacle[4]))
        #Figure out whether its to the left, right, or center and do something about it
        if (obstacle[2]>=0)and(obstacle[4]>=0):
            #Entire OBstacle is to the right of the robot center
            if obstacle[2]>(self.robot_width/2):
                #Obstacle is beyond the current collision path of the robot,
                #No action needed
                pass
            else:
                #Action required to steer left
                """Must fill in the appropriate motor control information here"""
                pass
        elif (obstacle[2]<0)and(obstacle[4]<0):
            #Entire Obstacle is to the left of the robot center
            if obstacle[4]<(-self.robot_width/2):
                #Obstacle is beyond the current collision path of the robot,
                #No action is needed
                pass
            else:
                #Action required to steer right
                """Must fill in the appropriate motor control information here"""
                pass
        else:
            #obstacle is centered on the robot
            """For the moment this is simply going to attempt to steer towards the
                side of the obstacle that is lesser, until one of the other contingencies
                sets in. If the obstacle is absolutely straight on, it will go the right.
                    (NOTE: This is temporary, this bit absolutely requires to have multi-
                        obstacle handling to determine the best accepted course between
                        all obstacles in the area when confronted with this situation."""
            if abs(obstacle[2])<abs(obstacle[4]):
                #steer to the left
                pass
            else:
                #steer to the right
                pass
