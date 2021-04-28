import CSVTable
import CSVCatalog
import json
import csv
import time

# define column definition.
people_columns_def = [CSVCatalog.ColumnDefinition("playerID", "text", True),
                      CSVCatalog.ColumnDefinition("birthYear", "text", True),
                      CSVCatalog.ColumnDefinition("birthMonth", "text", True),
                      CSVCatalog.ColumnDefinition("birthDay", "text", True),
                      CSVCatalog.ColumnDefinition("birthCountry", "text", True),
                      CSVCatalog.ColumnDefinition("birthState", "text", True),
                      CSVCatalog.ColumnDefinition("birthCity", "text", False),
                      CSVCatalog.ColumnDefinition("deathYear", "text", False),
                      CSVCatalog.ColumnDefinition("deathMonth", "text", False),
                      CSVCatalog.ColumnDefinition("deathDay", "text", False),
                      CSVCatalog.ColumnDefinition("deathCountry", "text", False),
                      CSVCatalog.ColumnDefinition("deathState", "text", False),
                      CSVCatalog.ColumnDefinition("deathCity", "text", False),
                      CSVCatalog.ColumnDefinition("nameFirst", "text", False),
                      CSVCatalog.ColumnDefinition("nameLast", "text", False),
                      CSVCatalog.ColumnDefinition("nameGiven", "text", False),
                      CSVCatalog.ColumnDefinition("weight", "text", False),
                      CSVCatalog.ColumnDefinition("height", "text", False),
                      CSVCatalog.ColumnDefinition("bats", "text", False),
                      CSVCatalog.ColumnDefinition("throws", "text", False),
                      CSVCatalog.ColumnDefinition("debut", "text", False),
                      CSVCatalog.ColumnDefinition("finalGame", "text", False),
                      CSVCatalog.ColumnDefinition("retroID", "text", False),
                      CSVCatalog.ColumnDefinition("bbrefID", "text", False)]
# playerID	yearID	stint	teamID	lgID	G	AB	R	H	2B	3B	HR	RBI	SB	CS	BB	SO	IBB	HBP	SH	SF	GIDP
batting_columns_def = [CSVCatalog.ColumnDefinition("playerID", "text", True),
                       CSVCatalog.ColumnDefinition("yearID", "text", True),
                       CSVCatalog.ColumnDefinition("stint", "text", True),
                       CSVCatalog.ColumnDefinition("teamID", "text", True),
                       CSVCatalog.ColumnDefinition("lgID", "text", True),
                       CSVCatalog.ColumnDefinition("G", "text", True),
                       CSVCatalog.ColumnDefinition("AB", "text", False),
                       CSVCatalog.ColumnDefinition("R", "text", False),
                       CSVCatalog.ColumnDefinition("H", "text", False),
                       CSVCatalog.ColumnDefinition("2B", "text", False),
                       CSVCatalog.ColumnDefinition("3B", "text", False),
                       CSVCatalog.ColumnDefinition("HR", "text", False),
                       CSVCatalog.ColumnDefinition("RBI", "text", False),
                       CSVCatalog.ColumnDefinition("SB", "text", False),
                       CSVCatalog.ColumnDefinition("CS", "text", False),
                       CSVCatalog.ColumnDefinition("BB", "text", False),
                       CSVCatalog.ColumnDefinition("SO", "text", False),
                       CSVCatalog.ColumnDefinition("IBB", "text", False),
                       CSVCatalog.ColumnDefinition("HBP", "text", False),
                       CSVCatalog.ColumnDefinition("SH", "text", False),
                       CSVCatalog.ColumnDefinition("SF", "text", False),
                       CSVCatalog.ColumnDefinition("GIDP", "text", False)]
# yearID	teamID	lgID	playerID	G_all	GS	G_batting	G_defense	G_p	G_c	G_1b	G_2b	G_3b	G_ss	G_lf	G_cf	G_rf
# G_of	G_dh	G_ph	G_pr
appearances_columns_def = [CSVCatalog.ColumnDefinition("yearID", "text", True),
                           CSVCatalog.ColumnDefinition("teamID", "text", True),
                           CSVCatalog.ColumnDefinition("lgID", "text", True),
                           CSVCatalog.ColumnDefinition("playerID", "text", True),
                           CSVCatalog.ColumnDefinition("G_all", "text", False),
                           CSVCatalog.ColumnDefinition("GS", "text", False),
                           CSVCatalog.ColumnDefinition("G_batting", "text", False),
                           CSVCatalog.ColumnDefinition("G_defense", "text", False),
                           CSVCatalog.ColumnDefinition("G_p", "text", False),
                           CSVCatalog.ColumnDefinition("G_c", "text", False),
                           CSVCatalog.ColumnDefinition("G_1b", "text", False),
                           CSVCatalog.ColumnDefinition("G_2b", "text", False),
                           CSVCatalog.ColumnDefinition("G_3b", "text", False),
                           CSVCatalog.ColumnDefinition("G_ss", "text", False),
                           CSVCatalog.ColumnDefinition("G_lf", "text", False),
                           CSVCatalog.ColumnDefinition("G_cf", "text", False),
                           CSVCatalog.ColumnDefinition("G_rf", "text", False),
                           CSVCatalog.ColumnDefinition("G_of", "text", False),
                           CSVCatalog.ColumnDefinition("G_dh", "text", False),
                           CSVCatalog.ColumnDefinition("G_ph", "text", False),
                           CSVCatalog.ColumnDefinition("G_pr", "text", False)
                           ]

# Must clear out all tables in CSV Catalog schema before using if there are any present
# Please change the path name to be whatever the path to the CSV files are
# First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided
def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")
    pass
# drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("people", "NewPeople.csv")
    cat.create_table("batting", "NewBatting.csv")
    cat.create_table("appearances", "NewAppearances.csv")
    pass
""" reserved
    cat.create_table("people", "NewPeople.csv", column_definitions=people_columns_def)
    cat.create_table("batting", "NewBatting.csv", column_definitions=batting_columns_def)
    cat.create_table("appearances", "NewAppearances.csv", column_definitions=appearances_columns_def)
"""
#create_lahman_tables()

# Note: You can default all column types to text
def update_people_columns():
    # ************************ TO DO **************************
    cat = CSVCatalog.CSVCatalog()
    people = cat.get_table("people")
    for cn in people_columns_def:
        people.add_column_definition(cn)
    pass
#update_people_columns()

def update_appearances_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    appearances = cat.get_table("appearances")
    for cn in appearances_columns_def:
        appearances.add_column_definition(cn)
    pass

#update_appearances_columns()

def update_batting_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    batting = cat.get_table("batting")
    for cn in batting_columns_def:
        batting.add_column_definition(cn)
    pass
#update_batting_columns()

#Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    people = cat.get_table("people")
    batting = cat.get_table("batting")
    appearances = cat.get_table("appearances")
    people.define_index("playerID", ["playerID"], type='PRIMARY')
    batting.define_index("playerID_stint_yearID", ["playerID", "stint", "yearID"], type='PRIMARY')
    appearances.define_index("yearID_teamID_playerID", ["yearID", "teamID", "playerID"], type='PRIMARY')
    pass

#add_index_definitions()

def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)

#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("people")
    names = table.__get_column_names__()
    print(names)

#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    # Minimal index definition
    cat = CSVCatalog.CSVCatalog()
    people = cat.get_table("people")
    batting = cat.get_table("batting")
    appearances = cat.get_table("appearances")
    people.define_index("last_first", ["nameLast", "nameFirst"], type='INDEX')
    batting.define_index("yearID", ["yearID"], type='INDEX')
    pass


def load_test():
    batting_table = CSVTable.CSVTable("batting")
    print(batting_table)

#load_test()

def dumb_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    #    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"load_test], {"playerID": "baxtemi01"},
    #                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    start_time = time.time()
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"teamID": "BOS", "yearID": "2000"},
                                          ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    end_time = time.time()
    if result:
        print(result)
    print("Duration for dumb_join = ", end_time - start_time)
#dumb_join_test()

def get_access_path_test():
    batting_table = CSVTable.CSVTable("batting")
    template = ["teamID", "playerID", "stint", "yearID"]
    index_result, count = batting_table.__get_access_path__(template)
    print(index_result)
    print(count)

#get_access_path_test()

def sub_where_template_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    template = {"teamID": "BOS", "yearID":"1932"}
    BOS_1932_template = batting_table.__get_sub_where_template__(template)
    BOS_1932_batting_data = batting_table.__find_by_template__(BOS_1932_template)
    print(BOS_1932_batting_data)

    pass

#sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    row = []
    batting_table = CSVTable.CSVTable("batting")
    template = {"playerID": "bakerdo01", "yearID": "1984", "stint": "1"}   # template is a dictionary
    result_index, count = batting_table.__get_access_path__(list(template.keys()))
    if result_index is not None:
        row = batting_table.__find_by_template_index__(template, result_index)
    print(row)
    pass

#test_find_by_template_index()


def test_find_by_template_scan():
    # ************************ TO DO ***************************

    batting_table = CSVTable.CSVTable("batting")
    # print(batting_table)
    template = { "playerID": "bakerdo01"}   # template is a dictionary
    start_time = time.time()
    row = batting_table.__find_by_template_scan__(template, ["playerID", "yearID","3B","IBB"])
    end_time = time.time()

    print(row)
    print("Duration for find_by_template_scan = ", end_time - start_time)

    pass


def smart_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
#    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
#                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    start_time = time.time()
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"], {"teamID": "BOS", "yearID": "2000"},
                                          ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    end_time = time.time()
    if result:
        print(result)
    print("Duration for smart_join = ", end_time - start_time, "s")

#smart_join_test()


"""
drop_tables_for_prep()
create_lahman_tables()
update_people_columns()
update_batting_columns()
update_appearances_columns()
add_index_definitions()
add_other_indexes()
sub_where_template_test()
test_find_by_template_index()
smart_join_test()

drop_tables_for_prep()
create_lahman_tables()
update_people_columns()
update_batting_columns()
update_appearances_columns()
add_index_definitions()
add_other_indexes()
test_load_info()
test_get_col_names()
load_test()
dumb_join_test()


"""