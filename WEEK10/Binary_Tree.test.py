# Unit test for inserting a new province at the root of an empty tree
def test_insert_province_at_root():
    # Create an empty tree
    root = None

    # Insert a new province at the root
    provinces = [
        ("Banteay Meanchey", 859549), ("Battambang", 1036288), ("Kampong Cham", 928694), ("Kampong Chhnang", 523202),
        ("Kampong Speu", 872219), ("Kampong Thom", 690414), ("Kampot", 585850), ("Kandal", 1195547), ("Kep", 41798),
        ("Koh Kong", 117481), ("Kratie", 366666), ("Mondulkiri", 92995), ("Oddar Meanchey", 231390), ("Pailin", 70482),
        ("Preah Vihear", 251645), ("Prey Veng", 947357), ("Pursat", 397161), ("Ratanakiri", 204027), ("Siem Reap", 1006512),
        ("Preah Sihanouk", 302887), ("Stung Treng", 122791), ("Svay Rieng", 482785), ("Takeo", 843931), ("Tbong Khmum", 754000)
    ]

    root = Node(provinces[0][0])

    # Assert that the root is not None
    assert root is not None

    # Assert that the root's data is the first province in the list
    assert root.data == provinces[0][0]

    # Assert that the tree has only one node after inserting the first province
    assert root.count_nodes() == 1

# Run the unit test
test_insert_province_at_root()