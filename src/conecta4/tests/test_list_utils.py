from conecta4.list_utils import all_same



def test_all_same():
    assert all_same([1,2,3,4])== False
    assert all_same([[], [], []]) 
    assert all_same([])

