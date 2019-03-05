from switrs_to_sqlite.converters import convert, negative, string_to_bool
from switrs_to_sqlite.datatypes import DataType
import switrs_to_sqlite.value_maps as vm


COLLISION_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert, None),
    (3, "Jurisdiction", DataType.INTEGER, None, convert, None),
    (6, "Officer_ID", DataType.TEXT, None, convert, None),
    (7, "Reporting_District", DataType.TEXT, None, convert, None),
    (9, "CHP_Shift", DataType.TEXT, None, convert, None),
    (10, "Population", DataType.TEXT, None, convert, None),
    (11, "County_City_Location", DataType.TEXT, None, convert, None),
    (12, "Special_Condition", DataType.TEXT, None, convert, None),
    (13, "Beat_Type", DataType.TEXT, None, convert, None),
    (14, "CHP_Beat_Type", DataType.TEXT, None, convert, None),
    (15, "City_Division_LAPD", DataType.TEXT, ["0"], convert, None),
    (16, "CHP_Beat_Class", DataType.TEXT, None, convert, None),
    (17, "Beat_Number", DataType.TEXT, None, convert, None),
    (18, "Primary_Road", DataType.TEXT, None, convert, None),
    (19, "Secondary_Road", DataType.TEXT, None, convert, None),
    (20, "Distance", DataType.REAL, None, convert, None),
    (21, "Direction", DataType.TEXT, None, convert, None),
    (22, "Intersection", DataType.TEXT, None, string_to_bool, None),
    (23, "Weather_1", DataType.TEXT, None, convert, None),
    (24, "Weather_2", DataType.TEXT, None, convert, None),
    (25, "State_Highway_Indicator", DataType.INTEGER, None, string_to_bool, None),
    (26, "Caltrans_County", DataType.TEXT, None, convert, None),
    (27, "Caltrans_District", DataType.INTEGER, None, convert, None),
    (28, "State_Route", DataType.INTEGER, None, convert, None),
    (29, "Route_Suffix", DataType.TEXT, None, convert, None),
    (30, "Postmile_Prefix", DataType.TEXT, None, convert, None),
    (31, "Postmile", DataType.REAL, None, convert, None),
    (32, "Location_Type", DataType.TEXT, None, convert, None),
    (33, "Ramp_Intersection", DataType.INTEGER, None, convert, None),
    (34, "Side_Of_Highway", DataType.TEXT, None, convert, None),
    (35, "Tow_Away", DataType.INTEGER, None, string_to_bool, None),
    (36, "Collision_Severity", DataType.INTEGER, None, convert, None),
    (37, "Killed_Victims", DataType.INTEGER, None, convert, None),
    (38, "Injured_Victims", DataType.INTEGER, None, convert, None),
    (39, "Party_Count", DataType.INTEGER, None, convert, None),
    (40, "Primary_Collision_Factor", DataType.TEXT, None, convert, None),
    (41, "PCF_Violation_Code", DataType.TEXT, None, convert, None),
    (42, "PCF_Violation_Category", DataType.TEXT, None, convert, None),
    (43, "PCF_Violation", DataType.INTEGER, None, convert, None),
    (44, "PCF_Violation_Subsection", DataType.TEXT, None, convert, None),
    (45, "Hit_And_Run", DataType.TEXT, None, convert, None),
    (46, "Type_Of_Collision", DataType.TEXT, None, convert, None),
    (47, "Motor_Vehicle_Involved_With", DataType.TEXT, None, convert, None),
    (48, "Ped_Action", DataType.TEXT, None, convert, None),
    (49, "Road_Surface", DataType.TEXT, None, convert, None),
    (50, "Road_Condition_1", DataType.TEXT, None, convert, None),
    (51, "Road_Condition_2", DataType.TEXT, None, convert, None),
    (52, "Lighting", DataType.TEXT, None, convert, None),
    (53, "Control_Device", DataType.TEXT, None, convert, None),
    (54, "CHP_Road_Type", DataType.TEXT, None, convert, None),
    (55, "Pedestrian_Collision", DataType.INTEGER, None, string_to_bool, None),
    (56, "Bicycle_Collision", DataType.INTEGER, None, string_to_bool, None),
    (57, "Motorcycle_Collision", DataType.INTEGER, None, string_to_bool, None),
    (58, "Truck_Collision", DataType.INTEGER, None, string_to_bool, None),
    (59, "Not_Private_Property", DataType.INTEGER, None, string_to_bool, None),
    (60, "Alcohol_Involved", DataType.INTEGER, None, string_to_bool, None),
    (61, "Statewide_Vehicle_Type_At_Fault", DataType.TEXT, None, convert, vm.STATEWIDE_VEHICLE_TYPE),
    (62, "CHP_Vehicle_Type_At_Fault", DataType.TEXT, ["99"], convert, None),
    (63, "Severe_Injury_Count", DataType.INTEGER, None, convert, None),
    (64, "Other_Visible_Injury_Count", DataType.INTEGER, None, convert, None),
    (65, "Complaint_Of_Pain_Injury_Count", DataType.INTEGER, None, convert, None),
    (66, "Pedestrian_Killed_Count", DataType.INTEGER, None, convert, None),
    (67, "Pedestrian_Injured_Count", DataType.INTEGER, None, convert, None),
    (68, "Bicyclist_Killed_Count", DataType.INTEGER, None, convert, None),
    (69, "Bicyclist_Injured_Count", DataType.INTEGER, None, convert, None),
    (70, "Motorcyclist_Killed_Count", DataType.INTEGER, None, convert, None),
    (71, "Motorcyclist_Injured_Count", DataType.INTEGER, None, convert, None),
    (72, "Primary_Ramp", DataType.TEXT, None, convert, None),
    (73, "Secondary_Ramp", DataType.TEXT, None, convert, None),
    (74, "Latitude", DataType.REAL, None, convert, None),
    (75, "Longitude", DataType.REAL, None, negative, None),
)

COLLISION_DATE_TABLE = (
    (4, "Collision_Date", DataType.TEXT),
    (5, "Collision_Time", DataType.TEXT),
    (2, "Process_Date", DataType.TEXT),
)

PARTY_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert, None),
    (1, "Party_Number", DataType.INTEGER, None, convert, None),
    (2, "Party_Type", DataType.TEXT, None, convert, vm.PARTY_TYPE),
    (3, "At_Fault", DataType.TEXT, None, string_to_bool, None),
    (4, "Party_Sex", DataType.TEXT, None, convert, vm.SEX),
    (5, "Party_Age", DataType.INTEGER, ["998"], convert, None),
    (6, "Party_Sobriety", DataType.TEXT, None, convert, None),
    (7, "Party_Drug_Physical", DataType.TEXT, None, convert, None),
    (8, "Direction_Of_Travel", DataType.TEXT, None, convert, None),
    (9, "Party_Safety_Equipment_1", DataType.TEXT, None, convert, None),
    (10, "Party_Safety_Equipment_2", DataType.TEXT, None, convert, None),
    (11, "Financial_Responsibility", DataType.TEXT, None, convert, None),
    (12, "Hazardous_Materials", DataType.TEXT, None, convert, None),
    (13, "Cellphone_Use", DataType.TEXT, None, convert, None),
    (14, "School_Bus_Related", DataType.TEXT, None, convert, None),
    (15, "OAF_Violation_Code", DataType.TEXT, None, convert, None),
    (16, "OAF_Violation_Category", DataType.TEXT, ["00"], convert, None),
    (17, "OAF_Violation_Section", DataType.INTEGER, None, convert, None),
    (18, "OAF_Violation_Suffix", DataType.TEXT, None, convert, None),
    (19, "Other_Associate_Factor_1", DataType.TEXT, None, convert, None),
    (20, "Other_Associate_Factor_2", DataType.TEXT, None, convert, None),
    (21, "Party_Number_Killed", DataType.INTEGER, None, convert, None),
    (22, "Party_Number_Injured", DataType.INTEGER, None, convert, None),
    (23, "Movement_Preceding_Collision", DataType.TEXT, None, convert, vm.MOVEMENT_PRECEDING),
    (24, "Vehicle_Year", DataType.INTEGER, ["9999"], convert, None),
    (25, "Vehicle_Make", DataType.TEXT, None, convert, None),
    (26, "Statewide_Vehicle_Type", DataType.TEXT, None, convert, vm.STATEWIDE_VEHICLE_TYPE),
    (27, "CHP_Vehicle_Type_Towing", DataType.TEXT, ["99"], convert, None),
    (28, "CHP_Vehicle_Type_Towed", DataType.TEXT, ["99"], convert, None),
    (29, "Party_Race", DataType.TEXT, None, convert, None),
)

VICTIM_ROW = (
    (0, "Case_ID", DataType.TEXT, None, convert, None),
    (1, "Party_Number", DataType.INTEGER, None, convert, None),
    (2, "Victim_Role", DataType.TEXT, None, convert, None),
    (3, "Victim_Sex", DataType.TEXT, None, convert, vm.SEX),
    (4, "Victim_Age", DataType.INTEGER, ["998"], convert, None),
    (5, "Victim_Degree_Of_Injury", DataType.TEXT, None, convert, vm.DEGREE_OF_INJURY),
    (6, "Victim_Seating_Position", DataType.TEXT, None, convert, None),
    (7, "Victim_Safety_Equipment_1", DataType.TEXT, None, convert, None),
    (8, "Victim_Safety_Equipment_2", DataType.TEXT, None, convert, None),
    (9, "Victim_Ejected", DataType.TEXT, None, convert, None),
)
