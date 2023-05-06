from src.sub import SubModule

class TestSubModule:
    
    def test_get_sys_path(self):
        
        exp = "hello from sub_module"
        got = SubModule().hello()
        
        assert exp == got
