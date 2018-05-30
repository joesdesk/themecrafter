import pytest
from themecrafter.interface.session import ThemeCrafterSession

def test_load_preset_data():
    """Test a session's ability to load preset data."""
    session = ThemeCrafterSession()
    
    session.load_preset_data('NewsGroups')
    assert len(session.docs) > 0
    
    session.load_preset_data('BGSurvey')
    assert len(session.docs) > 0
    
    #session.load_preset_data('GradReports')
    #assert len(session.docs) > 0
    
    session.load_preset_data('StudentsReview')
    assert len(session.docs) > 0
    
    session.load_preset_data()
    assert len(session.docs)==0