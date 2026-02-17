from conecta4.list_utils import all_same
from conecta4.oracle import ColumnRecommendation, ColumnClassification



def test_all_same():
    assert all_same([1,2,3,4])== False
    assert all_same([[], [], []]) 
    assert all_same([])

    assert all_same([ColumnRecommendation(0, ColumnClassification.WIN),
                     ColumnRecommendation(2, ColumnClassification.WIN),
                     ColumnRecommendation(0, ColumnClassification.WIN)])
    
    assert all_same([ColumnRecommendation(0, ColumnClassification.WIN),
                     ColumnRecommendation(0, ColumnClassification.MAYBE),
                     ColumnRecommendation(0, ColumnClassification.WIN)]) == False