from switrs_to_sqlite.datatypes import DataType
from switrs_to_sqlite.converters import convert, negative, string_to_bool


COLLISION_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert),
    (3, "Jurisdiction", DataType.INTEGER, None, convert),
    (6, "Officer_ID", DataType.TEXT, None, convert),
    (7, "Reporting_District", DataType.TEXT, None, convert),
    (9, "CHP_Shift", DataType.TEXT, None, convert),
    (10, "Population", DataType.TEXT, None, convert),
    (11, "County_City_Location", DataType.TEXT, None, convert),
    (12, "Special_Condition", DataType.TEXT, None, convert),
    (13, "Beat_Type", DataType.TEXT, None, convert),
    (14, "CHP_Beat_Type", DataType.TEXT, None, convert),
    (15, "City_Division_LAPD", DataType.TEXT, ['0'], convert),
    (16, "CHP_Beat_Class", DataType.TEXT, None, convert),
    (17, "Beat_Number", DataType.TEXT, None, convert),
    (18, "Primary_Road", DataType.TEXT, None, convert),
    (19, "Secondary_Road", DataType.TEXT, None, convert),
    (20, "Distance", DataType.REAL, None, convert),
    (21, "Direction", DataType.TEXT, None, convert),
    (22, "Intersection", DataType.TEXT, None, string_to_bool),
    (23, "Weather_1", DataType.TEXT, None, convert),
    (24, "Weather_2", DataType.TEXT, None, convert),
    (25, "State_Highway_Indicator", DataType.INTEGER, None, string_to_bool),
    (26, "Caltrans_County", DataType.TEXT, None, convert),
    (27, "Caltrans_District", DataType.INTEGER, None, convert),
    (28, "State_Route", DataType.INTEGER, None, convert),
    (29, "Route_Suffix", DataType.TEXT, None, convert),
    (30, "Postmile_Prefix", DataType.TEXT, None, convert),
    (31, "Postmile", DataType.REAL, None, convert),
    (32, "Location_Type", DataType.TEXT, None, convert),
    (33, "Ramp_Intersection", DataType.INTEGER, None, convert),
    (34, "Side_Of_Highway", DataType.TEXT, None, convert),
    (35, "Tow_Away", DataType.INTEGER, None, string_to_bool),
    (36, "Collision_Severity", DataType.INTEGER, None, convert),
    (37, "Killed_Victims", DataType.INTEGER, None, convert),
    (38, "Injured_Victims", DataType.INTEGER, None, convert),
    (39, "Party_Count", DataType.INTEGER, None, convert),
    (40, "Primary_Collision_Factor", DataType.TEXT, None, convert),
    (41, "PCF_Violation_Code", DataType.TEXT, None, convert),
    (42, "PCF_Violation_Category", DataType.TEXT, None, convert),
    (43, "PCF_Violation", DataType.INTEGER, None, convert),
    (44, "PCF_Violation_Subsection", DataType.TEXT, None, convert),
    (45, "Hit_And_Run", DataType.TEXT, None, convert),
    (46, "Type_Of_Collision", DataType.TEXT, None, convert),
    (47, "Motor_Vehicle_Involved_With", DataType.TEXT, None, convert),
    (48, "Ped_Action", DataType.TEXT, None, convert),
    (49, "Road_Surface", DataType.TEXT, None, convert),
    (50, "Road_Condition_1", DataType.TEXT, None, convert),
    (51, "Road_Condition_2", DataType.TEXT, None, convert),
    (52, "Lighting", DataType.TEXT, None, convert),
    (53, "Control_Device", DataType.TEXT, None, convert),
    (54, "CHP_Road_Type", DataType.TEXT, None, convert),
    (55, "Pedestrian_Collision", DataType.INTEGER, None, string_to_bool),
    (56, "Bicycle_Collision", DataType.INTEGER, None, string_to_bool),
    (57, "Motorcycle_Collision", DataType.INTEGER, None, string_to_bool),
    (58, "Truck_Collision", DataType.INTEGER, None, string_to_bool),
    (59, "Not_Private_Property", DataType.INTEGER, None, string_to_bool),
    (60, "Alcohol_Involved", DataType.INTEGER, None, string_to_bool),
    (61, "Statewide_Vehicle_Type_At_Fault", DataType.TEXT, None, convert),
    (62, "CHP_Vehicle_Type_At_Fault", DataType.TEXT, ["99"], convert),
    (63, "Severe_Injury_Count", DataType.INTEGER, None, convert),
    (64, "Other_Visible_Injury_Count", DataType.INTEGER, None, convert),
    (65, "Complaint_Of_Pain_Injury_Count", DataType.INTEGER, None, convert),
    (66, "Pedestrian_Killed_Count", DataType.INTEGER, None, convert),
    (67, "Pedestrian_Injured_Count", DataType.INTEGER, None, convert),
    (68, "Bicyclist_Killed_Count", DataType.INTEGER, None, convert),
    (69, "Bicyclist_Injured_Count", DataType.INTEGER, None, convert),
    (70, "Motorcyclist_Killed_Count", DataType.INTEGER, None, convert),
    (71, "Motorcyclist_Injured_Count", DataType.INTEGER, None, convert),
    (72, "Primary_Ramp", DataType.TEXT, None, convert),
    (73, "Secondary_Ramp", DataType.TEXT, None, convert),
    (74, "Latitude", DataType.REAL, None, convert),
    (75, "Longitude", DataType.REAL, None, negative),
)

COLLISION_DATE_TABLE = (
    (4, "Collision_Date", DataType.TEXT),
    (5, "Collision_Time", DataType.TEXT),
    (2, "Process_Date", DataType.TEXT),
)

PARTY_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert),
    (1, "Party_Number", DataType.INTEGER, None, convert),
    (2, "Party_Type", DataType.TEXT, None, convert),
    (3, "At_Fault", DataType.TEXT, None, string_to_bool),
    (4, "Party_Sex", DataType.TEXT, None, convert),
    (5, "Party_Age", DataType.INTEGER, ["998"], convert),
    (6, "Party_Sobriety", DataType.TEXT, None, convert),
    (7, "Party_Drug_Physical", DataType.TEXT, None, convert),
    (8, "Direction_Of_Travel", DataType.TEXT, None, convert),
    (9, "Party_Safety_Equipment_1", DataType.TEXT, None, convert),
    (10, "Party_Safety_Equipment_2", DataType.TEXT, None, convert),
    (11, "Financial_Responsibility", DataType.TEXT, None, convert),
    (12, "Hazardous_Materials", DataType.TEXT, None, convert),
    (13, "Cellphone_Use", DataType.TEXT, None, convert),
    (14, "School_Bus_Related", DataType.TEXT, None, convert),
    (15, "OAF_Violation_Code", DataType.TEXT, None, convert),
    (16, "OAF_Violation_Category", DataType.TEXT, ["00"], convert),
    (17, "OAF_Violation_Section", DataType.INTEGER, None, convert),
    (18, "OAF_Violation_Suffix", DataType.TEXT, None, convert),
    (19, "Other_Associate_Factor_1", DataType.TEXT, None, convert),
    (20, "Other_Associate_Factor_2", DataType.TEXT, None, convert),
    (21, "Party_Number_Killed", DataType.INTEGER, None, convert),
    (22, "Party_Number_Injured", DataType.INTEGER, None, convert),
    (23, "Movement_Preceding_Collision", DataType.TEXT, None, convert),
    (24, "Vehicle_Year", DataType.INTEGER, ["9999"], convert),
    (25, "Vehicle_Make", DataType.TEXT, None, convert),
    (26, "Statewide_Vehicle_Type", DataType.TEXT, None, convert),
    (27, "CHP_Vehicle_Type_Towing", DataType.TEXT, ["99"], convert),
    (28, "CHP_Vehicle_Type_Towed", DataType.TEXT, ["99"], convert),
    (29, "Party_Race", DataType.TEXT, None, convert),
)

VICTIM_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert),
    (1, "Party_Number", DataType.INTEGER, None, convert),
    (2, "Victim_Role", DataType.TEXT, None, convert),
    (3, "Victim_Sex", DataType.TEXT, None, convert),
    (4, "Victim_Age", DataType.INTEGER, ["998"], convert),
    (5, "Victim_Degree_Of_Injury", DataType.TEXT, None, convert),
    (6, "Victim_Seating_Position", DataType.TEXT, None, convert),
    (7, "Victim_Safety_Equipment_1", DataType.TEXT, None, convert),
    (8, "Victim_Safety_Equipment_2", DataType.TEXT, None, convert),
    (9, "Victim_Ejected", DataType.TEXT, None, convert),
)