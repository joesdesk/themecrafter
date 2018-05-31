import pytest
from themecrafter.datasets import NewsGroupsDataSet, BGSurveyDataSet, \
    GradReportsDataSet, StudentsReviewDataSet, SixDayWarDataSet
    
    
def test_load_preset_data():
    """Test a session's ability to load preset data."""
    
    dataset = NewsGroupsDataSet().X
    assert len(dataset) > 0
    
    dataset = BGSurveyDataSet().X
    assert len(dataset) > 0
    
    #dataset = GradReportsDataSet().X
    #assert len(dataset) > 0
    
    dataset = StudentsReviewDataSet().X
    assert len(dataset) > 0
    
    dataset = SixDayWarDataSet().X
    assert len(dataset) > 0
    
    