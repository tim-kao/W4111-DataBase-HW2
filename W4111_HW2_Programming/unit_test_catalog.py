import CSVCatalog
import json
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

# Example test, you will have to update the connection info
# Implementation Provided
def create_table_test():
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("people", "NewPeople.csv")
    cat.create_table("batting", "NewBatting.csv")
    cat.create_table("appearances", "NewAppearances.csv")
    pass
"""
    batting = cat.get_table("batting")
    appearances = cat.get_table("appearances")
    people = cat.get_table("people")
    print("Table = ", batting)
    print("Table = ", appearances)
    print("Table = ", people)
"""

def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("batting")
    cat.drop_table("appearances")
    cat.drop_table("people")
    pass


#drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    appearances = cat.get_table("appearances")
    for cn in appearances_columns_def:
        appearances.add_column_definition(cn)
    batting = cat.get_table("batting")
    for cn in batting_columns_def:
        batting.add_column_definition(cn)
    people = cat.get_table("people")
    for cn in people_columns_def:
        people.add_column_definition(cn)
    print("Table = ", batting)
    pass

#add_column_test()

# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("people")
    t.add_column_definition(col)

#column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("people")
    t.add_column_definition(col)

#column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("people")
    t.add_column_definition(col)
    t.add_column_definition(col)
#column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    people = cat.get_table("people")
    batting = cat.get_table("batting")
    appearances = cat.get_table("appearances")
    people.define_index("playerID", ["playerID"], type='PRIMARY')
    batting.define_index("playerID_stint_yearID", ["playerID", "stint", "yearID"], type='PRIMARY')
    appearances.define_index("yearID_teamID_playerID", ["yearID", "teamID", "playerID"], type='PRIMARY')
    pass

#add_index_test()

def col_drop_test():
    # call drop_column_definition with column name
    cat = CSVCatalog.CSVCatalog()
    batting = cat.get_table("batting")
    batting.drop_column_definition("2B")
    print(batting)
    pass

#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    batting = cat.get_table("batting")
    batting.drop_index("playerID_stint_yearID")
    print(batting)
    pass

#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("people")
    desc = t.describe_table()
    print("DESCRIBE People = \n", json.dumps(desc, indent=2))
"""
drop_table_test()
create_table_test()
add_column_test()
add_index_test()
col_drop_test()
index_drop_test()
column_name_failure_test()
column_type_failure_test()
column_not_null_failure_test()
describe_table_test()
"""
