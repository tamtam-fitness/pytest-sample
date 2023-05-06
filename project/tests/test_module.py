from src import Module

class TestModule:
    
    def test_get_sys_path(self):
        
        exp = "/workdir"
        got = Module().get_sys_path()
        
        assert exp in got
